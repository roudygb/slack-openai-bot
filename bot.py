import os
from typing import List
from openai import OpenAI
from slack_bolt import App
from dotenv import load_dotenv
from openai.types.responses.response_output_message import ResponseOutputMessage

load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
INSTRUCTIONS =  os.environ.get("INSTRUCTIONS")

client = OpenAI(api_key=OPENAI_API_KEY)
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

def process_response_output(output: List) -> str:
    for response_object in output:
        if type(response_object) == ResponseOutputMessage:
            return response_object.content[0].text

@app.event("app_mention")
def handle_mention(event, say):
    text_input = event["text"]
    try:
        response = client.responses.create(
            model="gpt-4o",
            tools=[{"type": "web_search_preview"}],
            tool_choice="auto",
            input=text_input,
            instructions=INSTRUCTIONS
        )
        say(process_response_output(response.output))
    except Exception as e:
        say(f"An error occurred: {e}")

if __name__ == "__main__":
   print("⚡️ Starting Slack bot...")
   app.start(port=int(os.environ.get("PORT", 8080)))