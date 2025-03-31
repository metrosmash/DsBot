# Discord Bot

A Discord bot built using the Discord.py library. This bot provides various features and commands for server management, entertainment, and more.

## Features

- Moderation commands (kick, ban, mute, etc.)
- Fun commands (jokes, memes, etc.)
- Utility commands (server info, user info, etc.)
- Customizable prefix for commands

## Getting Started

These instructions will help you set up and run the bot on your local machine.

### Prerequisites

- python3
- discord py 
- Discord account and a server where you have permission to add a bot

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/metrosmash/DsBot
   cd DsBot
   ```

2. Install the required dependencies:
   ```bash
   pip install discord.py
   ```

3. Create a `.env` file in the root directory and add the following:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   PREFIX=!
   ```

4. Run the bot:
   ```bash
   python main.py 
   ```

## Usage

Once the bot is running, you can use the following commands:

- `$guess` - starts a guess game with the bot
- `$rank_selection` - starts a rank selection game with another user.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Discord.py](https://discordpy.readthedocs.io/en/stable/) - A powerful library for interacting with the Discord API
