def clean_text(text):

    return text.strip()


def format_response(response):

    if isinstance(response, list):
        return response[0]

    return response


def validate_prompt(prompt):

    if not prompt.strip():
        raise ValueError("Digite um texto.")

    return True