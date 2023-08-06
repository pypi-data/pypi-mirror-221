import numpy as np
import pandas as pd


def get_histogram(df_in, col: str, binsize=None, density: bool = False, groupby: str = 'Group', discrete: bool = False):
    if discrete:
        df_out = (df_in
                  .groupby(groupby, sort=False)
                  [col]
                  .value_counts(normalize=density, sort=False)
                  .reset_index()
                  )
    else:
        bins = np.arange(df_in[col].min(), df_in[col].max()+2*binsize, binsize)
        df_out = (pd.concat([pd.cut(df_in[col], bins,
                                    labels=bins[1:]-binsize/2,
                                    include_lowest=True, right=False),
                             df_in[groupby]], axis=1)
                  .astype({col: 'float64'})
                  .groupby(groupby, sort=False, observed=True)
                  [col]
                  .value_counts(normalize=density, sort=False)
                  .reset_index()
                  )
    return df_out


def order_categories(df, col: str, order: list):
    df = (df.assign(tmp_col=lambda df:
                    df[col]
                    .astype('category')
                    .cat.reorder_categories(order, ordered=True))
            .drop(columns=col)
            .rename(columns={'tmp_col': col})
            .sort_values(by=col)
          )
    return df
