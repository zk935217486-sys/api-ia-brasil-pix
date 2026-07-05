# [PT-BR] Tokens Codex e Claude baratos no Brasil

🇧🇷 Exemplos simples para devs brasileiros testarem Codex e Claude com menor custo por token, Pix e saldo em Real.

Este repositório mostra como criar chamadas básicas para Claude e Codex usando Python e JavaScript, com foco em quem está no Brasil e quer reduzir custo de consumo de token. Pix, Real e R$5 grátis ajudam no onboarding, mas o ponto principal é gastar menos por uso.

> Plataforma citada nos exemplos: [token ai](https://api.8uie.com/home)

Landing page em PT-BR: <https://zk935217486-sys.github.io/api-ia-brasil-pix/>

Guias rápidos:

- [Codex token barato no Brasil: como reduzir custo de uso](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/codex-token-barato-brasil.html)
- [Claude API barato Brasil: teste com saldo em Real](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/claude-api-barato-brasil.html)
- [Compra direta vs token ai: onde está a economia?](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/comparar-preco-openai-token-ai.html)
- [Quanto custa token de IA caro no Brasil?](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/iof-api-ia-brasil.html)
- [Como criar um chatbot Claude no terminal em Python](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/claude-python-chatbot.html)
- [Claude ou Codex: qual usar no seu projeto?](https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/codex-claude-brasil.html)

## Por que isso existe?

Muita gente no Brasil quer usar Codex e Claude em produto real, mas o consumo de token começa a pesar rápido:

- revisão de código consome contexto e várias rodadas;
- chatbot com Claude multiplica mensagens por usuário;
- análise de documentos usa contexto longo;
- preço por token vira custo recorrente;
- cartão internacional, dólar, IOF e spread ainda pioram a conta.

A proposta do [token ai](https://api.8uie.com/home) é vender consumo de tokens Codex e Claude com menor custo por uso para devs brasileiros. Pix, preço em Real, R$5 de teste grátis e suporte em português via Telegram reduzem a fricção de compra.

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

Os valores abaixo são conceituais. Confira sempre o preço ativo no painel, o modelo usado e seu volume antes de escalar.

| Cenário | Compra direta | token ai |
|---|---:|---:|
| Foco | Preço oficial + cobrança internacional | Menor custo por token |
| Moeda | Geralmente USD | BRL |
| Pagamento | Cartão internacional | Pix |
| Controle | Fatura depois | Saldo antes de usar |
| Teste grátis | Depende da plataforma | R$5 grátis |
| Suporte | Global/genérico | Português via TG |

## Quando faz sentido usar?

- Você procura Codex token barato para revisar código sem estourar orçamento.
- Você quer Claude API barato Brasil para chatbot, resumo ou análise.
- Você quer comprar token IA com Pix e saldo em Real.
- Você quer comparar custo por tarefa antes de escalar.
- Você precisa de uma alternativa barata para API de IA com onboarding simples.

## FAQ

### Isso substitui documentação oficial?

Não. A documentação oficial continua sendo a referência técnica principal. Este repositório é um guia prático para dev brasileiro começar rápido.

### Posso usar em produção?

Use primeiro o crédito de teste, valide latência, limites, custo e estabilidade para o seu caso. Depois escale com monitoramento de uso.

### Preciso de cartão internacional?

Na proposta do [token ai](https://api.8uie.com/home), não. O fluxo é Pix, saldo em Real e consumo de tokens.

### Tem teste grátis?

Sim. A plataforma oferece R$5 de token de teste grátis para validar custo, qualidade e latência antes de colocar crédito.

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

- [Post LinkedIn sobre custo mensal de token](content/linkedIn-post-iof.md)
- [Post LinkedIn sobre Codex e Claude token barato](content/linkedIn-post-token-barato.md)
- [Post LinkedIn sobre Claude API com Python](content/linkedIn-post-claude-python.md)
- [Fila de publicação PT-BR](content/publication-queue.md)

## Links úteis

- Plataforma: <https://api.8uie.com/home>
- Landing page: <https://zk935217486-sys.github.io/api-ia-brasil-pix/>
- Palavra-chave: Codex token barato
- Palavra-chave: Claude API barato Brasil
- Palavra-chave: token IA barato Brasil
- Palavra-chave: alternativa barata OpenAI API
- Palavra-chave: comprar token Claude barato
- Palavra-chave: comprar token Codex com Pix
- Palavra-chave: comprar token IA com Pix
- Palavra-chave: saldo API IA com Pix

## Curtiu?

Deixe uma star no repositório para ajudar outros devs brasileiros a encontrarem este guia.
