from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
def gerar_texto(prompt):
    cliente = InferenceClient(
        model="Qwen/Qwen2.5-7B-Instruct",
    
    )

    resposta = cliente.chat_completion(
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=512
    )

    return resposta.choices[0].message.content