# -*- coding: utf-8 -*-
# @Time    : 14/07/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fxts.baseline_mdl import base_class


class TimeDist_Conv1D_RNN_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='TimeDist_Conv1D_RNN',
            type_mdl='Conv1D',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return

class Conv1D_RNN_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Conv1D_RNN',
            type_mdl='Conv1D',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class Conv1D_BiRNN_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Conv1D_BiRNN',
            type_mdl='Conv1D',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class Conv1D_BiRNN_Attention_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Conv1D_BiRNN_Attention',
            type_mdl='Conv1D',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return

