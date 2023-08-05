from kpi.miss_sales_kpi.miss_sales_kpi_metric import MissSalesKPI
from kpi.stock_kpi.stock_kpi_metric import StockKPI
from kpi.config import date_col, sku_col, store_col, sales_col, price_col, stock_col
import pandas as pd


def main(our_data: dict, enemy_data: dict, stock_df: pd.DataFrame, prices: dict, quantity: dict, year1: int = 2022,
         year2: int = 2023) -> dict:
    miss_sales_kpi = MissSalesKPI(date_col, sku_col, store_col, sales_col,
                                  price_col, stock_col)
    stock_kpi = StockKPI(sales_col, sku_col, stock_col, date_col, store_col)
    kpi_dict = {}

    kpi_dict["miss_sales"] = {}
    kpi_dict["miss_sales"]["year_comparison"] = miss_sales_kpi.calculate_first_kpi(our_data, enemy_data, prices, quantity,
                                                                             year1, year2)
    kpi_dict["miss_sales"]["quarter_comparison"] = miss_sales_kpi.calculate_second_kpi(our_data, enemy_data, prices,
                                                                                   quantity, year1, year2)
    kpi_dict["miss_sales"]["month_comparison"] = miss_sales_kpi.calculate_third_kpi(our_data, enemy_data, prices, quantity,
                                                                               year1, year2)

    kpi_dict["stock"] = {}
    kpi_dict["stock"]["year_comparison"] = stock_kpi.compare_years(stock_df, prices, year1, year2)
    kpi_dict["stock"]["quarter_comparison"] = stock_kpi.compare_quarters(stock_df, prices, year1, year2)
    kpi_dict["stock"]["month_comparison"] = stock_kpi.compare_months(stock_df, prices, year1, year2)
    return kpi_dict
