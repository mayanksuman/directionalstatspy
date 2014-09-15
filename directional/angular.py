import numpy as np 
import pandas as pd 


###########################
# PANDAS MATRIX CONVERSIONS
###########################


def col_names_from_sin_cos_matrix(df):
  half_columns = list(df.columns)[:int(len(df.columns) / 2)]
  return [col[:-5] for col in half_columns]


def sin_cos_matrix_to_radian_matrix(sin_cos_matrix):
  radian_matrix = pd.DataFrame(index = sin_cos_matrix.index)
  for col in col_names_from_sin_cos_matrix(sin_cos_matrix):
    radian_matrix[col] = np.arctan2(sin_cos_matrix[col + "--SIN"].values, sin_cos_matrix[col + "--COS"].values)
  return radian_matrix


def radian_matrix_to_sin_cos_matrix(radian_matrix):
  sin_matrix = radian_matrix.apply(np.sin)
  sin_matrix.columns = map(lambda x : x + "--SIN", radian_matrix.columns)
  cos_matrix = radian_matrix.apply(np.cos)
  cos_matrix.columns = map(lambda x : x + "--COS", radian_matrix.columns)
  return pd.concat([sin_matrix, cos_matrix], axis=1, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=True)


def sin_cos_matrix_to_degrees_matrix(sin_cos_matrix):
  return sin_cos_matrix_to_radian_matrix(sin_cos_matrix).applymap(np.degrees)


def sin_cos_matrix_std(sin_cos_matrix):
  mean = sin_cos_pair_mean(sin_cos_matrix)
  result = pd.Series(index = sin_cos_matrix.index)
  for name in col_names_from_sin_cos_matrix(sin_cos_matrix):
    pass


def sin_cos_matrix_mean(sin_cos_matrix):
  return sin_cos_matrix.mean()


