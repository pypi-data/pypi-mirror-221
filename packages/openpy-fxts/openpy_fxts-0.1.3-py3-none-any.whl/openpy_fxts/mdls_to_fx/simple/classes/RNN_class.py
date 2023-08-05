# -*- coding: utf-8 -*-
# @Time    : 14/07/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fxts.base_tf import tkl, tkm, value_miss
from openpy_fxts.layers.layers_class import type_rnn, rnn_drop, dense_multi_out
from openpy_fxts.mdls_to_fx.get_arch_dicts import _get_config_rnn


class rnn_dense_class(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(rnn_dense_class, self).__init__()
        if config is None:
            config = _get_config_rnn('rnn_dense')
        self.n_future = n_future
        self.n_out_ft = n_out_ft
        self.config = config
        mdl = type_rnn(config['rnn_layers']['type'])
        units = config['rnn_layers']['units']
        activations = config['rnn_layers']['activations']
        sequences = config['rnn_layers']['sequences']
        self.hidden_rnn = []
        for _, (unit, act, seq) in enumerate(zip(units, activations, sequences)):
            self.hidden_rnn.append(
                rnn_drop(
                    mdl,
                    unit,
                    act,
                    seq,
                    config['dropout']['activate'],
                    config['dropout']['rate']
                )
            )
        if config['dense_layer']['activate']:
            self.hidden_dense = tkl.Dense(
                config['dense_layer']['units'],
                activation=config['dense_layer']['activation']
            )
        self.layer_output = dense_multi_out(n_future, n_out_ft, config['output_layer']['activation'])

    def call(self, inputs, training=True, **kwargs):
        for j, (rnn) in enumerate(self.hidden_rnn):
            if j == 0:
                x = rnn(inputs)
            else:
                x = rnn(x)
        if self.config['dense_layer']['activate']:
            x = self.hidden_dense(x)
        x = self.layer_output(x)
        return x


class birnn_timedist_dense_class(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(birnn_timedist_dense_class, self).__init__()
        if config is None:
            config = _get_config_rnn('birnn_timedist_dense')
        self.n_future = n_future
        self.n_out_ft = n_out_ft
        self.config = config
        units = config['timedist_dense_layers']['units']
        activations = config['timedist_dense_layers']['activations']
        self.hidden_rnn = rnn_drop(
            mdl=type_rnn(config['rnn_layer']['type']),
            n_units=config['rnn_layer']['units'],
            activation=config['rnn_layer']['activations'],
            return_seq=config['rnn_layer']['sequences'],
            is_drop=False,
            rate=0.3,
            bidirectional=True
        )
        self.hidden_timedist_dense = []
        for j, (unit, act) in enumerate(zip(units, activations)):
            self.hidden_timedist_dense.append(tkl.TimeDistributed(tkl.Dense(units=unit, activation=act)))
        self.flatten = tkl.Flatten()
        self.hidden_dense = tkl.Dense(
            config['dense_layer']['units'],
            activation=config['dense_layer']['activation']
        )
        if config['dropout']['activate']:
            self.drop = tkl.Dropout(config['dropout']['rate'])
        self.layer_output = dense_multi_out(n_future, n_out_ft, config['output_layer']['activation'])

    def call(self, inputs, training=True, **kwargs):
        x = self.hidden_rnn(inputs)
        for layer in self.hidden_timedist_dense:
            x = layer(x)
        x = self.flatten(x)
        x = self.hidden_dense(x)
        if self.config['dropout']['activate']:
            x = self.drop(x)
        x = self.layer_output(x)
        return x


class multi_rnn_dense_class(tkm.Model):
    def __init__(
            self,
            n_past=None,
            n_inp_ft=None,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(multi_rnn_dense_class, self).__init__()
        if config is None:
            config = _get_config_rnn('multi_rnn_dense')
        self.n_past = n_past
        self.n_inp_ft = n_inp_ft
        self.n_future = n_future
        self.n_out_ft = n_out_ft
        self.config = config
        mdl = type_rnn(config['multi_rnn_layers']['type'])
        self.hidden_inp = []
        dimensions = config['multi_rnn_layers']['units']
        activations = config['multi_rnn_layers']['activations']
        sequences = config['multi_rnn_layers']['sequences']
        self.hidden_rnn_dict = dict()
        for i in range(n_inp_ft):
            dict_rnn = {}
            for j, (unit, act, seq) in enumerate(zip(dimensions, activations, sequences)):
                dict_rnn['' + str(j)] = rnn_drop(
                    mdl,
                    unit,
                    act,
                    seq,
                    config['dropout']['activate'],
                    config['dropout']['rate']
                )
            self.hidden_rnn_dict['' + str(i)] = dict_rnn
        self.concat = tkl.Concatenate(axis=1)
        if config['dropout']['activate']:
            self.drop1 = tkl.Dropout(config['dropout']['rate'])
        self.hidden_rnn = mdl(
            units=config['rnn_layer']['units'],
            activation=config['rnn_layer']['activation'],
            return_sequences=config['rnn_layer']['sequences']
        )
        if config['dropout']['activate']:
            self.drop2 = tkl.Dropout(config['dropout']['rate'])
        if config['dense_layer']['activate']:
            self.hidden_dense = tkl.Dense(
                config['dense_layer']['units'],
                activation=config['dense_layer']['activation']
            )
        self.dense_out = dense_multi_out(n_future, n_out_ft, config['output_layer']['activation'])

    def call(self, inputs, training=True, **kwargs):
        head_list = []
        for _, dict_aux in self.hidden_rnn_dict.items():
            for i, (_, layer_rnn) in enumerate(dict_aux.items()):
                if i == 0:
                    y = layer_rnn(inputs)
                else:
                    y = layer_rnn(y)
            head_list.append(y)
        x = self.concat(head_list)
        x = tkl.Reshape((head_list[0].shape[1], self.n_inp_ft))(x)
        if self.config['dropout']['activate']:
            x = self.drop1(x)
        x = self.hidden_rnn(x)
        if self.config['dropout']['activate']:
            x = self.drop2(x)
        if self.config['dense_layer']['activate']:
            x = self.hidden_dense(x)
        x = self.dense_out(x)
        return x


class birnn_dense_class(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(birnn_dense_class, self).__init__()
        if config is None:
            config = _get_config_rnn('birnn_dense')
        self.n_future = n_future
        self.n_out_ft = n_out_ft
        self.config = config
        mdl = type_rnn(config['rnn_layers'][''])
        units = config['rnn_layers']['units']
        activations = config['rnn_layers']['activations']
        sequences = config['rnn_layers']['sequences']
        self.hidden_rnn = []
        for _, (unit, act, seq) in enumerate(zip(units, activations, sequences)):
            self.hidden_rnn.append(
                rnn_drop(
                    mdl,
                    unit,
                    act,
                    seq,
                    config['dropout']['activate'],
                    config['dropout']['rate'],
                    True
                )
            )
        if config['dense_layer']['activate']:
            self.hidden_dense = tkl.Dense(
                config['dense_layer']['units'],
                activation=config['dense_layer']['activation']
            )
        self.layer_output = dense_multi_out(n_future, n_out_ft, config['output_layer']['activation'])

    def call(self, inputs, training=True, **kwargs):
        for j, (rnn) in enumerate(self.hidden_rnn):
            if j == 0:
                x = rnn(inputs)
            else:
                x = rnn(x)
        if self.config['dense_layer']['activate']:
            x = self.hidden_dense(x)
        x = self.layer_output(x)
        return x


class multi_birnn_dense_class(tkm.Model):

    def __init__(
            self,
            n_past=None,
            n_inp_ft=None,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(multi_rnn_dense_class, self).__init__()
        if config is None:
            config = _get_config_rnn('multi_birnn_dense')
        mdl = type_rnn(config['multi_rnn_layers']['type'])
        self.n_past = n_past
        self.n_inp_ft = n_inp_ft
        self.n_future = n_future
        self.n_out_ft = n_out_ft
        self.config = config
        self.hidden_inp = []
        dimensions = config['multi_rnn_layers']['units']
        activations = config['multi_rnn_layers']['activations']
        sequences = config['multi_rnn_layers']['sequences']
        self.hidden_rnn_dict = dict()
        for i in range(n_inp_ft):
            dict_rnn = {}
            for j, (unit, act, seq) in enumerate(zip(dimensions, activations, sequences)):
                dict_rnn['' + str(j)] = rnn_drop(
                    mdl,
                    unit,
                    act,
                    seq,
                    config['dropout']['activate'],
                    config['dropout']['rate'],
                    True
                )
            self.hidden_rnn_dict['' + str(i)] = dict_rnn
        self.concat = tkl.Concatenate(axis=1)
        if config['dropout']['activate']:
            self.drop1 = tkl.Dropout(config['dropout']['rate'])
        self.hidden_rnn = mdl(
            units=config['rnn_layer']['units'],
            activation=config['rnn_layer']['activation'],
            return_sequences=config['rnn_layer']['sequences']
        )
        if config['dropout']['activate']:
            self.drop2 = tkl.Dropout(config['dropout']['rate'])
        if config['dense_layer']['activate']:
            self.hidden_dense = tkl.Dense(
                config['dense_layer']['units'],
                activation=config['dense_layer']['activation']
            )
        self.dense_out = dense_multi_out(n_future, n_out_ft, config['output_layer']['activation'])

    def call(self, inputs, training=True, **kwargs):
        head_list = []
        for _, dict_aux in self.hidden_rnn_dict.items():
            for i, (_, layer_rnn) in enumerate(dict_aux.items()):
                if i == 0:
                    y = layer_rnn(inputs)
                else:
                    y = layer_rnn(y)
            head_list.append(y)
        x = self.concat(head_list)
        x = tkl.Reshape((head_list[0].shape[1], self.n_inp_ft))(x)
        if self.config['dropout']['activate']:
            x = self.drop1(x)
        x = self.hidden_rnn(x)
        if self.config['dropout']['activate']:
            x = self.drop2(x)
        if self.config['dense_layer']['activate']:
            x = self.hidden_dense(x)
        x = self.dense_out(x)
        return x
