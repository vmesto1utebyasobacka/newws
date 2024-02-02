from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 25116728
api_hash = "8fef459b63e30e0d4c7febd57d036648"
phone = "+994707909293"

# The channel/Group name that you want to get messages from
source_channel_name = 'Swing Trades | CST 🎯'

# The channel/Group that you want to send messages to
destination_channel_link = -1001874052676

client = TelegramClient(phone, api_id, api_hash)


async def send_to_destination(message, channel, media):
    await client.send_message(entity=channel, message=message, file=media)


@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title == source_channel_name:
            message = event.message
            text = message.text
            media = message.media

            # Check for specific keywords in the message
            keywords = ["- Binance Killers®", "1) Open Interest"]
            keywords_1 = ["- Binance Killers®", "BK® Crypto Fear and Greed Index"]
            keywords_2 = ["- Binance Killers®", "VIP Crypto Market RSI Heatmap", "Timeframe: Daily"]
            keywords_3 = ["UPDATE VIP", "We told you first,", "Fed. Russian Insiders®"]
            keywords_4 = ["- Bitcoin Bullets® Trading", "VIP NEWS"]
            keywords_5 = ["INSIDER UPDATE", "Bitcoin Bullets® Trading"]

            # Check if the text contains the exact phrase "the price action"
            if "support level" not in text.lower():
                if all(keyword in text for keyword in keywords):
                    modified_text = text.replace("VIP", "CM's").replace("- Binance Killers®", "- Crypto Moon®")
                    await send_to_destination(modified_text, destination_channel_link, media)

                elif all(keyword in text for keyword in keywords_1):
                    modified_text = text.replace("BK®", "CM®").replace("- Binance Killers®", "- Crypto Moon®")
                    await send_to_destination(modified_text, destination_channel_link, media)

                elif all(keyword in text for keyword in keywords_2):
                    modified_text = text.replace("VIP", "CM®").replace("- Binance Killers®", "- Crypto Moon®")
                    await send_to_destination(modified_text, destination_channel_link, media)

                elif all(keyword in text for keyword in keywords_3):
                    modified_text = text.replace("VIP", "NEWS").replace("Fed. Russian Insiders®",
                                                                        "- Crypto Moon®").replace("We told you first,",
                                                                                                  "")
                    await send_to_destination(modified_text, destination_channel_link, media)

                elif all(keyword in text for keyword in keywords_4):
                    modified_text = text.replace("VIP", "CM®").replace("- Bitcoin Bullets® Trading", "- Crypto Moon®")
                    await send_to_destination(modified_text, destination_channel_link, media)

                elif all(keyword in text for keyword in keywords_5):
                    modified_text = text.replace("Bitcoin Bullets® Trading", "- Crypto Moon®")
                    await send_to_destination(modified_text, destination_channel_link, media)

    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit


client.start()
client.run_until_disconnected()