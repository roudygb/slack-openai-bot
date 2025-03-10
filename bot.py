import os
from openai import OpenAI
from slack_bolt import App
from dotenv import load_dotenv

system_prompt =  '''
You are a helpful bot.
'''

load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

@app.event("app_mention")
def handle_mention(event, say):
    text = event["text"]
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": system_prompt
                    }
                ]
                },
                {"role": "user",
                "content": [{
                    "type": "text",
                    "text": text
                }]
                }
            ]
        )
        say(response.choices[0].message.content)
    except Exception as e:
        say(f"An error occurred: {e}")

@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    # currently a placeholder for other message workflows
    say(f"Hey there <@{message['user']}>!")


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
