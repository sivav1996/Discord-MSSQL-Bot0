import discord
import AzConect
import respondBot
import os


async def send_message(message, user_message, is_private):
    try:
        response = respondBot.handle_message(user_message)
        await message.author.send(
            response
        ) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    TOKEN = 'insert token here'
    ID = ['465043911346487296', '436792250937376769']

    @client.event
    async def on_ready():
        print("Logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.content.startswith("!"):
            mod_id = str(message.author.id)
            if (mod_id) in ID:
                if message.author == client.user:
                    return

                # username = str(message.author)
                user_message = str(message.content)
                # channel = str(message.channel)

                if user_message[0] == "?":
                    user_message = user_message[1:]
                    await send_message(message, user_message, is_private=True)
                else:
                    await send_message(message, user_message, is_private=False)

                if message.content.startswith("!insert"):
                    params = message.content.split()
                    if len(params) != 7:
                        await send_message(message, "INVALID", is_private=False)
                        return

                    if len(params) == 7:
                        AzConect.insert_data(
                            params[1], params[2], params[3], params[4], params[5], params[6]
                        )
                        await send_message(message, "SUCCESS", is_private=False)
                        return

                if message.content.startswith("!get"):
                    # Parse the person ID from the command
                    person_id = message.content.split()
                    if len(person_id) != 2:
                        await send_message(message, "INVALID", is_private=False)
                        return
                    if len(person_id) == 2:
                        if (person_id[1]) != "all":
                            data_str = AzConect.get_account_info(
                                (person_id[1]))
                            if data_str == 'No record found':
                                await send_message(
                                    message, "FAILED "+"No record found", is_private=False
                                )
                            else:
                                await send_message(
                                    message, "SUCCESS" + data_str, is_private=False
                                )

                        if (person_id[1]) == "all":

                            await send_message(
                                message, "SUCCESS" + AzConect.get_data(), is_private=False
                            )

            if (mod_id) not in ID:
                await send_message(message, "INVALIDUSER", is_private=False)
                return

    client.run(TOKEN)
