import anthropic
from dotenv import load_dotenv
import os
from image_encoder import image_encoder

# Load env
load_dotenv()

# Claude client
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

# Image to base64
image = image_encoder('./Gigi-berlubang.jpeg')

print(image)

# Message hit
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Kamu adalah seorang AI dengan pengetahuan terkait kesehatan gigi dan mulut, untuk membantu pasien dalam berkonsultasi, serta membantu membuat anamnesa pasien"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Baik terimakasih"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Gigi saya kenapa ya?"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": "<base64_encoded_image>"
                    }
                }
            ]
        }
    ]
)

# Message output
print(message.content)