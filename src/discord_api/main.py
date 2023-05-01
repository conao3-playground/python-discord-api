import discord
import pydantic

class Settings(pydantic.BaseSettings):
    bot_token: str

    class Config:  # type: ignore
        env_file = '.env'

settings = Settings()  # type: ignore

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


def main():
    print('Hello, world!')
    client.run(settings.bot_token)
