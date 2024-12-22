# import asyncio
from config import sdk

model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.5)
# result = model.run("расскажи что такое квадратный корень")
# async def message():
#     result = await model.run("расскажи что такое квадратный корень")
#     print( result.text)

# asyncio.run(message())
