import tensorflow as tf

from openpy_fxts.mdls_to_fx.get_arch_mdl import _get_architecture
from openpy_fxts.preprocessing.prepare_data import pre_processing_data
from openpy_fxts.mdls_to_fx.utils import _mdl_characteristics
from openpy_fxts.mdls_to_fx.utils import _callbacks
from openpy_fxts.mdls_to_fx.utils import _learning_curve
from openpy_fxts.mdls_to_fx.utils import _process_values_preliminary

tkm = tf.keras.models
tkl = tf.keras.layers
tkloss = tf.keras.losses
tko = tf.keras.optimizers
tku = tf.keras.utils


class base_model:

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl=None,
            type_mdl=None
    ):
        # Parameters for dataset
        self.config_data = config_data
        self.n_past = config_data['n_past']
        self.n_future = config_data['n_future']
        self.n_inp_ft = config_data['n_inp_ft']
        self.n_out_ft = config_data['n_out_ft']
        # Parameters for model
        self.config_mdl = config_mdl
        self.optimizer = config_mdl['optimizer']
        self.loss = config_mdl['loss']
        self.metrics = config_mdl['metrics']
        self.batch_size = config_mdl['batch_size']  # Batch size for training.
        self.epochs = config_mdl['epochs']  # Number of epochs to train for.
        # Parameters for simulation
        self.config_sim = config_sim
        self.verbose = config_sim['verbose']
        self.patience = config_sim['patience']
        self.plot_history = config_sim['plt_history']
        self.preliminary = config_sim['preliminary']
        self.config_arch = config_arch
        self.name_mdl = name_mdl
        self.type_mdl = type_mdl

    def _architecture_model(self):
        get_arch = _get_architecture(
            name_mdl=self.name_mdl,
            type_mdl=self.type_mdl,
            n_past=self.n_past,
            n_future=self.n_future,
            n_inp_ft=self.n_inp_ft,
            n_out_ft=self.n_out_ft,
            config_arch=self.config_arch
        )
        model = get_arch.select_model()
        return model

    def reshape_train_valid(self, pre_processed):
        # Training
        X_train = pre_processed['train']['X']
        y_train = pre_processed['train']['y']
        # Validation
        X_valid = pre_processed['valid']['X']
        y_valid = pre_processed['valid']['y']
        if self.type_mdl == 'MLP':
            if self.name_mdl == 'MLP_Dense':
                X_train_list, X_valid_list = [], []
                for i in range(X_train.shape[2]):
                    X_train_list.append(X_train[:, :, i])
                    X_valid_list.append(X_valid[:, :, i])

                '''
                y_train_list, y_valid_list = [], []
                for j in range(y_train.shape[2]):
                    y_train_list.append(y_train[:, :, j])
                    y_valid_list.append(y_valid[:, :, j])
                '''

                return X_train_list, y_train, X_valid_list, y_valid
            if self.name_mdl == 'MLP_RNN':
                X_train_list, X_valid_list = [], []
                for i in range(X_train.shape[2]):
                    X_train_list.append(X_train[:, :, i])
                    X_valid_list.append(X_valid[:, :, i])
                return X_train_list, X_valid_list, X_valid, y_valid
        if self.type_mdl == 'Conv1D':
            if self.name_mdl == 'TimeDist_Conv1D_RNN':
                X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
                X_valid = X_valid.reshape(X_valid.shape[0], X_valid.shape[1], X_valid.shape[2], 1)
                return X_train, y_train, X_valid, y_valid
            else:
                return X_train, y_train, X_valid, y_valid
        else:
            return X_train, y_train, X_valid, y_valid

    def _training_mdl(self, filepath):
        base = base_model(
            self.config_data, self.config_mdl, self.config_sim, self.config_arch, self.name_mdl, self.type_mdl
        )
        pre_processed = pre_processing_data(
            self.config_data,
            train=True,
            valid=True
        ).transformer_data(dropnan=True)
        model = base._architecture_model()
        print(self.name_mdl)
        model.compile(
            optimizer=self.optimizer,
            loss=self.loss,
            metrics=self.metrics
        )
        _mdl_characteristics(model, self.config_sim, filepath)
        X_train, y_train, X_valid, y_valid = base.reshape_train_valid(pre_processed)
        history = model.fit(
            x=X_train,
            y=y_train,
            validation_data=(
                X_valid,
                y_valid
            ),
            batch_size=self.batch_size,
            epochs=self.epochs,
            verbose=self.verbose,
            callbacks=_callbacks(
                filepath,
                weights=True,
                verbose=self.verbose,
                patience=self.patience
            )
        )
        if self.plot_history:
            _learning_curve(history, self.name_mdl, filepath, self.config_sim['time_init'])
        if self.preliminary:
            self.config_data['pct_valid'] = None
            return _process_values_preliminary(
                model,
                pre_processing_data(
                    self.config_data,
                    train=True, valid=True
                ).transformer_data(dropnan=False),
                self.config_data,
                self.config_sim,
                self.name_mdl,
                self.type_mdl
            ).get_values(filepath)
        else:
            return None

    def _prediction_model(self, model_train, filepath):
        return _process_values_preliminary(
            model_train,
            pre_processing_data(
                self.config_data,
                test=True
            ).transformer_data(dropnan=True),
            self.config_data,
            self.config_sim,
            self.name_mdl,
            self.type_mdl
        ).get_values(filepath)


class base_class(base_model):

    def __init__(
            self,
            config_data=None,
            config_mdl=None,
            config_sim=None,
            config_arch=None,
            name_mdl=None,
            type_mdl=None,
    ):
        super().__init__(config_data, config_mdl, config_sim, config_arch, name_mdl, type_mdl)

    def build_mdl(self):
        mdl = base_class(
            self.config_data, self.config_mdl, self.config_sim, self.config_arch, self.name_mdl, self.type_mdl
        )
        return mdl._architecture_model()

    def train_mdl(self, filepath: str = None):
        mdl = base_class(
            self.config_data, self.config_mdl, self.config_sim, self.config_arch, self.name_mdl, self.type_mdl
        )
        return mdl._training_mdl(filepath)

    def prediction_mdl(self, model, filepath: str = None):
        mdl = base_class(
            self.config_data, self.config_mdl, self.config_sim, self.config_arch, self.name_mdl, self.type_mdl
        )
        return mdl._prediction_model(model, filepath)

    def _change_name(self, name):
        self.name_mdl = name
        return
