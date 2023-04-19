import asyncio
import aioschedule


async def sayHello():
    print("Hey! My name is John Doe")


async def scheduler():
    aioschedule.every().saturday.at("15:00").do(sayHello)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
