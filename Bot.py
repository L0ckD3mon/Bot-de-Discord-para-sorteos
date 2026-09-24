import discord
from discord.ext import commands
from Sorteo_Funciones import recibir_mensajes,obtener_ganador,Inicio_Sorteo

prefix_list = ["!","/","?"]
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix_list,intents=intents)

@bot.command()
async def Sorteo(ctx, *premio, tiempo=15):

    premios = await Inicio_Sorteo(ctx=ctx,premio=premio)
    participantes = await recibir_mensajes(bot,tiempo=tiempo),
    ganador = await obtener_ganador(participantes)

    await ctx.send(f"# El ganador de {premios} es: {ganador[0]}")

def bot_run(token):
    bot.run(token)