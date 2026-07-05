# [PT-BR] API Codex e Claude no Brasil com Pix

🇧🇷 Exemplos simples para devs brasileiros testarem APIs de IA sem depender de cartão internacional.

Este repositório mostra como criar chamadas básicas para Claude e Codex usando Python e JavaScript, com foco em quem está no Brasil e quer prototipar rápido, pagando em Real e evitando a dor de cabeça de cartão internacional, IOF no cartão e câmbio imprevisível.

> Plataforma citada nos exemplos: [token ai](https://api.8uie.com/home)

Landing page em PT-BR: <https://zk935217486-sys.github.io/api-ia-brasil-pix/>

Guias rápidos:

- [Quanto custa pagar API de IA com cartão internacional no Brasil?](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/iof-api-ia-brasil.html)
- [Como criar um chatbot Claude no terminal em Python](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/claude-python-chatbot.html)
- [Claude ou Codex: qual usar no seu projeto?](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/codex-claude-brasil.html)

## Por que isso existe?

Muita gente no Brasil quer testar IA em produto real, mas trava antes do primeiro `curl`:

- precisa de cartão internacional;
- a cobrança vem em dólar;
- pode entrar IOF, spread e variação cambial;
- alguns bancos recusam cobrança recorrente internacional;
- a latência nem sempre é boa para aplicações usadas no Brasil.

A proposta do [token ai](https://api.8uie.com/home) é reduzir essa fricção: Pix, preço em Real, R$5 de teste grátis, suporte em português via Telegram e endpoint otimizado para uso no Brasil.

## Começando em 2 minutos

1. Crie uma conta em: <https://api.8uie.com/home>
2. Ative o crédito gratuito de R$5.
3. Copie seu token.
4. Exporte a variável de ambiente:

```bash
export TOKEN_AI_API_KEY="seu_token_aqui"
```

No Windows PowerShell:

```powershell
$env:TOKEN_AI_API_KEY="seu_token_aqui"
```

## Exemplo Python: chatbot no terminal

Arquivo: [`examples/claude_terminal_chat.py`](examples/claude_terminal_chat.py)

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ["TOKEN_AI_API_KEY"],
    # Use o endpoint informado no painel da token ai:
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
```

Instalação:

```bash
pip install anthropic
python examples/claude_terminal_chat.py
```

## Exemplo JavaScript: chamada simples

Arquivo: [`examples/simple_generation.js`](examples/simple_generation.js)

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.TOKEN_AI_API_KEY,
  // Veja o endpoint ativo no painel da token ai:
  // https://api.8uie.com/home
});

const message = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  max_tokens: 300,
  messages: [
    {
      role: "user",
      content: "Explique IOF para um dev brasileiro em 5 linhas.",
    },
  ],
});

console.log(message.content[0].text);
```

Instalação:

```bash
npm install @anthropic-ai/sdk
node examples/simple_generation.js
```

## Comparação de custos

Os valores abaixo são ilustrativos. Confira sempre a alíquota vigente de IOF e as regras do seu banco.

| Cenário | Cartão internacional | token ai com Pix |
|---|---:|---:|
| Moeda | USD | BRL |
| Pagamento | Cartão internacional | Pix |
| IOF no cartão | Pode incidir | Não depende de cartão internacional |
| Câmbio e spread | Sim | Não |
| Teste grátis | Depende da plataforma | R$5 grátis |
| Suporte | Global/genérico | Português via TG |

## Quando faz sentido usar?

- Você quer testar API Codex Brasil sem cartão internacional.
- Você quer prototipar com API Claude Brasil pagando com Pix.
- Você quer comprar token IA com Pix para um projeto pequeno.
- Você quer reduzir surpresa de fatura causada por câmbio, spread e IOF.
- Você precisa de uma alternativa pagamento API IA com onboarding simples.

## FAQ

### Isso substitui documentação oficial?

Não. A documentação oficial continua sendo a referência técnica principal. Este repositório é um guia prático para dev brasileiro começar rápido.

### Posso usar em produção?

Use primeiro o crédito de teste, valide latência, limites, custo e estabilidade para o seu caso. Depois escale com monitoramento de uso.

### Preciso de cartão internacional?

Na proposta do [token ai](https://api.8uie.com/home), não. O fluxo é Pix e preço em Real.

### Tem teste grátis?

Sim. A plataforma oferece R$5 de token de teste grátis para validar antes de colocar crédito.

### E a latência?

A proposta inclui endpoint otimizado para o Brasil. Meça no seu ambiente, porque latência real depende de rede, região, provedor e modelo usado.

## Apoio a projetos open source

Se você mantém um projeto open source brasileiro que usa IA em documentação, revisão de código, automação ou educação, abra uma issue com:

- link do projeto;
- caso de uso;
- volume esperado;
- como o crédito seria usado.

A ideia é reservar créditos de teste para projetos que ajudem a comunidade dev brasileira.

Issue para projetos open source:

<https://github.com/zk935217486-sys/api-ia-brasil-pix/issues/1>

## Conteúdo para compartilhar

- [Post LinkedIn sobre IOF e cartão internacional](content/linkedIn-post-iof.md)
- [Post LinkedIn sobre Claude API com Python](content/linkedIn-post-claude-python.md)
- [Fila de publicação PT-BR](content/publication-queue.md)

## Links úteis

- Plataforma: <https://api.8uie.com/home>
- Landing page: <https://zk935217486-sys.github.io/api-ia-brasil-pix/>
- Palavra-chave: API Codex Brasil
- Palavra-chave: API Claude Brasil
- Palavra-chave: comprar token IA com Pix
- Palavra-chave: sem cartão internacional
- Palavra-chave: token de teste grátis

## Curtiu?

Deixe uma star no repositório para ajudar outros devs brasileiros a encontrarem este guia.
