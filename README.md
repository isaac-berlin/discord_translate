# Discord Translator Bot
A discord bot to automatically translate messages in a channel to a specified language. It only translates messages that are not already in the desired language. This bot uses the [Google Cloud Translation API](https://cloud.google.com/translate/docs) with the [googletrans](https://pypi.org/project/googletrans/) python package the to translate messages. This bot is written in Python using the [discord.py](https://discordpy.readthedocs.io/en/stable/api.html) library.

## Usage
1. Invite the bot to your server using [this link](https://discord.com/api/oauth2/authorize?client_id=1120740957411880983&permissions=60480&scope=bot).
2. Type `~channel_add` in the channel you want to translate messages in.
3. You are done! All messages in that channel will be translated to English if no already.


## Commands
- `~channel_add` - Adds the channel to the list of channels to translate messages in.
- `~channel_remove` - Removes the channel from the list of channels to translate messages in.
- `~lang_search` - Lists if search language is in the list of supported languages and lists all avaliable languages if no search term is given.
- `~lang_change` - Sets the language to translate messages (english by default).

## Run yourslef
1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a .env file in the root directory of the project and add the following: `DISCORD_TOKEN=<your discord bot token>`
4. Run the bot using `python bot.py`.