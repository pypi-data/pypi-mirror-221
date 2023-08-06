__version__ = '0.1.4'

# Simple models
# Model Multi Layer Perceptron
from openpy_fxts.mdls_to_fx.simple.dlm_MLP import MLP_Dense_class
# Model Recurrent Neural Networks (RNN)
from openpy_fxts.mdls_to_fx.simple.dlm_RNN import RNN_Dense_class, Multi_RNN_Dense_class
from openpy_fxts.mdls_to_fx.simple.dlm_RNN import BiRNN_Dense_class, Multi_BiRNN_Dense_class
# Models: Conv1D
from openpy_fxts.mdls_to_fx.simple.dlm_Conv1D import Conv1D_Dense_class, Multi_Conv1D_Dense_class
# Hybrids models
from openpy_fxts.mdls_to_fx.hybrids.dlm_Conv1D import TimeDist_Conv1D_RNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Conv1D import Conv1D_RNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Conv1D import Conv1D_BiRNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Conv1D import Conv1D_BiRNN_Attention_class  # New
# Models: BiRNN
from openpy_fxts.mdls_to_fx.hybrids.dlm_BiRNN import BiRNN_TimeDist_Dense_class
from openpy_fxts.mdls_to_fx.hybrids.dlm_BiRNN import BiRNN_Conv1D_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_BiRNN import BiRNN_Bahdanau_Attention_Conv1D_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_BiRNN import BiRNN_MultiHeadAttention_Conv1D_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_BiRNN import BiRNN_Luong_Attention_Conv1D_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_BiRNN import BiRNN_MDN  # Review
# Model: Others with BiRNN
from openpy_fxts.mdls_to_fx.hybrids.dlm_Others import TCN_BiRNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Others import Time2Vec_BiRNN_class  # New
# Model: Encoder Decoder
from openpy_fxts.mdls_to_fx.hybrids.dlm_EncDec import EncDec_RNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_EncDec import EncDec_BiRNN_class
from openpy_fxts.mdls_to_fx.hybrids.dlm_EncDec import EncDec_Conv1D_BiRNN_class
# Models: Seq2Seq
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_RNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_RNN2_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_BiRNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_BiRNN2_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_RNN_Batch_Drop_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_Conv1D_BiRNN_class  # New
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_Multi_Head_Conv1D_BiRNN_class  # New -> Function
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_RNN_with_Luong_Attention_class  # New -> Function
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_BiRNN_with_Attention_class  # New -> Function
from openpy_fxts.mdls_to_fx.hybrids.dlm_Seq2Seq import Seq2Seq_Conv2D_RNN_class
# Models: Stacked
from openpy_fxts.mdls_to_fx.hybrids.dlm_Stacked import RNN_Stacked, Stacked_SciNet
# BBDD test
from openpy_fxts.preprocessing.examples_data import hpc_dataframe
from openpy_fxts.mdls_to_fx.utils import _date_init_final
