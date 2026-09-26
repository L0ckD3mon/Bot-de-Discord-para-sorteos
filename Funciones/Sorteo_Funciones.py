import asyncio
from random import choice
####################################################################################################################################

# Mensajes que dan inicio al sorteo
async def Inicio_Sorteo(ctx,premios: str,tiempo: int):
    await ctx.send(f"# {ctx.author} Inicio un sorteo, Lo sorteado es: {premios}")
    await asyncio.sleep(1)
    await ctx.send(f'¡Todo el que escriba en los proximos {tiempo} segundos despues de la cuenta regresiva se unira al sorteo!')
    await asyncio.sleep(2)
    await ctx.send("Empezamos en 3")
    await asyncio.sleep(1)
    await ctx.send("Empezamos en 2")
    await asyncio.sleep(1)
    await ctx.send("Empezamos en 1")
    await asyncio.sleep(1)
    await ctx.send("YA!!!!")

# Almacenar quien envia mensajes en un lapso de tiempo, este ultimo administrador por un contador
async def recibir_mensajes(bot,tiempo: int):
    participantes = []
    # Inicia la cuenta regresiva
    contador = asyncio.get_event_loop().time() + tiempo
    contador -= asyncio.get_event_loop().time()

    try:
        while contador:
            msj = await bot.wait_for("message",timeout=contador) # Recibe los mensajes durante el tiempo establecido
            nombre = msj.author.mention # Es el @ del usuario
            if nombre not in participantes:
                participantes.append(nombre)   
    except TimeoutError: # Para cuando se acaba el tiempo
        return participantes

# Sacar un ganador aleatorio
async def obtener_ganador(participantes: list[str]):
    ganador = choice(participantes) # Choice elije un participante aleatorio
    return ganador