import asyncio 


async def get_data(): 
    await asyncio.sleep(2)  
    print("data")


async def main(): 
    task = asyncio.create_task(get_data())
    print("hello")


asyncio.run(main())


"""
    async operation in python creates coroutine object (not promise)
"""