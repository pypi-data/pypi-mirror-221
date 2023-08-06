import hbshare as hbs
import pandas as pd
from hbshare.quant.Kevin.quant_room.MyUtil.data_loader import fetch_data_batch_hbs


class BigMomStrategyTest:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def _load_data(trade_date):
        # 所需数据: 收盘价、总市值、股息率、PEG
        sql_script = "SELECT SYMBOL, TDATE, TCLOSE, VOTURNOVER, TCAP FROM finchina.CHDQUOTE WHERE" \
                     " TDATE = {}".format(trade_date)
        df = fetch_data_batch_hbs(sql_script, "readonly")
        df = df[df['SYMBOL'].str[0].isin(['0', '3', '6'])]
        df.rename(columns={"SYMBOL": "ticker", "TDATE": "tradeDate", "TCAP": "marketValue",
                           "MCAP": "negMarketValue", "VATURNOVER": "turnoverValue",
                           "PCHG": "dailyReturnReinv"}, inplace=True)
        # 剔除ST、停牌、涨跌停的个股，剔除上市不满3个月的新股

    def run(self):
        self._load_data("20221230")


if __name__ == '__main__':
    BigMomStrategyTest("20221230", "20230720").run()