#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
IG Markets REST API sample with Python
2015 FemtoTrader
"""

from trading_ig import IGService
from trading_ig.config import config
import logging

# if you need to cache to DB your requests
from datetime import timedelta
import requests_cache

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    logging.basicConfig(level=logging.DEBUG)

    expire_after = timedelta(hours=1)
    session = requests_cache.CachedSession(
        cache_name="cache", backend="sqlite", expire_after=expire_after
    )

    print(session.headers)
    # set expire_after=None if you don't want cache expiration
    # set expire_after=0 if you don't want to cache queries

    # config = IGServiceConfig()

    # no cache
    ig_service = IGService(
        config.username,
        config.password,
        config.api_key,
        config.acc_type,
        acc_number=config.acc_number,
    )

    # if you want to globally cache queries
    # ig_service = IGService(config.username, config.password, config.api_key,
    #   config.acc_type, session)

    ig_service.create_session()
    # ig_stream_service.create_session(version='3')

    accounts = ig_service.fetch_accounts()
    print("accounts:\n%s" % accounts)

    # account_info = ig_service.switch_account(config.acc_number, False)
    # print(account_info)

    # open_positions = ig_service.fetch_open_positions()
    # print("open_positions:\n%s" % open_positions)

    print("")

    # working_orders = ig_service.fetch_working_orders()
    # print("working_orders:\n%s" % working_orders)

    print("")

    # epic = 'CS.D.EURUSD.MINI.IP'
    epic = "CS.D.USDJPY.CFD.IP"  # US (SPY) - mini
    # epic = "CS.D.GBPUSD.CFD.IP"  # sample CFD epic

    resolution = "D"
    # see from pandas.tseries.frequencies import to_offset
    # resolution = 'H'
    # resolution = '1Min'

    num_points = 10
    response = ig_service.fetch_historical_prices_by_epic_and_num_points(
        epic, resolution, num_points
    )
    #response["prices"].to_pickle("./His_USDJPY.pkl") 
    print(response)
    # Exception: error.public-api.exceeded-account-historical-data-allowance

    # if you want to cache this query
    # response = ig_service.fetch_historical_prices_by_epic_and_num_points(
    #   epic, resolution, num_points, session
    # )

    # df_ask = response['prices']['ask']
    # print("ask prices:\n%s" % df_ask)

    #(start_date, end_date) = ('2010-01-01 00:00:00', '2010-01-20 00:00:00')
    #response = ig_service.fetch_historical_prices_by_epic_and_date_range(
    # epic, resolution, start_date, end_date
    #)

    #response["prices"].to_pickle("./His_USDJPY_D_2010-2023.pkl") 
    #print(response)

    # if you want to cache this query
    # response = ig_service.fetch_historical_prices_by_epic_and_date_range(
    #   epic, resolution, start_date, end_date, session
    # )
    # df_ask = response['prices']['ask']
    # print("ask prices:\n%s" % df_ask)


if __name__ == "__main__":
    main()
