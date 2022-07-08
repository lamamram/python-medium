# %%
import asyncio


async def say_after(msg, timeout=3):
    await asyncio.sleep(timeout)
    print(msg)

async def main(aw):
    await asyncio.gather(
        # les objets coroutines sont consommés par await
        # non réutilisables
        aw,
        say_after("hi", 1))
    
    for f in asyncio.as_completed([say_after("hello"), say_after("hi", 1)]):
        await f
    
# l'appel renvoit l'objet coroutine
aw = say_after("hello")
asyncio.run(main(aw))
# %%
