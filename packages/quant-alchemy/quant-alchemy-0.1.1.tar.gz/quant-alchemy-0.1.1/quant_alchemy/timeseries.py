import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis, jarque_bera, norm

class Timeseries:
    """
    A class to perform financial calculations on time series data.
    """
    
    def __init__(self, prices):
        """
        Constructs all the necessary attributes for the Timeseries object.

        Parameters
        ----------
        prices : pandas.Series or pandas.DataFrame
            The time series data of prices.
        """
        self.prices = prices.copy()

    def returns(self):
        """
        Calculate the simple returns of the time series data.

        Returns
        -------
        pandas.Series or pandas.DataFrame
            The simple returns of the time series data.
        """
        return self.prices.pct_change()

    def log_returns(self):
        """
        Calculate the logarithmic returns of the time series data.

        Returns
        -------
        pandas.Series or pandas.DataFrame
            The logarithmic returns of the time series data.
        """
        return np.log(self.prices/self.prices.shift(1))

    def volatility(self):
        """
        Calculate the volatility (standard deviation) of the returns of the time series data.

        Returns
        -------
        float
            The volatility of the returns of the time series data.
        """
        return self.prices.pct_change().std(ddof=1)
    
    def periods_in_year(self, period, trading_days=252, hours_per_day=8):
        """
        Calculate the number of periods in a year based on the given period, trading days and trading hours.

        Parameters
        ----------
        period : str
            The period ('annually', 'semi-annually', 'quarterly', 'monthly', 'weekly', 'daily', '4hourly', 'hourly', '30min', '15min', '5min', or '1min').
        trading_days : int, optional
            The number of trading days in a year (default is 252).
        hours_per_day : int, optional
            The number of trading hours in a day (default is 8).

        Returns
        -------
        int or str
            The number of periods in a year, or an error message if the period is invalid.
        """
        if hours_per_day not in [8, 24]:
            raise ValueError('Invalid number of trading hours. Please choose 8 (for traditional markets) or 24 (for cryptocurrencies and forex)')

        return {
            'annually': 1,
            'semi-annually': 2,
            'quarterly': 4,
            'monthly': 12,
            'weekly': 52 * (hours_per_day / 24),
            'daily': trading_days,
            '4hourly': trading_days * hours_per_day / 4,
            'hourly': trading_days * hours_per_day,
            '30min': trading_days * hours_per_day * 2,
            '15min': trading_days * hours_per_day * 4,
            '5min': trading_days * hours_per_day * 12,
            '1min': trading_days * hours_per_day * 60,
        }.get(period.lower(), "Invalid period. Please choose a valid period")

    def annualized_returns(self, period='daily', trading_days=252, hours_per_day=8):
        """
        Calculate the annualized returns of the time series data.

        Parameters
        ----------
        period : str, optional
            The period of the time series data (default is 'daily'). ('annually', 'semi-annually', 'quarterly', 'monthly', 'weekly', 'daily', '4hourly', 'hourly', '30min', '15min', '5min', or '1min') (default is 'daily').
        trading_days : int, optional
            The number of trading days in a year (default is 252).
        hours_per_day : int, optional
            The number of trading hours in a day (default is 8).

        Returns
        -------
        float
            The annualized returns of the time series data.
        """
        periods = self.periods_in_year(period, trading_days, hours_per_day)
        if isinstance(periods, str):
            raise ValueError(periods)
        return self.prices.pct_change().mean() * periods

    def annualized_volatility(self, period='daily', trading_days=252, hours_per_day=8):
        """ 
        Calculates the annualized volatility of the financial data given a specific period, 
        the number of trading days, and the number of trading hours per day. 

        The annualized volatility is calculated as the standard deviation of the percent changes 
        in the data times the square root of the number of periods in a year.

        Parameters: 
            period (str, optional): The period type of the time series data (i.e. 'annually', 'semi-annually', 'quarterly', 
                                    'monthly', 'weekly', 'daily', '4hourly', 'hourly', '30min', 
                                    '15min', '5min', '1min'). Defaults to 'daily'.
            trading_days (int, optional): The number of trading days in a year. Defaults to 252.
            hours_per_day (int, optional): The number of trading hours in a day. Defaults to 8.

        Raises: 
            ValueError: If the given period is not valid.

        Returns: 
            float: The calculated annualized volatility.
        """
        periods = self.periods_in_year(period, trading_days, hours_per_day)
        if isinstance(periods, str):
            raise ValueError(periods)
        return self.prices.pct_change().std(ddof=1) * np.sqrt(periods)

    def compound_returns(self):
        """
        This method calculates and returns the compounded returns.

        Returns:
            float: The compounded return.
        """
        returns = self.returns()
        return np.expm1(np.log1p(returns).sum())
    
    def max_drawdown(self):        
        """
        This method calculates and returns the maximum drawdown of the time series data.
        
        The drawdown is the percentage loss from the highest point to the lowest point.
        
        Returns:
            float: The maximum drawdown of the time series data.
        """
        return (self.prices / self.prices.cummax()).min() - 1
    
    def drawdown(self):
        """
        This method calculates and returns a DataFrame containing the return series,
        cumulative return series, previous peak in the cumulative returns, 
        and the drawdown series.

        The drawdown is the percentage loss from the highest point to the lowest point.

        Returns:
            dict: A dictionary where the keys are column names and the values are DataFrames containing the return series, cumulative return series, previous peak in the cumulative returns, and the drawdown series.
        """
        return_series = self.returns()
        cumulative_returns = (1 + return_series).cumprod()
        running_max = cumulative_returns.cummax()
        running_max.iloc[0] = 1.0
        drawdown = (cumulative_returns) / running_max - 1.0

        return {
            col: pd.DataFrame({
                'Returns': return_series[col],
                'Cumulative Returns': cumulative_returns[col],
                'Running Max': running_max[col],
                'Drawdown': drawdown[col]
            })
            for col in return_series.columns
        }

    def skewness(self):
        """
        This method calculates and returns the skewness of the returns of the time series data.

        Skewness is a measure of the asymmetry of the probability distribution.

        Returns:
            float: The skewness of the returns of the time series data.
        """
        returns = self.returns()
        return skew(returns)
    
    def kurtosis(self):
        """
        This method calculates and returns the kurtosis of the returns of the time series data.

        Kurtosis is a statistical measure that defines how heavily the tails of a distribution differ from the tails of a normal distribution.

        Returns:
            float: The kurtosis of the returns of the time series data.
        """
        returns = self.returns()
        return kurtosis(returns)
    
    def is_normal(self, level=0.01):
        """
        This method applies the Jarque-Bera test to determine if the returns are normally distributed.

        The Jarque-Bera test is a goodness-of-fit test of whether sample data have the skewness and kurtosis matching a normal distribution.

        Returns:
            bool: True if the p-value of the test is greater than the significance level indicating that
                the returns could be from a normal distribution, False otherwise.
        """
        returns = self.returns()
        _, p_value = jarque_bera(returns)
        return p_value > level
    
    def sharpe_ratio(self, period='daily', risk_free_rate=0.0, trading_days=252, hours_per_day=8):
        """
        This method calculates and returns the Sharpe ratio of the time series data.

        The Sharpe ratio is a measure of risk-adjusted return.

        Parameters:
            period (str, optional): The period type of the time series data (i.e. 'annually', 'semi-annually', 'quarterly', 
                                    'monthly', 'weekly', 'daily', '4hourly', 'hourly', '30min', 
                                    '15min', '5min', '1min'). Defaults to 'daily'.
            risk_free_rate (float, optional): The risk-free rate of return. Defaults to 0.0.
            trading_days (int, optional): The number of trading days in a year. Defaults to 252.
            hours_per_day (int, optional): The number of trading hours in a day. Defaults to 8.

        Raises:
            ValueError: If the given period is not valid.

        Returns:
            float: The Sharpe ratio of the time series data.
        """
        periods = self.periods_in_year(period, trading_days, hours_per_day)
        if isinstance(periods, str):
            raise ValueError(periods)
        
        annualized_returns = self.annualized_returns(period, trading_days, hours_per_day)
        annualized_volatility = self.annualized_volatility(period, trading_days, hours_per_day)
        return (annualized_returns - risk_free_rate) / annualized_volatility

    def semideviation(self, threshold=0.0):
        """
        Calculates semideviation of the returns that are less than the provided threshold.

        Parameters:
            threshold (float, optional): The reference value below which a return is considered as underperforming. 
            Defaults to 0.0, meaning any negative return is considered underperforming.

        Returns:
        float: The semideviation of the returns. This is computed as the square root of the 
                average of the squared deviations of the underperforming returns from their mean.
                The method uses a degrees of freedom (ddof) value of 1, implying that the function
                computes sample standard deviation which is an unbiased estimator of the population 
                standard deviation.
        """
        returns = self.returns()
        return returns[returns < threshold].std(ddof=1)

