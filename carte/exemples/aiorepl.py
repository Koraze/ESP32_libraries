# Installez d'abord les éléments suivants
# import mip
# mip.install("github:Koraze/ESP32_libraries/mip/deps/aiorepl.json")
# 
# Pour plus d'informations :
# - https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl
# - https://docs.micropython.org/en/latest/library/asyncio.html 


# libraries
import asyncio
import deps.aiorepl as aiorepl


async def task1():
    while True:
        await asyncio.sleep_ms(500)


async def main():
    print("Starting tasks...")

    t1 = asyncio.create_task(task1())            # Start other program tasks.
    repl = asyncio.create_task(aiorepl.task())   # Start the aiorepl task.

    await asyncio.gather(t1, repl)


asyncio.run(main())
