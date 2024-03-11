import discord
import responses
import random

# Define a list of mean comments
mean_comments = [
    "You're not very bright, are you?",
    "You couldn't find your way out of a paper bag.",
    "Do you ever listen to yourself?",
    "I've met smarter sandwiches.",
    "Why don't you try thinking before you speak?",
    "Did you even read the instructions?",
    "Your brain must be the size of a pea.",
    "You're about as useful as a screen door on a submarine."
]


async def send_message(message, user_message, is_private):
    try:
        # Check if the user's message is a question
        if user_message.startswith('?'):
            response = responses.get_response(user_message[1:])
        else:
            # Select a random mean comment
            response = random.choice(mean_comments)

        # Send the response to the user
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    # Replace TOKEN with your actual Discord bot token
    TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        # Check if the user's message is a question
        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)


# Run the bot
if __name__ == '__main__':
    run_discord_bot()
