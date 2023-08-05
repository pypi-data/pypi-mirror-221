from utils.kpi_and_metrics import MissSalesKPI, StockKPI
import pytest
import pandas as pd
import numpy as np


def simulate_data(num_entries=5000):
    """
    This function generates a simulated dataset with the following columns:
    'date', 'sku', 'store', 'sales', 'price', 'stock'.

    Args:
        num_entries (int, optional): The number of rows to generate for the dataset. Defaults to 5000.

    Returns:
        df_sales (pd.DataFrame): A DataFrame with the simulated sales and stock data.
        prices (dict): A dictionary with simulated prices for each SKU.
        quantity (dict): A dictionary with simulated quantities for each SKU.
    """
    date_range = pd.date_range(start='2022-01-01', end='2023-12-31')
    sku_list = [f'sku_{i}' for i in range(1, 11)]
    store_list = [f'store_{i}' for i in range(1, 11)]
    price_list = np.random.uniform(1, 100, size=len(sku_list))

    dates = np.random.choice(date_range, size=num_entries)
    skus = np.random.choice(sku_list, size=num_entries)
    stores = np.random.choice(store_list, size=num_entries)
    sales = np.random.randint(0, 100, size=num_entries)
    stock = np.random.randint(0, 200, size=num_entries)

    df_sales = pd.DataFrame({
        'date': dates,
        'sku': skus,
        'store': stores,
        'sales': sales,
        'price': price_list[0],  # assuming same price for all SKUs in df
        'stock': stock
    })

    prices = {sku: price for sku, price in zip(sku_list, price_list)}
    quantity = df_sales.groupby('sku')['sales'].mean().to_dict()

    return df_sales, prices, quantity


def test_MissSalesKPI_calc_A():
    df_sales, df_stock, prices, quantity = simulate_data()
    miss_sales_kpi = MissSalesKPI()
    result = miss_sales_kpi.calc_A(df_sales)
    assert isinstance(result, float)

def test_MissSalesKPI_calc_B():
    df_sales, df_stock, prices, quantity = simulate_data()
    miss_sales_kpi = MissSalesKPI()
    result = miss_sales_kpi.calc_B(df_stock, prices, threshold=14)
    assert isinstance(result, float)

def test_StockKPI_calc_G():
    df_sales, df_stock, prices, quantity = simulate_data()
    stock_kpi = StockKPI()
    result = stock_kpi.calc_G(df_sales)
    assert isinstance(result, float)

