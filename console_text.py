import discord
import os
import datetime

#file for console calls when messaging user
def get_time():
    today = datetime.datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time