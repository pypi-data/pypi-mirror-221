from openpy_fxts.baseline_mdl import base_class


class TCN_BiRNN_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='TCN_BiLSTM',
            type_mdl='Others',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class Time2Vec_BiRNN_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Time2Vec_BiRNN',
            type_mdl='Others',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


