import logging
from message.logger.RabbitMQ_logger_handler import RabbitMQHandler

logger = logging.getLogger('Test project')
logger.setLevel(logging.DEBUG)

#all we need is the following two lines of code to start emitting the logs
Gv_handler = RabbitMQHandler('Grapevine')
logger.addHandler(Gv_handler)
#----------------------------#

log_prefix = 'Grapevine:Views'
logger.debug(u'{} {}'.format(log_prefix,'Test'))
logger.info('Test')
logger.exception('Testing')