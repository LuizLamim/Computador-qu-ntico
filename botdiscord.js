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