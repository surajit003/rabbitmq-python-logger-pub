from setuptools import setup

setup(
    name="pub_rabbitmq",  # This is the name of your PyPI-package.
    version="0.1",  # Update the version number for new releases
    scripts=[
        "MQloggerpub"
    ],  # The name of your scipt, and also the command you'll be using for calling it
    download_url='https://github.com/surajit003/rabbitmq-python-logger-pub/archive/v1.0.tar.gz',
    install_requires=[
              'pika',
          ],
)
