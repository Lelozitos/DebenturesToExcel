from anbima import AnbimaBot

import requests

# bot = AnbimaBot() # today
# bot = AnbimaBot(1) # yesterday

# print(bot)

# bot.tableToCSV() # creates file in /history

for i in range(8): # latest anbima date
    bot = AnbimaBot(i)
    bot.tableToCSV()

# bot.headerToArray()
# bot.tableToArray()
# print(bot.headers)
# print(bot.dataTable)
