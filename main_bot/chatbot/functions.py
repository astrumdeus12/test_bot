from .settings import model

def format_text_for_telegram(text):
    text = text.replace('$', '*')
    text = text.replace('\\cdot', '*')
    text = text.replace('\\\\', '\\')
    return text



def get_bot_answer(message : str):
    answer_object = model.run(message)
    answer = answer_object.alternatives[0].text
    result = format_text_for_telegram(answer)
    return result



