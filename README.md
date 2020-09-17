# MQlogger

MQlogger is a Python library for publishing logs to RabbitMQ exchange

## Installation

Use the package manager [pip](https://pypi.org/project/MQlogger/) to install foobar.

```bash
pip install MQlogger
```

## Usage

```python
import logging
from MQlogger.MQloggerpub import RabbitMQHandler
rmq_handler = RabbitMQHandler('broker_url',
        'broker_port',
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

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)