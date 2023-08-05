# -*- coding: utf-8 -*-
# @Time    : 14/07/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ------------
# @Software: PyCharm

from openpy_fxts.baseline_mdl import base_class


class RNN_Dense_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='RNN_Dense',
            type_mdl='RNN',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class Multi_RNN_Dense_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Multi_RNN_Dense',
            type_mdl='RNN',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class BiRNN_Dense_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='BiRNN_Dense',
            type_mdl='BiRNN',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class Multi_BiRNN_Dense_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Multi_BiRNN_Dense',
            type_mdl='BiRNN',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return
