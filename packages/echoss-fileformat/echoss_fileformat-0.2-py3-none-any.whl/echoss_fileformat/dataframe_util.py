import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


def print_table(df: pd.DataFrame, method, index=False, max_cols=20, max_rows=10, col_space=16, max_colwidth=24):
    method(table_to_string(df, index=index, max_cols=max_cols, max_rows=max_rows, col_space=col_space, max_colwidth=max_colwidth))


def table_to_string(df: pd.DataFrame, index=False, max_cols=20, max_rows=5, col_space=16, max_colwidth=24):
    """

    Args:
        df:

    Returns:

    """
    return '\n'+df.to_string(index=index, index_names=index, max_cols=max_cols, max_rows=max_rows, justify='left',
                             show_dimensions=True, col_space=col_space, max_colwidth=max_colwidth)+'\n'


def reduce_memory_usage(df: pd.DataFrame,
                        index_cols: list =None,
                        use_cols: list = None,
                        category_cols: list = None,
                        str_cols: list = None,
                        numeric_cols: list = None,
                        numeric_fillna = 0,
                        date_cols: list = None,
                        date_formats: list = None
                        ) -> pd.DataFrame:
    """
    :param df: dataframe
    :param category_cols: category 타입으로 변경
    :param str_cols: 문자열 타입 컬럼
    :param numeric_cols: 숫자형 타입 컬럼
    :return:
    """
    start_mem = df.memory_usage().sum() / 1024 ** 2 # MB
    logger.info(('Memory usage of dataframe is {:.2f} MB').format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype
        col_name = df[col].name

        try:
            if date_cols is not None and col_name in date_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            elif category_cols is not None and col_name in category_cols:
                df[col] = df[col].astype('category')
            elif numeric_cols is not None and col_name in numeric_cols:
                if col_type == object: # mixed one?
                    df[col] = pd.to_numeric(df[col],errors='coerce' ).fillna(numeric_fillna)
                c_min = df[col].min()
                c_max = df[col].max()
                if str(col_type)[:3] == 'int':
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)
                    else:
                        df[col] = df[col].astype(np.int64)
                else:
                    if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        df[col] = df[col].astype(np.float32)
                    else:
                        df[col] = df[col].astype(np.float64)
            elif str_cols is not None and col_name in str_cols:
                df[col] = df[col].astype('str')
            else:
                logger.error(f"unsupported column {col_name} exist as type {col_type}")
        except Exception as e:
            logger.error(f"Error on dataframe astype convert [{col_name}:{col_type}] by [{e}]")

    if index_cols is not None:
        df = df.set_index(index_cols)

    if use_cols is not None:
        df = df[use_cols]

    end_mem = df.memory_usage().sum() / 1024 ** 2
    logger.info(('Memory usage after optimization is: {:.2f} MB decreased by {:.1f}%')
          .format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df