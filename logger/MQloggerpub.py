import pika
import logging
from logging import Handler
from message.mq_connection import MQConnection


class RabbitMQHandler(Handler):
    def __init__(
            self, exchange, routing_key, level=logging.NOTSET, message_headers=None,
    ):
        Handler.__init__(self, level)
        # will be useful to specify the system publishing the log e.g KUZA,GRAPEVINE
        self.message_headers = message_headers
        self.exchange = exchange
        self.routing_key = routing_key

    def get_channel(self):
        connection = MQConnection.getInstance()
        channel = connection.channel()
        return channel

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
        except Exception:
            self.handleError(record)
            raise Exception
        finally:
            self.release()
