import discord
from discord.ext import commands
from discord.utils import get





client = commands.Bot(command_prefix = '!')
client.remove_command('help')
# !help



@client.event

async def on_ready():
	print('PB works fine UwU')

@client.event

async def on_member_join(member):
	channel = client.get_channel( 769304139678089229 )

	role = discord.utils.get(member.guild.roles, id = 769516108561776651)

	await member.add_roles( role )



##########MUTE####################################################
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def mute(ctx, member: discord.Member):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'MUTE')
	await member.add_roles(mute_role)
	await member.send('You have been muted on server')
	await ctx.send(f'{member.mention} has been muted')


##########UNMUTE##################################################
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unmute(ctx, member: discord.Member):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'MUTE')
	await member.remove_roles(mute_role)
	await member.send('You have been unmuted on server')
	await ctx.send(f'{member.mention} has been unmuted')
##########SUPPORT#################################################
@client.command(pass_context = True)

async def support(ctx):
	await ctx.send("If you need help join support discord server ||https://discord.gg/jK3JqsauEJ|| or write this guy SadBoi_69#9806")

##########BOTSERVERS##############################################

@client.command(pass_context=True)
async def botservers(ctx):
    await ctx.send(f"Count of servers: {len(client.guilds)}")

##########ADD_ROLE################################################
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def addrole(ctx, member: discord.Member, role: discord.Role):
	await member.add_roles(role)
	await ctx.send(f"{member.mention} got role {role.mention}")


##########REMOVE_ROLE#############################################
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def removerole(ctx, member: discord.Member, role: discord.Role):
	await member.remove_roles(role)
	await ctx.send(f"{member.mention} lost role {role.mention}")

##########HELP####################################################

@client.command(pass_context = True)

async def help(ctx):
	emb = discord.Embed(title='Commands help', color = discord.Color.purple())

	emb.add_field(name='{}clear'.format( '!' ), value='Clear chat(Only admins)')
	emb.add_field(name='{}kick'.format( '!' ), value='Kick member(Only admins)')
	emb.add_field(name='{}hello'.format( '!' ), value='Hello of bot')
	emb.add_field(name='{}ban'.format( '!' ), value='Ban member(Only admins)')
	emb.add_field(name='{}unban'.format( '!' ), value='Unban member(Only admins)')
	emb.add_field(name='{}mute'.format( '!' ), value='Mute member(Only admins)')
	emb.add_field(name='{}addrole'.format( '!' ), value='Add role to user(Only admins)')
	emb.add_field(name='{}removerole'.format( '!' ), value='Remove role from user(Only admins)')
	emb.add_field(name='{}unmute'.format( '!' ), value='Unmute member(Only admins)')
	#emb.add_field(name='{}rules'.format( '!' ), value='Правила')

	await ctx.send(embed = emb)


##########HELLO###################################################

@client.command(pass_context = True)

async def hello(ctx):
	author = ctx.message.author
	await ctx.send(f'Hello {author.mention}, I am open source PurpleBot UwU')

##########KICK####################################################

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):

	await member.kick(reason = reason)
	await member.send('You have been kicked from server')
	await ctx.send(f"{member.name} has been kicked from server!")

##########BAN#####################################################

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):

	await member.ban(reason = reason)
	await member.send('You have been banned on server')
	await ctx.send(f"{member.name} has been banned on server!")

########UNBAN#####################################################

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member):


	banned_users = await ctx.guild.bans()
	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await member.send('You has been unbanned on server')
		await ctx.send(f'{user.mention} has been banned on server!')
		return
##########CLEAR###################################################


@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def clear(ctx, amount = 100):
	await ctx.channel.purge(limit = amount)







##########CLIENTRUN###############################################

client.run('token here')
