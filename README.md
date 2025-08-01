🎮 Game Master Agent — Fantasy Adventure Game
Welcome to Fantasy Games, a text-based adventure powered by OpenAI Agent SDK and multi-agent handoff. This project is a small yet powerful demonstration of how to combine narrative storytelling, combat mechanics, and reward logic using AI agents and tools like dice rolls and random events.

✨ Features
🧙 NarratorAgent: Sets the scene and drives the story forward.

🐉 MonsterAgent: Simulates battles using dice and random encounters.

💎 ItemAgent: Grants rewards and handles inventory logic.

🎲 Tools: roll_dice() and generate_event() to simulate gameplay unpredictability.

⚙️ Multi-agent orchestration using OpenAI's Agent SDK and OpenRouter-compatible models.

🧠 How It Works
The game flow includes:

NarratorAgent paints the scene based on the player's first input.

MonsterAgent takes over during a combat encounter using tool access.

ItemAgent rewards the player at the end of the turn.

Each agent uses the same model with different instructions and (optionally) tools.

