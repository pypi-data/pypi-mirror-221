import tensorflow as tf

from openpy_fxts.layers.attention_class import _Luongs_concat_attention
from openpy_fxts.layers.attention_class import _Luongs_dot_attention
from openpy_fxts.layers.attention_class import _Luongs_general_attention
# import tensorflow.keras.backend as K


K = tf.keras.backend
# from tensorflow.keras.regularizers import L1L2

tfk = tf.keras
tkl = tf.keras.layers
tkm = tf.keras.models

feat_1 = 1  # index+1 where feature is ending
feat_2 = 2  # index+1 where feature is ending
feat_3 = 3  # index+1 where feature is ending
feat_4 = 4  # index+1 where feature is ending
# adding 0 at the front to help in the very first iteration while creating layers in a loop
feat_lst = [0, feat_1, feat_2, feat_3, feat_4]


# Experiment Nro. 1
# Without teacher forcing
# Define an input sequence and process it.
class lstm_hybrid_normal_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):

        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(features):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(1, dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input = data
        all_outputs = []
        for i in range(self.features):
            outputs = []
            enc_input = tf.expand_dims(encoder_input[:, :, i], 2)
            e_input = enc_input
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = final
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_hybrid_tf_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(len(feat_lst) - 1):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(feat_lst[i + 1] - feat_lst[i], dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        for i in range(len(feat_lst) - 1):
            outputs = []
            enc_input, d_input = encoder_input[:, :, feat_lst[i]:feat_lst[i + 1]], decoder_input[:, :,
                                                                                   feat_lst[i]:feat_lst[i + 1]]
            e_input = enc_input
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = tf.expand_dims(d_input[:, j, :], 1)
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_separate_tf_exp1(tkm.Model):
    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):

        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(features):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(1, dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        for i in range(self.features):
            outputs = []
            enc_input, d_input = tf.expand_dims(encoder_input[:, :, i], 2), tf.expand_dims(decoder_input[:, :, i], 2)
            e_input = enc_input
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = tf.expand_dims(d_input[:, j, :], 1)
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# without teacher forcing
# Define an input sequence and process it.
class lstm_separate_normal_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):

        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(features):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(1, dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)

        self.var = var

    def call(self, data):
        encoder_input = data
        all_outputs = []
        for i in range(self.features):
            outputs = []
            enc_input = tf.expand_dims(encoder_input[:, :, i], 2)
            e_input = enc_input
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = final
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# without teacher forcing
# Define an input sequence and process it.
class lstm_shared_normal_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_state=True, dtype='float64')
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        all_outputs = []
        _, hidden, cell = self.encoder(encoder_input)  # We discard `encoder_outputs` and only keep the states.
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            cur_vec = final
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# without teacher forcing
class lstm_luongs_dot_attention_shared_normal_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_dot_attention()
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(encoder_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = final
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_luongs_general_attention_shared_normal_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_general_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(encoder_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = final
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_luongs_concat_attention_shared_normal_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_concat_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(encoder_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = final
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_shared_tf_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_state=True, dtype='float64')
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        _, hidden, cell = self.encoder(encoder_input)  # We discard `encoder_outputs` and only keep the states.
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_luongs_general_attention_shared_tf_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_general_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(encoder_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            cur_vec = tf.cast(cur_vec, 'float64')
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_luongs_concat_attention_shared_tf_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_concat_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(encoder_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            cur_vec = tf.cast(cur_vec, 'float64')
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_luongs_dot_attention_shared_tf_exp1(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_dot_attention()
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(encoder_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            cur_vec = tf.cast(cur_vec, 'float64')
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# Experiment Nro. 2
class lstm_hybrid_normal_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(len(feat_lst) - 1):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(feat_lst[i + 1] - feat_lst[i], dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input = data
        all_outputs = []
        for i in range(len(feat_lst) - 1):
            outputs = []
            enc_input = encoder_input[:, :, feat_lst[i]:feat_lst[i + 1]]
            e_input = enc_input[:, :-1, :]
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = final
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_hybrid_tf_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(len(feat_lst) - 1):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(feat_lst[i + 1] - feat_lst[i], dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        for i in range(len(feat_lst) - 1):
            outputs = []
            enc_input = encoder_input[:, :, feat_lst[i]:feat_lst[i + 1]]
            d_input = decoder_input[:, :, feat_lst[i]:feat_lst[i + 1]]
            e_input = enc_input[:, :-1, :]
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = tf.expand_dims(d_input[:, j, :], 1)
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_separate_tf_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(features):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(1, dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        all_outputs = []
        for i in range(self.features):
            outputs = []
            enc_input, d_input = tf.expand_dims(encoder_input[:, :, i], 2), tf.expand_dims(decoder_input[:, :, i], 2)
            e_input = enc_input[:, :-1, :]
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = tf.expand_dims(d_input[:, j, :], 1)
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# without teacher forcing
# Define an input sequence and process it.
class lstm_separate_normal_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features
        var = []
        for i in range(features):
            lst = []
            encoder = tkl.LSTM(units, return_state=True, dtype='float64')
            decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
            dense = tkl.Dense(1, dtype='float64')
            lst.append(encoder)
            lst.append(decoder)
            lst.append(dense)
            var.append(lst)
        self.var = var

    def call(self, data):
        encoder_input = data
        all_outputs = []
        for i in range(self.features):
            outputs = []
            enc_input = tf.expand_dims(encoder_input[:, :, i], 2)
            e_input = enc_input[:, :-1, :]
            _, hidden, cell = self.var[i][0](e_input)  # We discard `encoder_outputs` and only keep the states.
            states = [hidden, cell]
            cur_vec = tf.expand_dims(enc_input[:, -1, :], 1)
            final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
            final = self.var[i][2](final)
            outputs.append(final)
            states = [hidden, cell]
            for j in range(self.decoder_outputs_length - 1):
                cur_vec = final
                final, hidden, cell = self.var[i][1](cur_vec, initial_state=states)
                final = self.var[i][2](final)
                outputs.append(final)
                states = [hidden, cell]
            outputs = tf.concat(outputs, axis=1)
            all_outputs.append(outputs)
        all_outputs = tf.concat(all_outputs, axis=2)
        return all_outputs


# without teacher forcing
# Define an input sequence and process it.
class lstm_shared_normal_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_state=True, dtype='float64')
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        _, hidden, cell = self.encoder(enc_input)  # We discard `encoder_outputs` and only keep the states.
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            cur_vec = final
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs

    # without teacher forcing


class lstm_luongs_dot_attention_shared_normal_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_dot_attention()
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(enc_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = final
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_luongs_general_attention_shared_normal_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_general_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(enc_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = final
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)

        return all_outputs


class lstm_luongs_concat_attention_shared_normal_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_concat_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(enc_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = final
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_shared_tf_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_state=True, dtype='float64')
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        _, hidden, cell = self.encoder(enc_input)  # We discard `encoder_outputs` and only keep the states.
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


class lstm_luongs_general_attention_shared_tf_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()

        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_general_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(enc_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            cur_vec = tf.cast(cur_vec, 'float64')
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_luongs_concat_attention_shared_tf_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_concat_attention(units=units)
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(enc_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            cur_vec = tf.cast(cur_vec, 'float64')
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_luongs_dot_attention_shared_tf_exp2(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.attention = _Luongs_dot_attention()
        self.decoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        enc_input = encoder_input[:, :-1, :]
        all_outputs = []
        encoder_output, hidden, cell = self.encoder(enc_input)
        context_vector, attention_weights = self.attention(hidden, encoder_output)
        states = [hidden, cell]
        cur_vec = tf.expand_dims(encoder_input[:, -1, :], 1)
        cur_vec = tf.cast(cur_vec, 'float64')
        context_vector = tf.expand_dims(context_vector, 1)
        cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
        final, hidden, cell = self.decoder(cur_vec, initial_state=states)
        final = self.dense(final)
        all_outputs.append(final)
        states = [hidden, cell]
        for i in range(self.decoder_outputs_length - 1):
            context_vector, attention_weights = self.attention(hidden, encoder_output)
            cur_vec = tf.expand_dims(decoder_input[:, i, :], 1)
            cur_vec = tf.cast(cur_vec, 'float64')
            context_vector = tf.expand_dims(context_vector, 1)
            cur_vec = tf.concat([context_vector, cur_vec], axis=-1)
            final, hidden, cell = self.decoder(cur_vec, initial_state=states)
            final = self.dense(final)
            all_outputs.append(final)
            states = [hidden, cell]
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# Define an input sequence and process it.
class lstm_normal_exp4(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.decoder = tkl.LSTM(units, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input = data
        encoder_input = tf.cast(encoder_input, dtype='float64')
        encoder_outputs, hidden, cell = self.encoder(encoder_input)
        states = [hidden, cell]
        all_outputs = []
        final = self.decoder(encoder_outputs, initial_state=states)
        final = self.dense(final)
        final = tf.expand_dims(final, axis=1)
        all_outputs.append(final)
        for i in range(self.decoder_outputs_length - 1):
            encoder_input = encoder_input[:, 1:, :]
            encoder_input = tf.concat([encoder_input, all_outputs[-1]], axis=1)
            encoder_outputs, hidden, cell = self.encoder(encoder_input)
            states = [hidden, cell]
            final = self.decoder(encoder_outputs, initial_state=states)
            final = self.dense(final)
            final = tf.expand_dims(final, axis=1)
            all_outputs.append(final)
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs


# teacher forcing
# Define an input sequence and process it.
class lstm_tf_exp4(tkm.Model):

    def __init__(self, encoder_inputs_length, decoder_outputs_length, features, units):
        super().__init__()
        self.encoder = tkl.LSTM(units, return_sequences=True, return_state=True, dtype='float64')
        self.decoder = tkl.LSTM(units, dtype='float64')
        self.dense = tkl.Dense(features, dtype='float64')
        self.decoder_outputs_length = decoder_outputs_length
        self.features = features

    def call(self, data):
        encoder_input, decoder_input = data[0], data[1]
        encoder_outputs, hidden, cell = self.encoder(encoder_input)
        states = [hidden, cell]
        all_outputs = []
        final = self.decoder(encoder_outputs, initial_state=states)
        final = self.dense(final)
        final = tf.expand_dims(final, axis=1)
        all_outputs.append(final)
        for i in range(self.decoder_outputs_length - 1):
            encoder_input = encoder_input[:, 1:, :]
            encoder_input = tf.concat([encoder_input, decoder_input[:, i:i + 1, :]], axis=1)
            encoder_outputs, hidden, cell = self.encoder(encoder_input)
            states = [hidden, cell]
            final = self.decoder(encoder_outputs, initial_state=states)
            final = self.dense(final)
            final = tf.expand_dims(final, axis=1)
            all_outputs.append(final)
        all_outputs = tf.concat(all_outputs, axis=1)
        return all_outputs

