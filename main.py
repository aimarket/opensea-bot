import discord
from discord.ext import commands
from tools import toolset


class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)



description = '''Welcome to open sea live floor'''

intents = discord.Intents.default()
intents.members = True
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix='-', description=description, intents=intents, help_command=help_command)

bot.help_command = MyNewHelp()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    """Pong"""
    await ctx.send(":ping_pong: ")
    print ("user has pinged")

class Opensea(commands.Cog):
    """Commands for Opensea bot!"""
    
    @commands.command()
    async def add(self,ctx, activity_link:str, keyword:str):
        """Adds link to list with keyword."""
        
        toolset.add_link(activity_link, keyword) 
        if ctx.invoked_subcommand is None:
            link =""
            if "?tab=activity" in activity_link:
                link = activity_link.split("/")[4].split("?")[0]
            else:
                link = activity_link.split("/")[4]
            await ctx.send(link+" added to list with keyword: ```"+keyword+"```")
            
    @commands.command()
    async def delete(self,ctx, keyword:str):
        """deletes link from list with keyword."""
        
        toolset.del_link(keyword) 
        if ctx.invoked_subcommand is None:
            await ctx.send("```"+keyword+"``` deleted from list.")

    @commands.command()
    async def links(self,ctx):
        """Show available links"""
        if ctx.invoked_subcommand is None:
            await ctx.send(toolset.list_links())
    
    @commands.command()
    async def flr(self,ctx, keyword:str):
        """Gets recent nft sales from specified collection"""
        async with ctx.typing():
            toolset.fetch_screenshot(keyword)
        file = discord.File("C:\\Location\\of\\screenshot.png") 
        await ctx.send(file = file)

   



bot.add_cog(Opensea())

bot.run('WEBHOOK_GOES_IN_THIS_SECTION')





