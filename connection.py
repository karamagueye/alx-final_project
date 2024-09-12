import discord

# Créer un objet Intents avec tous les intents activés (vous pouvez personnaliser en fonction des besoins)
intents = discord.Intents.default()
intents.message_content = True  # Assurez-vous que cette ligne est présente si vous voulez que le bot puisse lire les messages

# Créer le client Discord avec les intents
client = discord.Client(intents=intents)

client.run(TOKEN")
