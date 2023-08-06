# -*- coding: utf-8 -*-
# @Time    : 14/07/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm


def _get_config_mlp(name_mdl):
    if name_mdl == 'mlp_dense':
        return {
            'input_layer': {
                'units': 128,
                'activation': None
            },
            'dense_layers': {
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu']
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'output_layer': {
                'activation': None
            }
        }


def _get_config_rnn(name_mdl):
    if name_mdl == 'rnn_dense':
        return {
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, False]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'dense_layer': {
                'activate': True,
                'units': 128,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'multi_rnn_dense':
        return {
            'multi_rnn_layers': {
                'type': 'LSTM',
                'units': [64, 64],
                'activations': ['relu', 'relu'],
                'sequences': [True, False]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'rnn_layer': {
                'units': 64,
                'activation': 'relu',
                'sequences': False
            },
            'dense_layer': {
                'activate': False,
                'units': 64,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'birnn_dense':
        return {
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, False]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'dense_layer': {
                'activate': True,
                'units': 128,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'multi_birnn_dense':
        return {
            'multi_rnn_layers': {
                'type': 'LSTM',
                'units': [32, 32],
                'activations': ['relu', 'relu'],
                'sequences': [True, False]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'rnn_layer': {
                'units': 32,
                'activation': 'relu',
                'sequences': False
            },
            'dense_layer': {
                'activate': False,
                'units': 32,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'birnn_timedist_dense':
        return {
            'rnn_layer': {
                'type': 'LSTM',
                'units': 256,
                'activations': 'relu',
                'sequences': True
            },
            'timedist_dense_layers': {
                'units': [64, 32],
                'activations': ['relu', 'relu']
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'dense_layer': {
                'units': 64,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }


def _get_config_conv1d_others(name_mdl):
    if name_mdl == 'timedist_conv1d_rnn_dense':
        return {
            'conv1d_layers': {
                'filters': [32, 32, 32],
                'kernels': [11, 9, 3],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'maxpooling': True,
                'pool_size': 2

            },
            'rnn_layer': {
                'type': 'LSTM',
                'units': 256,
                'activation': 'relu',
                'sequences': False
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'pool_size': 2,
            'dense_layer': {
                'units': 128,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'conv1d_dense':
        return {
            'conv1d_layers': {
                'filters': [32, 32, 32],
                'kernels': [11, 9, 3],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal']
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'pool_size': 2,
            'dense_layer': {
                'activate': False,
                'units': 32,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'multi_conv1D_dense':
        return {
            'conv1d_layers': {
                'filters': [32, 32, 32],
                'kernels': [11, 9, 3],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal']
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'pool_size': 2,
            'dense_layer': {
                'activate': False,
                'units': 32,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'conv1d_rnn_dense':
        return {
            'conv1d_layers': {
                'filters': [32, 32, 32],
                'kernels': [11, 9, 3],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 2
            },
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, False]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'pool_size': 2,
            'dense_layer': {
                'activate': False,
                'units': 32,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'conv1d_birnn_dense':
        return {
            'conv1d_layers': {
                'filters': [32, 32, 32],
                'kernels': [11, 9, 3],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 2
            },
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, False]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'dense_layer': {
                'activate': True,
                'units': 32,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'conv1d_birnn_attention_dense':
        return {
            'conv1d_layers': {
                'filters': [32, 32, 32],
                'kernels': [11, 9, 3],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 2
            },
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, True]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'dense_layer': {
                'activate': False,
                'units': 32,
                'activation': 'relu'
            },
            'output_layer': {
                'activation': None
            }
        }


def _get_config_birnn_others(name_mdl):
    if name_mdl == 'birnn_conv1d_dense':
        return {
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, True]
            },
            'conv1d_layers': {
                'filters': [128, 64, 32],
                'kernels': [11, 9, 2],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 1
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'birnn_bahdanau_attention_conv1d_dense':
        return {
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, True]
            },
            'attention': {
                'kernel_reg': 1e-4,
                'bias_reg': 1e-4,
                'reg_weight': 1e-4,
            },
            'conv1d_layers': {
                'filters': [128, 64, 32],
                'kernels': [11, 9, 2],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 1
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'birnn_luong_attention_conv1d_dense':
        return {
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, True]
            },
            'attention': {
                'kernel_reg': 1e-4,
                'bias_reg': 1e-4,
                'reg_weight': 1e-4,
            },
            'conv1d_layers': {
                'filters': [128, 64, 32],
                'kernels': [11, 9, 2],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 1
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'birnn_multihead_attention_conv1d_dense':
        return {
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, True]
            },
            'attention': {
                'num_heads': 2,
                'key_dim': 2,
                'dropout': 0.1
            },
            'conv1d_layers': {
                'filters': [128, 64, 32],
                'kernels': [11, 9, 2],
                'activations': ['relu', 'relu', 'relu'],
                'paddings': ['causal', 'causal', 'causal'],
                'pool_size': 1
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'output_layer': {
                'activation': None
            }
        }
    if name_mdl == 'time2vec_bilstm':
        return {
            'time2vec': {
                'units': [128]
            },
            'rnn_layers': {
                'type': 'LSTM',
                'units': [128, 128, 128],
                'activations': ['relu', 'relu', 'relu'],
                'sequences': [True, True, True]
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
            'output_layer': {
                'activation': None
            }
        }


def _get_config_encdec(name_mdl):
    if name_mdl == 'encdec_rnn':
        return {
            'encoder': {
                'rnn_layers': {
                    'type': 'LSTM',
                    'units': [64, 64, 64],
                    'activations': ['relu', 'relu', 'relu'],
                    'sequences': [True, True, False]
                }
            },
            'decoder': {
                'rnn_layers': {
                    'type': 'LSTM',
                    'units': [64, 64, 64],
                    'activations': ['relu', 'relu', 'relu'],
                    'sequences': [True, True, True]
                }
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
        }
    if name_mdl == 'encdec_birnn':
        return {
            'encoder': {
                'rnn_layers': {
                    'type': 'LSTM',
                    'units': [64, 64, 64],
                    'activations': ['relu', 'relu', 'relu'],
                    'sequences': [True, True, False]
                }
            },
            'decoder': {
                'rnn_layers': {
                    'type': 'LSTM',
                    'units': [64, 64, 64],
                    'activations': ['relu', 'relu', 'relu'],
                    'sequences': [True, True, True]
                }
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
        }
    if name_mdl == 'encdec_conv1d_birnn':
        return {
            'encoder': {
                'conv1d_layers': {
                    'filters': [128, 64, 32],
                    'kernels': [11, 9, 3],
                    'activations': ['relu', 'relu', 'relu'],
                    'paddings': ['causal', 'causal', 'causal'],
                    'pool_size': 2
                },
            },
            'decoder': {
                'rnn_layers': {
                    'type': 'LSTM',
                    'units': [32, 32, 32],
                    'activations': ['relu', 'relu', 'relu'],
                    'sequences': [True, True, True]
                }
            },
            'dropout': {
                'activate': True,
                'rate': 0.3
            },
        }