'''
MIT License

Copyright (c) 2019 Nofil Qasim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
'''

#Library Imports
import discord
from discord.ext import commands

myself = '''I.... Am Bottinsation....
         Leader of the Discord Bots'''

#Command prefix for interfacing with bot in discord 
bot = commands.Bot(command_prefix='/', description = myself)

#Bot readout / Login descriptor
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

#User initiated command to send some pinoy trashtalk
@bot.command()
async def pinoy(ctx, member: discord.Member):
    ctx.send = ('{0.name} is a goblok anjing'.format(member))

#Run bot (String is bot token)
#Fake token here because repo is public
bot.run('NTk0NTQ3MDI5ODE3MDMyNzI1.XReBTw.XLtcKlYA3N0ohVq4QIRcP_E4KYI')