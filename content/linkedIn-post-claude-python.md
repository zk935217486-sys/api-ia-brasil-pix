# LinkedIn post - Claude API com Python

Quer montar um chatbot simples no terminal usando Claude API em Python?

O código base é menor do que parece:

```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["TOKEN_AI_API_KEY"])

print("Chat Claude. Digite 'sair' para encerrar.")

while True:
    prompt = input("Voce: ")

    if prompt.lower() == "sair":
        break

    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    print("Claude:", msg.content[0].text)
```

Passo a passo:

1. Instale o SDK:

```bash
pip install anthropic
```

2. Configure seu token.
3. Rode o script e teste prompts reais.

Para dev brasileiro, muitas vezes o problema não é integrar a API. É conseguir pagar sem cartão internacional, IOF no cartão e fatura em dólar.

No token ai, dá para testar com R$5 grátis, pagar via Pix e usar preço em Real.

Link: https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/claude-python-chatbot.html

#ClaudeAPI #PythonBrasil #APIClaudeBrasil #IAParaDevs #Pix #DevBrasil #TokenDeTesteGratis

