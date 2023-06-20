import discord
from discord.ext import commands
import dotenv
import os
from googletrans import Translator, LANGUAGES, LANGCODES

def main():
    dotenv.load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    return_lang = 'en' #default language
    allowed_channels = [] 
    BOT_PREFIX = '~'

    translator = Translator()
    bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())


    @bot.event
    async def on_ready(): #startup message
        print(f'{bot.user.name} has connected to Discord!')

        
    @bot.event
    async def on_message(message):
        # Ignore messages from the bot itself
        if message.author == bot.user:
            return
        
        # Ignore messages that don't start with the command prefix
        if message.content.startswith(BOT_PREFIX):
            await bot.process_commands(message)
            return
        
        # Ignore messages from channels not in the allowed channels list
        if message.channel.id not in allowed_channels:
            return
        msg = message.content.lower()
        msg_lang = translator.detect(msg)
        
        # Ignore messages that are already in the desired language
        if msg_lang.lang == return_lang:
            return
        
        translation = translator.translate(msg, dest=return_lang, src=msg_lang.lang)
        channel = message.channel
        await channel.send(translation.text)
        

    @bot.command(name='lang_change', help='Changes the language of the bot')
    async def lang_change(ctx, lang, *args):
        global return_lang
        if lang in LANGUAGES:
            print(f'Changing language to {lang}')
            return_lang = lang
        elif lang in LANGCODES:
            print(f'Changing language to {LANGCODES[lang]}')
            return_lang = LANGCODES[lang]
        else:
            await ctx.send(f'Language not found: {lang}')
            return
            
    @bot.command(name='lang_search', help='Lists all languages supported by the bot')
    async def lang_search(ctx, search=None):
        if search == None:
            await ctx.send(LANGUAGES)
            return
        
        search = search.lower()
        if search in LANGUAGES:
            await ctx.send(f'{search}: {LANGUAGES[search]}')
            return
        elif search in LANGCODES:
            await ctx.send(f'{LANGCODES[search]}: {search}')
            return
        else:
            await ctx.send(f'Language not found: {search}')
            
    @bot.command(name='channel_add', help='Adds a channel to the allowed channels list')
    async def channel_add(ctx):
        global allowed_channels
        allowed_channels.append(ctx.channel.id)
        await ctx.send(f'Added channel {ctx.channel.name} to allowed channels list')
        
    @bot.command(name='channel_remove', help='Removes a channel from the allowed channels list')
    async def channel_remove(ctx):
        global allowed_channels
        allowed_channels.remove(ctx.channel.id)
        await ctx.send(f'Removed channel {ctx.channel.name} from allowed channels list')
        
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
