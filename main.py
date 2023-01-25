import logging
import logging.handlers
import os
import requests

logger=logging.getLogger(__name__)   # Created logger
logger.setLevel(logging.DEBUG)
logger_file_handler=logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding='utf8'
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]

except KeyError:
    SOME_SECRET = "Token not avilabe!!"
    #logger.info("Token not avilabe!!")
    #raise Exception("Token not avilabe!!")

if __name__ == "_main_":
    logger.info(f"Token value: {SOME_SECRET}")
    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f"Weather in Berlin:{temperature}")