import discord
from discord.ext import commands
from Funciones.Sorteo_Funciones import recibir_mensajes,obtener_ganador,Inicio_Sorteo
from Funciones.LenerServer_Funciones import lener_links
####################################################################################################################################
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def Sorteo(ctx, *premio, tiempo=20):
    premios = " ".join(premio) # join para que los premios pasen de tuplas a un string normal (asi viendose mejor)
    await Inicio_Sorteo(ctx,premios,tiempo) # Inicio
    participantes = await recibir_mensajes(bot,tiempo) # Obteniendo mensajes durante el tiempo establecido
    ganador = await obtener_ganador(participantes) # obteniendo Ganador aleatorio
    await ctx.send(f"# El ganador de {premios} es: {ganador}") # Mostrar ganador

@bot.command()
async def lener(ctx):
    await lener_links(ctx) #Canales de lenner
  
def bot_run(token):
    bot.run(token) # Funcion para iniciar el Bot