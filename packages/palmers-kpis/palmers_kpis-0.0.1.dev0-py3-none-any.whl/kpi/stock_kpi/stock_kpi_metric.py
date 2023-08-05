import pandas as pd
import numpy as np
from kpi.utils import mean_over_months


class StockKPI:
    def __init__(self, sales_col, sku_col, stock_col, date_col, store_col):
        self.sales_col = sales_col
        self.sku_col = sku_col
        self.stock_col = stock_col
        self.date_col = date_col
        self.store_col = store_col


    def calc_G(self, df: pd.DataFrame) -> float:
        """
        calculate G metric, G = # items sold/# items in stock - no money related

        Args:
            df: (pd.DataFrame) sales and stock data

        Returns:
            float = # items sold/# items in stock
        """
        items_sold = df[self.sales_col].sum()
        items_in_stock = df[self.stock_col].sum()

        return items_sold / items_in_stock

    def calc_H(self, df: pd.DataFrame, prices: dict) -> float:
        """
        calculate H metric, H = $ gained from items sales/# items in stock

        Args:
            df: (pd.DataFrame) sales and stock data
            prices: (dict) {sku: price}

        Returns:
            float = $ gained from items sales/# items in stock
        """
        items_sold = df[self.sales_col].sum()
        items_in_stock = df[self.stock_col].sum()
        total_sales_value = items_sold * prices[df[self.sku_col].iloc[0]]  # assuming same price for all SKUs in df

        return total_sales_value / items_in_stock

    def calc_I(self, df: pd.DataFrame, prices: dict) -> float:
        """
        calculate I metric, I = $ gained from sales/$ value of stock

        Args:
            df: (pd.DataFrame) sales and stock data
            prices: (dict) {sku: price}

        Returns:
            float = $ gained from sales/$ value of stock
        """
        total_sales_value = (df[self.sales_col] * prices[
            df[self.sku_col].iloc[0]]).sum()  # assuming same price for all SKUs in df
        stock_value = (df[self.stock_col] * prices[df[self.sku_col].iloc[0]]).sum()

        return total_sales_value / stock_value

    def calc_J(self, df: pd.DataFrame, year: int, month: int) -> float:
        """
        calculate J metric, J = # sales of store(i) (year =y, month = m)/# stock (store = i, year=y, month = m)

        Args:
            df: (pd.DataFrame) sales and stock data
            year: (int) year
            month: (int) month

        Returns:
            float = # sales of store(i) (year =y, month = m)/# stock (store = i, year=y, month = m)
        """
        df_filtered = df[(df[self.date_col].dt.year == year) & (df[self.date_col].dt.month == month)]
        items_sold = df_filtered[self.sales_col].sum()
        items_in_stock = df_filtered[self.stock_col].sum()

        return items_sold / items_in_stock

    def calc_1_over_G(self, df: pd.DataFrame) -> float:
        """
        calculate 1/G - 1 metric

        Args:
            df: (pd.DataFrame) sales and stock data

        Returns:
            float = 1/G - 1
        """
        G = self.calc_G(df)

        return 1 / G - 1

    def compare_years(self, df: pd.DataFrame, prices: dict, year1: int, year2: int) -> dict:
        """
        Compare metrics G, H, I, J and 1/G - 1 between two years

        Args:
            df: (pd.DataFrame) sales and stock data
            prices: (dict) {sku: price}
            year1: (int) First year for comparison
            year2: (int) Second year for comparison

        Returns:
            dict: Metrics for each year
        """
        df[self.date_col] = pd.to_datetime(df[self.date_col], format="%Y-%m-%d")
        df_year1 = df[df[self.date_col].dt.year == year1]
        df_year2 = df[df[self.date_col].dt.year == year2]

        metrics_year1 = {
            'G': self.calc_G(df_year1),
            'H': self.calc_H(df_year1, prices),
            'I': self.calc_I(df_year1, prices),
            'J': {month: self.calc_J(df_year1, year1, month) for month in range(1, 13)},
            '1/G - 1': self.calc_1_over_G(df_year1)
        }

        metrics_year2 = {
            'G': self.calc_G(df_year2),
            'H': self.calc_H(df_year2, prices),
            'I': self.calc_I(df_year2, prices),
            'J': {month: self.calc_J(df_year2, year2, month) for month in range(1, 13)},
            '1/G - 1': self.calc_1_over_G(df_year2)
        }

        comparison = {
            year1: metrics_year1,
            year2: metrics_year2
        }

        return comparison

    def compare_quarters(self, df: pd.DataFrame, prices: dict, year1: int, year2: int) -> dict:
        """
        Compare metrics between quarters in two years
        """

        metrics = ["G", "H", "I", "J", "1_over_G"]
        quarters = range(1, 5)

        comparison = {}

        for q in quarters:
            df[self.date_col] = pd.to_datetime(df[self.date_col], format="%Y-%m-%d")
            df_q1 = df[(df[self.date_col].dt.year == year1) & (df[self.date_col].dt.quarter == q)]
            df_q2 = df[(df[self.date_col].dt.year == year2) & (df[self.date_col].dt.quarter == q)]

            comp_q = {}

            for m in metrics:
                func = getattr(self, f"calc_{m}")
                if m == "G" or m == "1_over_G":
                    comp_q[m] = {q :(func(df_q1), func(df_q2)) }
                elif m == "J":
                    comp_q[m] = {q: (mean_over_months(func,df_q1, year1), mean_over_months(func,df_q2,year2))}
                else:
                    comp_q[m] = {q:(func(df_q1, prices), func(df_q2, prices)) }

            comparison[f"Q{q}"] = comp_q

        return comparison

    def compare_months(self, df: pd.DataFrame, prices: dict, year1: int, year2: int) -> dict:
        """
        Compare metrics between months in two years
        """
        df[self.date_col] = pd.to_datetime(df[self.date_col], format="%Y-%m-%d")
        metrics = ["G", "H", "I", "J", "1_over_G"]
        months = range(1, 13)

        comparison = {}
        for month in months:
            df_m1 = df[(df[self.date_col].dt.year == year1) & (df[self.date_col].dt.month == month)]
            df_m2 = df[(df[self.date_col].dt.year == year2) & (df[self.date_col].dt.month == month)]

            print(f"df_m1: {df_m1}")
            print(f"df_m2: {df_m2}")
            comp_m = {}

            for metric in metrics:
                func = getattr(self, f"calc_{metric}")
                if metric == "G" or metric == "1_over_G":
                    comp_m[metric] = {month:(func(df_m1), func(df_m2)) }
                elif metric == "J":
                    comp_m[metric] = {month: (func(df_m1, year1, month) ,func(df_m2,year2,month))}
                else:
                    comp_m[metric] = {month:(func(df_m1, prices), func(df_m2, prices))}

            comparison[f"M{month}"] = comp_m

            return comparison

