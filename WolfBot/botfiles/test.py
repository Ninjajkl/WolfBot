import discord
client = discord.Client()
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('MjY3NjUzNDE0NjE0MzM1NDkw.DPsOng.3B4TVo1hb5kEXgehNUtYV8NCz9U')