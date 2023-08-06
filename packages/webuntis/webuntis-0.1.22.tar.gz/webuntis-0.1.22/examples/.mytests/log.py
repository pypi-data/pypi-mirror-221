import logging.handlers
import sys

LOG_FILENAME = 'webuntis.log'



# Set up a specific logger with our desired output level
my_logger = logging.getLogger('WebuntisLogger')
# my_logger.setLevel(logging.INFO)
# my_logger.setLevel(logging.WARNING)
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5000000, backupCount=5)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)-24s %(name)-9s %(levelname)-7s %(message)s')
# tell the handler to use this format
handler.setFormatter(formatter)
my_logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
# console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-9s %(levelname)-7s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
my_logger.addHandler(console)


