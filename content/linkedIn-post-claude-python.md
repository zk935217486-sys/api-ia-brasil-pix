# LinkedIn post - Claude API barato com Python

Quer montar um chatbot simples no terminal usando Claude API em Python sem gastar token à toa?

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
3. Rode o script com prompts reais.
4. Meça tokens consumidos e custo por conversa.

Para dev brasileiro, muitas vezes o problema não é integrar a API. É manter Claude rodando todo dia sem o custo por token virar susto.

No token ai, dá para testar Claude com R$5 via suporte, pagar via Pix, usar saldo em Real e comparar o custo real antes de escalar.

Link: https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/claude-python-chatbot.html

#ClaudeAPI #PythonBrasil #ClaudeAPIBrasil #TokenIA #DevBrasil #Pix #IAParaDevs

