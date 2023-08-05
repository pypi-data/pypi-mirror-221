from openpy_fxts.baseline_mdl import base_class


class Conv1D_Dense_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Conv1D_Dense',
            type_mdl='Conv1D',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return


class Multi_Conv1D_Dense_class(base_class):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl='Multi_Conv1D_Dense',
            type_mdl='Conv1D',
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)
        return