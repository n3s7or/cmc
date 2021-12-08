import logging
import logging.handlers
import os


BASE_URL = 'https://pro-api.coinmarketcap.com'

LOG_FILE = os.environ.get('HX_CMC_LOG_FILE') or 'coinmarketcap.log'

formatter = logging.Formatter(r'%(asctime)s %(levelname)s [%(pathname)s:%(lineno)s] %(message)s')
sh = logging.handlers.WatchedFileHandler(LOG_FILE)
sh.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(sh)
logger.setLevel(logging.INFO)


API_KEY = os.environ.get('HX_CMC_APIKEY')

if not API_KEY:
    logger.critical('No API KEY provided. You must ensure `HX_CMC_APIKEY` environment variable is set')
    raise Exception('No API KEY provided. You must ensure `HX_CMC_APIKEY` environment variable is set')



