from MQlogger.MQloggerpub import RabbitMQHandler
import logging
rmq_handler = RabbitMQHandler('broker_url',
        5672,
        'broker_vhost',
        'broker_username',
        'broker_password',
        'broker_exchange',
        'broker_routing_key',
        level=logging.NOTSET,
        message_headers=None,)

logger = logging.getLogger('Test project')
logger.setLevel(logging.DEBUG)
logger.addHandler(rmq_handler)
logger.debug('Test data')
logger.info('Testing again')