def var_historic(self, level=5):
    """
    This method calculates and returns the historic Value at Risk (VaR) at a specified level.

    VaR is a statistical technique used to measure and quantify the level of financial risk within a firm or investment portfolio over a specific time frame.

    Parameters:
        level: (float, optional)
            The percentile level at which to calculate VaR. This is the level below which the returns would fall with the given level of probability. Defaults to 5.

    Raises:
        ValueError: If the given level is not a valid percentile (i.e., not between 0 and 100).

    Returns:
        float: The historic VaR at the specified level. This is the return value such that 'level' percent of returns fall below this number and (100 - level) percent of returns fall above this number.
    """
    if not 0 <= level <= 100:
        raise ValueError("The 'level' should be a percentile, i.e., between 0 and 100.")
    
    returns = self.returns()
    return np.percentile(returns, level)

    def cvar_historic(self, level=5):
        """
        Calculates the historic Conditional Value at Risk (CVaR), also known as Expected Shortfall (ES),
        at a specified level. CVaR quantifies the expected value of loss given that a certain level of 
        loss threshold (VaR) has been exceeded.

        Parameters:
            level: (float, optional)
                The percentile level at which to calculate CVaR. This is the level below which the returns would 
                fall with the given level of probability. Defaults to 5.

        Raises:
            ValueError: If the given level is not a valid percentile (i.e., not between 0 and 100).

        Returns:
            float: The historic CVaR at the specified level. This is the average return value such that 'level' 
                percent of returns fall below this number.
        """
        if not 0 <= level <= 100:
            raise ValueError("The 'level' should be a percentile, i.e., between 0 and 100.")
        
        returns = self.returns()
        var = np.percentile(returns, level)
        return returns[returns <= var].mean()

    def var_gaussian(self, level=5):
        """
        Calculates the Gaussian Value at Risk (VaR) at a specified level.

        Parameters:
            level: (float, optional)
                The percentile level at which to calculate VaR. This is the level below which the returns would 
                fall with the given level of probability. Defaults to 5.

        Raises:
            ValueError: If the given level is not a valid percentile (i.e., not between 0 and 100).

        Returns:
            float: The Gaussian VaR at the specified level. This is the return value such that 'level' percent of 
                    returns fall below this number, assuming returns follow a Gaussian distribution.
        """
        if not 0 <= level <= 100:
            raise ValueError("The 'level' should be a percentile, i.e., between 0 and 100.")
        
        returns = self.returns()
        # Using 'ppf' function to find the percentile point
        return -norm.ppf(level/100, loc=returns.mean(), scale=returns.std(ddof=1))