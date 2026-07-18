import requests

from config.settings import HF_API_URL, HEADERS


def call_model(model_name, payload):

    response = requests.post(
        f"{HF_API_URL}/{model_name}",
        headers=HEADERS,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    return response.json()