# Ruina-v2-Text-generation-image



Ruina-v2-Text-generation-image is a telegram chatbot based on chatGPT from openai and have image generation feature dall-E




## Installation

install the required libraries






See the [OpenAI API docs.](https://beta.openai.com/docs/api-reference?lang=python)


```bash
pip install -r requirements.txt
```

The library needs to be configured with your account's secret key which is available on the [Website](https://beta.openai.com/account/api-keys).

add your secret key at 

```bash
import openai
openai.api_key = "Openai-key"
```

to get the telegram secret key you can see the tutorial 

add your telegram secret key at 

```bash
api = 'telegrambot-key'
bot = telebot.TeleBot(api)
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/domswp/Ruina-v2-Text-generation-Image-.git
```

Go to the project directory

```bash
  cd Ruina-v2-generation-Image
```

Start the program

```bash
  python main.py
```


