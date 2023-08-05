import numpy as np
import pandas as pd
from kpi.config import date_col, sku_col, store_col, sales_col, price_col, stock_col
def get_cumulative_stock_including_delivery(start_date: str, end_date: str, df_stock: pd.DataFrame,
                                            df_delivery: pd.DataFrame) -> dict:
    """
    This function calculates the cumulative stock including the delivery for each sku and store in the given date range.
    and returns a dictionary with the sku, store as keys and the cumulative stock as values.
    Args:
        start_date:
        end_date:
        df_stock:
        df_delivery:

    Returns:

    """
    x_o = df_stock[(df_stock['valid_from_date'] <= start_date) & (df_stock['valid_to_date'] >= start_date)]
    df_delivery_filter = df_delivery[
        (df_delivery['delivery_date'] >= start_date) & (df_delivery['delivery_date'] <= end_date)]
    df_delivery_filter = df_delivery_filter.groupby(['sku', 'store']).agg({'total_delivered_quantity': 'sum'}).to_dict(
        "index")
    dict_x0_sku_stock_store = {(sku, store): stock for sku, store, stock in zip(x_o['sku'], x_o['store'], x_o['stock'])}
    final_dict = {}
    for (sku, store), stock in dict_x0_sku_stock_store.items():
        if (sku, store) in df_delivery_filter:
            final_dict[(sku, store)] = stock + df_delivery_filter[(sku, store)]['total_delivered_quantity']
        else:
            final_dict[(sku, store)] = stock
    return final_dict

def mean_over_months(func,df, year):
    """
    This function calculates the mean of a function over a given quarter and year.
    Args:
        func: function to be applied
        df: dataframe
        year: year
        quarter: quarter

    Returns: mean of the function

    """
    return np.mean([func(df, year, month) for month in np.unique(df[date_col].dt.month)])


