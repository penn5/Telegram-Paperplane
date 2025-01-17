# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from os import environ
from sqlite3 import connect

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

from userbot import LOGS, LogicWorker, bot
from userbot.modules import ALL_MODULES

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n  Tip: Use Country Code along with No.' \
             '\n       Recheck your Phone Number'

for i in ALL_ROWS:
    LogicWorker.append(i[0])
connect("learning-data-root.check").close()
try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Your Bot is alive! Test it by typing .alive on any chat."
          " Should you need assistance, head to https://t.me/userbot_support")
LOGS.info("Your Bot Version is 4.0")

CI_TEST = environ.get("CI", None)
if CI_TEST:
    bot.disconnect()
else:
    bot.run_until_disconnected()
