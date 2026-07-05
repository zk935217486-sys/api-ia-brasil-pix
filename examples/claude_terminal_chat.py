import os
from anthropic import Anthropic


def main():
    client = Anthropic(
        api_key=os.environ["TOKEN_AI_API_KEY"],
        # Veja seu endpoint/token no painel da token ai:
        # https://api.8uie.com/home
    )

    print("Chat Claude no terminal. Digite 'sair' para encerrar.")

    while True:
        prompt = input("Voce: ")

        if prompt.strip().lower() == "sair":
            break

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )

        print("Claude:", message.content[0].text)


if __name__ == "__main__":
    main()

