
from trading_ig import IGService
from trading_ig.config import config
import logging

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

    ig_service.create_session()
    # ig_stream_service.create_session(version='3')

    accounts = ig_service.fetch_accounts()
    print("accounts:\n%s" % accounts)
    
    
    epic = "CS.D.USDJPY.CFD.IP" 
    resolution = "D"
    num_points = 10

    
    response = ig_service.fetch_historical_prices_by_epic_and_num_points(
        epic, resolution, num_points
    )


    #(start_date, end_date) = ('2010-01-01 00:00:00', '2010-01-20 00:00:00')
    #response = ig_service.fetch_historical_prices_by_epic_and_date_range(
    # epic, resolution, start_date, end_date
    #)

    #response["prices"].to_pickle("./His_USDJPY.pkl") 
    print(response)

if __name__ == "__main__":
    main()
