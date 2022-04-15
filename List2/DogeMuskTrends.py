import seaborn as sns
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import pandas as pd


def show_trends():
    trends_dogecoin = TrendReq()
    trends_musk = TrendReq()

    trends_dogecoin.build_payload(kw_list=["dogecoin"])
    trends_musk.build_payload(kw_list=["musk"])
    over_time_dogecoin = pd.DataFrame(trends_dogecoin.interest_over_time())
    over_time_musk = pd.DataFrame(trends_musk.interest_over_time())

    sns.lineplot(data=over_time_musk, x="date", y="musk", color='b')
    sns.lineplot(data=over_time_dogecoin, x="date", y="dogecoin", color='r')

    plt.legend(labels=["dogecoin", "musk"])
    plt.show()


if __name__ == '__main__':
    show_trends()
