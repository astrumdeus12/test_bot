from config import sdk

model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.5)
