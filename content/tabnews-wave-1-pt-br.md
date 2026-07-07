# Pack TabNews - onda 1

Objetivo: entrar em TabNews com posts úteis, anti-marketing e centrados em custo real para dev brasileiro.

## Post 1 - Calculadora de custo em BRL

Título:

`Fiz uma calculadora para comparar custo de Claude/Codex em BRL com câmbio, IOF e Pix`

Texto:

Quase toda discussão sobre API de IA no Brasil vira:

- "qual modelo é melhor?"
- "qual API é mais barata?"

Mas para quem paga com cartão internacional, a conta real passa por:

- preço por token
- câmbio
- IOF
- spread
- custo por tarefa

Então eu montei uma calculadora simples para comparar compra internacional com saldo em BRL/Pix:

https://zk935217486-sys.github.io/api-ia-brasil-pix/ferramentas/calculadora-custo-codex-claude.html

A ideia não é vender "a chamada mais barata". É medir:

- quanto custa revisar PR com Codex
- quanto custa chatbot com Claude
- quanto custa resumo em lote

Se alguém quiser, eu também posso postar uma versão com cenários prontos para code review e chatbot.

## Post 2 - Sem cartão internacional

Título:

`Para muito dev brasileiro, o problema de testar Claude não é técnico. É cartão internacional.`

Texto:

Tem muito teste pequeno que nem começa porque a parte chata entra antes:

- cartão internacional
- fatura em dólar
- spread
- IOF
- limite

Quando a pessoa ainda está validando produto, isso já cria atrito demais.

Escrevi um guia direto sobre esse ponto:

https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/api-claude-sem-cartao-internacional.html

Curiosidade: em vários fluxos, o que o time queria não era "mais um modelo". Era só um jeito previsível de testar custo em BRL.

## Post 3 - Code review com custo real

Título:

`Codex para code review: a pergunta certa não é “funciona?”, é “quanto custa por PR?”`

Texto:

Se você mede Codex com prompt curto, a conta engana.

O uso real costuma ter:

- diff maior
- contexto do repo
- mais de uma tentativa
- testes sugeridos
- comentários de risco

Por isso eu prefiro medir custo por PR.

Montei este guia:

https://zk935217486-sys.github.io/api-ia-brasil-pix/artigos/codex-code-review-barato.html

Se alguém usa isso em time, eu queria muito saber qual métrica acompanhou:

- custo por PR
- tempo poupado
- qualidade da revisão
- latência
