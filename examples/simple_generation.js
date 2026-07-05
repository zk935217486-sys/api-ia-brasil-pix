import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.TOKEN_AI_API_KEY,
  // Veja seu endpoint/token no painel da token ai:
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

