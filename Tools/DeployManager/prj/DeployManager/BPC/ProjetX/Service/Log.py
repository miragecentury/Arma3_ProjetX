__author__ = 'victorien.vanroye@gmail.com'

import logging

from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging
from raven import Client

class Logger():
    def __init__(self):
        self.client = Client(
            'https://3c18e3d3733c418db02ae756c563f8a5:0c54dac88a08442194f511e70ee35cdf@sentry.sudri.fr/3')
        self.handler = SentryHandler(self.client)
        setup_logging(self.handler)
        self.logger = logging.getLogger(__name__)

    def getLogger(self):
        return self.logger

    def getClient(self):
        return self.client