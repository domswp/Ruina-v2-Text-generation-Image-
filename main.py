import telebot
from telebot import types
import openai
import requests

openai.api_key = "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"
api = '1056639370:AAEZQt9uU2ZYJaRJOOi5NEFo_8RzYzJVwqM'
bot = telebot.TeleBot(api)

def generate_image(prompt):
    model = "image-alpha-001"
    url = "https://api.openai.com/v1/images/generations"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {openai.api_key}"}
    data = """
    {
        """
    data += f'"model": "{model}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"256x256",
        "response_format":"url"
    }
    """
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    return response_json["data"][0]["url"]

def rsp(question):
    prmt = "Q: {qst}\nA:".format(qst=question)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prmt,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text

@bot.message_handler(commands=['generate_image'])
def handle_generate_image(message):
    # get the user's message and use it as the prompt for the image generation function
    prompt = message.text[len('/generate_image'):].strip()
    image_url = generate_image(prompt)
    
    # send the generated image
    bot.send_photo(message.chat.id, image_url)

@bot.message_handler(commands=['ask'])
def handle_ask(message):
    # get the user's message and use it to generate a response
    question = message.text[len('/ask'):].strip()
    response = rsp(question)
    
    # send the response
    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: True) 
def echo_message(message):
    bot.send_message(message.chat.id, "Maaf, perintah yang Anda berikan tidak dapat dipahami. Gunakan perintah /ask diikuti dengan pertanyaan untuk mendapatkan jawaban atau perintah /generate_image diikuti dengan prompt untuk membuat sebuah gambar.")
    
print('bot start running')
bot.polling()