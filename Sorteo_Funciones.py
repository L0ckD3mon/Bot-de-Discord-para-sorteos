import asyncio
from random import randint

async def recibir_mensajes(bot,tiempo):
    participantes = []
    contador = asyncio.get_event_loop().time() + tiempo + 1
    tiempo_restante = contador - asyncio.get_event_loop().time()
    try:
        while True:
            if tiempo_restante > 0:
                msj = await bot.wait_for("message",timeout=tiempo_restante)
                nombre = msj.author.mention
                if not participantes:
                    participantes.append(nombre)
                    
            else:
                return participantes
    except TimeoutError:
        print("Se acabo el tiempo")
        return participantes

async def Inicio_Sorteo(ctx,premio):
    # un join que evita que El premio salga como una tupla: ("premio1", "premio2").
        premios = " ".join(premio)
        # Salida: premio1 premio2
    
        await ctx.send(f"# {ctx.author} Inicio un sorteo, El premio es: {premios}")
        await asyncio.sleep(1)
        await ctx.send('¡Todo el que escriba en los proximos 20 segundos despues de la cuenta regresiva se unira al sorteo!')
    
        await asyncio.sleep(1.8)
    
        await ctx.send("Empezamos en 3")
        await asyncio.sleep(1)
    
        await ctx.send("Empezamos en 2")
        await asyncio.sleep(1)
    
        await ctx.send("Empezamos en 1")
        await asyncio.sleep(1)
    
        await ctx.send("YA!!!!")
        print("a")
        return premios

async def obtener_ganador(participantes):
    print(participantes)
    ultimo_participante = len(participantes) - 1
    numero_aleatorio = randint(0,ultimo_participante)
    ganador = participantes[numero_aleatorio]
    return ganador