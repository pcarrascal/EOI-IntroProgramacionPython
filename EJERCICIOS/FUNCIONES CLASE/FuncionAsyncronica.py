
import asyncio

async def saludo():
    print ('hola')
    await asyncio.sleep(4)
    print('...mundo')

asyncio.run(saludo())
print('Fin del programa')

