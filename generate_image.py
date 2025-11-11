
from openai import OpenAI

client = OpenAI(api_key="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")

def generate_image(prompt, output_path="generated.png"):
    response = client.images.generate(
        model="gpt-image-1",   # مولد صور خفيف وسريع
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = response.data[0].b64_json

    import base64
    image_bytes = base64.b64decode(image_base64)

    with open(output_path, "wb") as f:
        f.write(image_bytes)

    return output_path
