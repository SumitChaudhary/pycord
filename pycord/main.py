import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))        

"""
def dshello():
    dsc.
    response = requests.get('https://httpbin.org/ip')
    return('Your IP is {0}'.format(response.json()['origin']))
"""

def hello():
    print ('Hello World from function')

if __name__ == "__main__":
    hello()