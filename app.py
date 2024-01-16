#!/usr/bin/python

import requests
import logging
import time

from random import randint

APPS = [{"name": "marley", "port": "8080"}]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

while True:
    random0 = randint(0, len(APPS) - 1)
    random1 = randint(0, 15)
    random2 = randint(1, 10)

    url_base = f"http://{APPS[random0]['name']}:{APPS[random0]['port']}/logs/"

    if random1 > 11:
        random1 = 0

    if random1 <= 4:
        url = url_base + "info"
        try:
            requests.get(url)
            logger.info(f"requesting {url}")
        except requests.exceptions.ConnectionError as e:
            logger.critical(e)

    elif random1 >= 5 and random1 <= 8:
        url = url_base + "warning"
        try:
            requests.get(url)
            logger.warning(f"requesting {url}")
        except requests.exceptions.ConnectionError as e:
            logger.critical(e)

    elif random1 >= 9 and random1 <= 10:
        url = url_base + "info"

        try:
            requests.get(url)
            logger.error(f"requesting {url}")
        except requests.exceptions.ConnectionError as e:
            logger.critical(e)

    else:
        url = url_base + "info"

        try:
            requests.get(url)
            logger.debug(f"requesting {url}")
        except requests.exceptions.ConnectionError as e:
            logger.critical(e)

    time.sleep(random2)
