# -*- coding: utf-8 -*-
# @Time    : 14/07/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fxts.base_tf import tkm, tkl, tkr
from openpy_fxts.layers.layers_class import type_rnn, dense_multi_out
from openpy_fxts.layers.layers_class import multi_conv1d_pool_flat_drop, multi_rnn_drop
from openpy_fxts.layers.layers_class import dense_reshape_conv1d_multi_out
from openpy_fxts.layers.layers_class import multi_birnn_attention_conv1d, multi_birnn_multihead_attention_conv1d
from openpy_fxts.mdls_to_fx.get_arch_dicts import _get_config_birnn_others


class birnn_conv1d_dense(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(birnn_conv1d_dense, self).__init__()
        if config is None:
            config = _get_config_birnn_others('birnn_conv1d_dense')
        self.n_future = n_future,
        self.n_out_ft = n_out_ft,
        self.config = config
        self.multi_hidden_birnn = multi_rnn_drop(
            mdl=type_rnn(config['rnn_layers']['type']),
            units=config['rnn_layers']['units'],
            activations=config['rnn_layers']['activations'],
            sequences=config['rnn_layers']['sequences'],
            is_drop=config['dropout']['activate'],
            rate=config['dropout']['rate'],
            bidirectional=True
        )
        self.multi_hidden_conv1d = multi_conv1d_pool_flat_drop(
            filters=config['conv1d_layers']['filters'],
            kernels=config['conv1d_layers']['kernels'],
            activations=config['conv1d_layers']['activations'],
            paddings=config['conv1d_layers']['paddings'],
            is_drop=config['dropout']['activate'],
            rate=config['dropout']['rate'],
            maxpooling_1d=True,
            pool_global=True,
            pool_size=config['conv1d_layers']['pool_size'],
            flatten=True)
        if config['dropout']['activate']:
            self.dropout = tkl.Dropout(rate=config['dropout']['rate'])
        self.dense_conv1d_out = dense_reshape_conv1d_multi_out(
            n_future,
            n_out_ft,
            config['output_layer']['activation'],
            'same'
        )

    def call(self, inputs, training=True, **kwargs):
        x = self.multi_hidden_birnn(inputs)
        x = self.multi_hidden_conv1d(x)
        if self.config['dropout']['activate']:
            x = self.dropout(x)
        x = self.dense_conv1d_out(x)
        return x


class birnn_bahdanau_attention_conv1d_dense(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(birnn_bahdanau_attention_conv1d_dense, self).__init__()
        if config is None:
            config = _get_config_birnn_others('birnn_bahdanau_attention_conv1d_dense')
        self.config = config
        self.multi_hidden_layers = multi_birnn_attention_conv1d(
            mdl=type_rnn(config['rnn_layers']['type']),
            bidirectional=True,
            units=config['rnn_layers']['units'],
            rnn_act=config['rnn_layers']['activations'],
            return_seq=config['rnn_layers']['sequences'],
            att_type='Bahdanau',
            kernel_reg=config['attention']['kernel_reg'],
            bias_reg=config['attention']['bias_reg'],
            reg_weight=config['attention']['reg_weight'],
            n_filters=config['conv1d_layers']['filters'],
            kernels=config['conv1d_layers']['kernels'],
            conv_act=config['conv1d_layers']['activations'],
            paddings=config['conv1d_layers']['paddings'],
            simple_pool=True,
            global_pool=False,
            pool_size=config['conv1d_layers']['pool_size']
        )
        self.flatten = tkl.Flatten()
        if config['dropout']['activate']:
            self.dropout = tkl.Dropout(config['dropout']['rate'])
        self.dense_out = dense_multi_out(
            n_future,
            n_out_ft,
            config['output_layer']['activation']
        )

    def call(self, inputs, training=True, **kwargs):
        x = self.multi_hidden_layers(inputs)
        x = self.flatten(x)
        if self.config['dropout']['activate']:
            x = self.dropout(x)
        x = self.dense_out(x)
        return x


class birnn_luong_attention_conv1d_dense(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(birnn_luong_attention_conv1d_dense, self).__init__()
        if config is None:
            config = _get_config_birnn_others('birnn_luong_attention_conv1d_dense')
        self.config = config
        self.multi_hidden_layers = multi_birnn_attention_conv1d(
            mdl=type_rnn(config['rnn_layers']['type']),
            bidirectional=True,
            units=config['rnn_layers']['units'],
            rnn_act=config['rnn_layers']['activations'],
            return_seq=config['rnn_layers']['sequences'],
            att_type='Luong',
            kernel_reg=config['attention']['kernel_reg'],
            bias_reg=config['attention']['bias_reg'],
            reg_weight=config['attention']['reg_weight'],
            n_filters=config['conv1d_layers']['filters'],
            kernels=config['conv1d_layers']['kernels'],
            conv_act=config['conv1d_layers']['activations'],
            paddings=config['conv1d_layers']['paddings'],
            simple_pool=True,
            global_pool=False,
            pool_size=config['conv1d_layers']['pool_size']
        )
        self.flatten = tkl.Flatten()
        if config['dropout']['activate']:
            self.dropout = tkl.Dropout(config['dropout']['rate'])
        self.dense_out = dense_multi_out(
            n_future,
            n_out_ft,
            config['output_layer']['activation']
        )

    def call(self, inputs, training=True, **kwargs):
        x = self.multi_hidden_layers(inputs)
        x = self.flatten(x)
        if self.config['dropout']['activate']:
            x = self.dropout(x)
        x = self.dense_out(x)
        return x


class birnn_multihead_attention_conv1d_dense(tkm.Model):

    def __init__(
            self,
            n_future=None,
            n_out_ft=None,
            config=None
    ):
        super(birnn_multihead_attention_conv1d_dense, self).__init__()
        if config is None:
            config = _get_config_birnn_others('birnn_multihead_attention_conv1d_dense')
        self.config = config
        self.multi_hidden_layers = multi_birnn_multihead_attention_conv1d(
            mdl=type_rnn(config['rnn_layers']['type']),
            bidirectional=True,
            units=config['rnn_layers']['units'],
            rnn_act=config['rnn_layers']['activations'],
            return_seq=config['rnn_layers']['sequences'],
            att_type='MultiHeadAttention',
            num_heads=config['attention']['num_heads'],
            key_dim=config['attention']['key_dim'],
            dropout=config['attention']['dropout'],
            n_filters=config['conv1d_layers']['filters'],
            kernels=config['conv1d_layers']['kernels'],
            conv_act=config['conv1d_layers']['activations'],
            paddings=config['conv1d_layers']['paddings'],
            simple_pool=True,
            global_pool=False,
            pool_size=config['conv1d_layers']['pool_size']
        )
        self.flatten = tkl.Flatten()
        if config['dropout']['activate']:
            self.dropout = tkl.Dropout(config['dropout']['rate'])
        self.dense_out = dense_multi_out(
            n_future,
            n_out_ft,
            config['output_layer']['activation']
        )

    def call(self, inputs, training=True, **kwargs):
        x = self.multi_hidden_layers(inputs)
        x = self.flatten(x)
        if self.config['dropout']['activate']:
            x = self.dropout(x)
        x = self.dense_out(x)
        return x