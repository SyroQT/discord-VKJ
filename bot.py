from cut import cut
import discord
import asyncio
ID = 678175450618658816
# skaitom tokena


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readline()
        return lines.strip()


def bot():
    token = read_token()
    bible = cut()
    client = discord.Client()

    @client.event
    async def on_ready():
        channel = client.get_channel(ID)
        # await channel.send(bible)
        if (len(bible) > 2000):


channel.send(
    "Šios dienos evangelija per ilgą. Ją rasite: http://kasdienapmastau.lt/")
        else:
            await channel.send(bible)

        exit()

    client.run(token)


if __name__ == "__main__":
    bot()
