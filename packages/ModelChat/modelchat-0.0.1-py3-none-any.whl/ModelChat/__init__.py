import requests

def simulate_conversation(model_name, token, prompt, user_intent, max_tokens):
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {token}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    payload = {
        "inputs": f"<|prompter|>{prompt}<|prompter|>{user_intent}<|endoftext|><|assistant|>",
        "parameters": {
            "max_new_tokens": max_tokens
        }
    }

    output = query(payload)
    output_text = output[0]['generated_text']
    response_text = output_text.split('<|assistant|>')[1].strip()
    return response_text