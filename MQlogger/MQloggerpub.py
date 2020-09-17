import pika
import logging
from logging import Handler


class RabbitMQHandler(Handler):
    def __init__(
        self,
        broker_url,
        broker_port,
        broker_vhost,
        broker_username,
        broker_password,
        exchange,
        routing_key,
        level=logging.NOTSET,
        message_headers=None,
    ):
        Handler.__init__(self, level)
        # will be useful to specify the system publishing the log e.g KUZA,GRAPEVINE
        self.broker_url = broker_url
        self.broker_port = broker_port
        self.broker_vhost = broker_vhost
        self.broker_username = broker_username
        self.broker_password = broker_password
        self.message_headers = message_headers
        self.exchange = exchange
        self.routing_key = routing_key

    def get_channel(self):
        try:
            parameters = pika.ConnectionParameters(
                self.broker_url,
                self.broker_port,
                self.broker_vhost,
                pika.PlainCredentials(self.broker_username, self.broker_password),
            )
            # Connect to CloudAMQP
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            return channel
        except Exception as ex:
            raise Exception(ex)

    def emit(self, record):
        """
        will be used to push data to the queue for logging
        """
        self.acquire()  # locks the IO thread for publishing data to the MQ
        try:
            if self.get_channel():
                self.get_channel().basic_publish(
                    exchange=self.exchange,
                    routing_key=self.routing_key,
                    body=self.format(record),
                    properties=pika.BasicProperties(
                        delivery_mode=2, headers=self.message_headers
                    ),
                )
        except Exception as ex:
            self.handleError(record)
            raise Exception(ex)
        finally:
            self.release()
