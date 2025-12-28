const { Client, GatewayIntentBits } = require('discord.js');
require('dotenv').config();

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,           // Para interagir com servidores
        GatewayIntentBits.GuildMessages,    // Para ver mensagens
        GatewayIntentBits.MessageContent    // Para ler o conteúdo das mensagens
    ]
});

client.once('ready', () => {
    console.log(`✅ Bot online como: ${client.user.tag}`);
});

client.on('messageCreate', (message) => {
    // Evita que o bot responda a si mesmo ou a outros bots
    if (message.author.bot) return;

    // Comando básico: !ping
    if (message.content === '!ping') {
        message.reply('Pong! 🏓');
    }

    // Comando básico: !ola
    if (message.content.toLowerCase() === '!ola') {
        message.channel.send(`Olá, ${message.author.username}! Tudo bem?`);
    }
});

// Faz o login do bot usando o token do arquivo .env
client.login(process.env.TOKEN);