import pandas as pd
import numpy as np


class MissSalesKPI:
    """
    This class calculate KPIs for missing sales
    Denote # - size of the set - for example # miss sales - number of missing sales (upto defined miss sale)
    Denote $ - value of the set - for example $ miss sales - value of missing sales (upto defined miss sale and a measure)

    Metrics:
    A = $ gained from sales
    B = $ value of missed sales
    C = # of missed sales
    D = # missed sales$/gained from sales
    E = $ value of missed/sales$ gained from sales

    KPIs:
        1.A/B/C/D/E in 2023 compared to 2022
            Our method
            Our method vs enemy method on poc (over stores, over a predefined period of time)
        2.A/B/C/D/E in 2023 compared to 2022 over the months 6-9
            Our method
            Our method vs enemy method on poc (over stores, over a predefined period of time)

        3.A/B/C/D/E in 2023 palmers week compared to 2022 palmers week
            Our method
            Our method vs enemy method on poc (over stores, over a predefined period of time)
    """

    def __init__(self, date_col, sku_col, store_col, sales_col,
                 price_col, stock_col):
        """
        This function initializes the class
        Args:
            date_col: (str) date column name
            sku_col: (str) sku column name
            store_col: (str) store column name
            sales_col: (str) sales column name
        """
        self.date_col = date_col
        self.sku_col = sku_col
        self.store_col = store_col
        self.sales_col = sales_col
        self.price_col = price_col
        self.stock_col = stock_col

    def calc_A(self, df: pd.DataFrame) -> float:
        """
        Calculates the total sales by multiplying the sales and price columns
        Args:
            df: (pd.DataFrame) sales data

        Returns:
            (float) total sales for the given data
        """
        sales = df[self.sales_col]
        prices = df[self.price_col]
        return (sales * prices).sum()

    def calc_B(self, df: pd.DataFrame,quantity: dict, prices: dict, threshold: int = 14) -> float:
        """
        This method calculates the total sales of the products that have been out of stock for more than 14 days
        and multiplies it by the price of the product at the time it went out of stock
        and then use the exponential function to calculate the total sales for the next 14 days
        Args:
            df:  (pd.DataFrame) sales data
            prices:  (dict) prices of the products
            threshold:  (int) number of days to consider the product out of stock

        Returns:
            (float) total sales for the given data

        """
        df = df[df[self.stock_col] == 0]
        if df.empty:
            return 0
        df = df.sort_values(self.date_col)
        df = df.reset_index(drop=True)
        df['days'] = df[self.date_col].diff().dt.days
        beta = df['days'].mean()
        T = df[df['days'] <= threshold].shape[0]
        return prices[df.iloc[0][self.sku_col]] * np.exp(T / beta)

    def calc_C(self, df: pd.DataFrame, quantity: dict,prices: dict, threshold: int = 14) -> float:
        """
        This method is # of missed sales for the products that have been out of stock for more than 14 days
        and multiplies it by the quantity of the product at the time it went out of stock
        and then use the exponential function to calculate the total sales for the next 14 days
        Args:
            df: (pd.DataFrame) sales data
            quantity:   (dict) quantity of the products
            threshold:  (int) number of days to consider the product out of stock

        Returns:
            (float) total sales for the given data
        """
        df = df[df[self.stock_col] == 0]
        if df.empty:
            return 0
        df = df.sort_values(self.date_col)
        df = df.reset_index(drop=True)
        df['days'] = df[self.date_col].diff().dt.days
        beta = df['days'].mean()
        T = df[df['days'] <= threshold].shape[0]
        return quantity[df.iloc[0][self.sku_col]] * np.exp(T / beta)

    def calc_D(self, df: pd.DataFrame, quantity: dict, prices: dict, threshold: int = 14):
        """
        This method calculates the ratio of the total sales of the products that have been out of stock for more than 14 days
        by formula D = B / A
        Args:
            df:   (pd.DataFrame) sales data
            df_stock:   (pd.DataFrame) stock data
            prices:     (dict) prices of the products
            threshold:  (int) number of days to consider the product out of stock

        Returns:
            (float) ratio of the total sales of the products that have been out of stock for more than 14 days
        """
        return self.calc_C(df, prices, threshold) / self.calc_A(df)

    def calc_E(self, df: pd.DataFrame, quantity: dict, prices: dict, threshold: int = 14):
        """
        This method calculates the ratio of the total sales of the products that have been out of stock for more than 14 days
        by formula E = B / C
        Args:
            df_sales:   (pd.DataFrame) sales data
            df_stock:   (pd.DataFrame) stock data
            prices:     (dict) prices of the products
            threshold:  (int) number of days to consider the product out of stock

        Returns:
            (float) ratio of the total sales of the products that have been out of stock for more than 14 days

        """
        return self.calc_B(df, prices,quantity, threshold) / self.calc_A(df)

    def calculate_first_kpi(self, our_data: dict, enemy_data: dict, prices: dict, quantity: dict, year1: int, year2: int) -> dict:
        """
        Args:
            kpi_dict:
            our_data:
            enemy_data:
            year1:
            year2:

        Returns:

        """
        our_sales_year1 = our_data['sales'][pd.to_datetime(our_data['sales'][self.date_col]).dt.year == year1]
        our_sales_year2 = our_data['sales'][pd.to_datetime(our_data['sales'][self.date_col]).dt.year == year2]
        enemy_sales_year1 = enemy_data['sales'][pd.to_datetime(enemy_data['sales'][self.date_col]).dt.year == year1]
        enemy_sales_year2 = enemy_data['sales'][pd.to_datetime(enemy_data['sales'][self.date_col]).dt.year == year2]
        kpi_dict = {}
        metrics = ["A", "B", "C", "D", "E"]
        function_dict = {
            "A": self.calc_A,
            "B": self.calc_B,
            "C": self.calc_C,
            "D": self.calc_D,
            "E": self.calc_E
        }
        for metric in metrics:

            if metric in ["B", "C","D", "E"]:
                our_metric_year1 = function_dict[metric](our_sales_year1, prices, quantity)
                our_metric_year2 = function_dict[metric](our_sales_year2, prices, quantity)
                enemy_metric_year1 = function_dict[metric](enemy_sales_year1, prices, quantity)
                enemy_metric_year2 = function_dict[metric](enemy_sales_year2, prices, quantity)
            else:
                our_metric_year1 = function_dict[metric](our_sales_year1)
                our_metric_year2 = function_dict[metric](our_sales_year2)
                enemy_metric_year1 = function_dict[metric](enemy_sales_year1)
                enemy_metric_year2 = function_dict[metric](enemy_sales_year2)
            kpi_dict[metric] = {}
            kpi_dict[metric][f'{year1}'] = (our_metric_year1, enemy_metric_year1)
            kpi_dict[metric][f"{year2}"] = (our_metric_year2, enemy_metric_year2)
        return kpi_dict

    def calculate_second_kpi(self, our_data: dict, enemy_data: dict, prices: dict, quantity: dict, year1: int, year2: int) -> dict:
        """
                Args:
                    kpi_dict:
                    our_data:
                    enemy_data:
                    year1:
                    year2:

                Returns:

        """
        kpi_dict = {}
        metrics = ["A", "B", "C", "D", "E"]
        function_dict = {
            "A": self.calc_A,
            "B": self.calc_B,
            "C": self.calc_C,
            "D": self.calc_D,
            "E": self.calc_E
        }

        for q in range(1, 5):
            our_sales_year1_q = our_data['sales'][our_data['sales'][self.date_col].dt.quarter == q]
            our_sales_year2_q = our_data['sales'][our_data['sales'][self.date_col].dt.quarter == q]

            enemy_sales_year1_q = enemy_data['sales'][enemy_data['sales'][self.date_col].dt.quarter == q]
            enemy_sales_year2_q = enemy_data['sales'][enemy_data['sales'][self.date_col].dt.quarter == q]

            for metric in metrics:
                if metric in ["B", "C","D", "E"]:
                    our_metric_year1 = function_dict[metric](our_sales_year1_q, prices, quantity)
                    our_metric_year2 = function_dict[metric](our_sales_year2_q, prices, quantity)
                    enemy_metric_year1 = function_dict[metric](enemy_sales_year1_q, prices, quantity)
                    enemy_metric_year2 = function_dict[metric](enemy_sales_year2_q, prices, quantity)
                else:
                    our_metric_year1 = function_dict[metric](our_sales_year1_q)
                    our_metric_year2 = function_dict[metric](our_sales_year2_q)
                    enemy_metric_year1 = function_dict[metric](enemy_sales_year1_q)
                    enemy_metric_year2 = function_dict[metric](enemy_sales_year2_q)
                kpi_dict[f'{metric}_Q{q}'] = {f'{year1}': (our_metric_year1, enemy_metric_year1),
                                              f'{year2}': (our_metric_year2, enemy_metric_year2)}

        return kpi_dict

    def calculate_third_kpi(self, our_data: dict, enemy_data: dict, prices: dict, quantity: dict, year1: int, year2: int) -> dict:
        """
                Args:
                    kpi_dict:
                    our_data:
                    enemy_data:
                    year1:
                    year2:

                Returns:

        """
        kpi_dict = {}
        metrics = ["A", "B", "C", "D", "E"]
        function_dict = {
            "A": self.calc_A,
            "B": self.calc_B,
            "C": self.calc_C,
            "D": self.calc_D,
            "E": self.calc_E
        }
        for m in range(1, 13):
            our_sales_year1_m = our_data['sales'][our_data['sales'][self.date_col].dt.month == m]
            our_sales_year2_m = our_data['sales'][our_data['sales'][self.date_col].dt.month == m]

            enemy_sales_year1_m = enemy_data['sales'][enemy_data['sales'][self.date_col].dt.month == m]
            enemy_sales_year2_m = enemy_data['sales'][enemy_data['sales'][self.date_col].dt.month == m]

            for metric in metrics:
                if metric in ["B", "C","D", "E"]:
                    our_metric_year1 = function_dict[metric](our_sales_year1_m, prices, quantity)
                    our_metric_year2 = function_dict[metric](our_sales_year2_m, prices, quantity)
                    enemy_metric_year1 = function_dict[metric](enemy_sales_year1_m, prices, quantity)
                    enemy_metric_year2 = function_dict[metric](enemy_sales_year2_m, prices, quantity)
                else:
                    our_metric_year1 = function_dict[metric](our_sales_year1_m)
                    our_metric_year2 = function_dict[metric](our_sales_year2_m)
                    enemy_metric_year1 = function_dict[metric](enemy_sales_year1_m)
                    enemy_metric_year2 = function_dict[metric](enemy_sales_year2_m)
                kpi_dict[f'{metric}_M{m}'] = {f'{year1}': (our_metric_year1, enemy_metric_year1),
                                              f'{year2}': (our_metric_year2, enemy_metric_year2)}

        return kpi_dict
