# import os
# from dotenv import load_dotenv
# from agents import Runner, Agent , OpenAIChatCompletionsModel, handoff
# from openai import AsyncOpenAI
# from agents.run import RunConfig 
# from tools_needed import roll_dice , generate_event

# load_dotenv()
# openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# client = AsyncOpenAI(
#     api_key = openrouter_api_key,
#     base_url="https://openrouter.ai/api/v1"
# )


# model_ai = OpenAIChatCompletionsModel(
#     model = "openai/gpt-3.5-turbo",
#     openai_client = client,
# )

# config = RunConfig(
#     model = model_ai,
#     tracing_disabled= True,
# )


# monster_agent = Agent(
#     name= "monster agent",
#     instructions="Your role is to handle monster encounters using `roll_dice` and `generate_event`",
#     model= model_ai,
#     tools=[roll_dice , generate_event]
# )

# item_agent = Agent(
#     name = "item agent",
#     instructions= "you provide the player with rewards and prizes",
#     model= model_ai
# )


# narrator_agent = Agent(
#     name = "narrator",
#     instructions="You are the narrator of a text-based adventure game. You will describe the world, characters, and events to the player. Your responses should be vivid and engaging, setting the scene for the player.",
#     model = model_ai,
#     handoffs=[
#         handoff(agent = monster_agent),
#         handoff(agent=item_agent)
#     ]
# )


# def main():
#     print("Welcome to Fantasy Games🎲🎮")

#     choice = input("Would you enter the forest or turn back?")

#     result_1 = Runner.run_sync(narrator_agent,choice,run_config=config)
#     print("\n STORY:" , result_1.final_output)

#     result_2 = Runner.run_sync(monster_agent, "Start Encounter" ,run_config=config)
#     print("\n ENCOUNTER:" , result_2.final_output)

#     result_3 = Runner.run_sync(item_agent, "Give Rewards" ,run_config=config)
#     print("\n REWARD AND PRIZE" , result_3.final_output)

# if __name__ == "__main__":
#     main()




import os
from dotenv import load_dotenv
from agents import Runner, Agent, OpenAIChatCompletionsModel, handoff
from openai import AsyncOpenAI
from agents.run import RunConfig
from tools_needed import roll_dice, generate_event

# Load API key
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter client
client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Model
model_ai = OpenAIChatCompletionsModel(
    model="openai/gpt-3.5-turbo",
    openai_client=client,
)


config = RunConfig(
    model=model_ai,
    tracing_disabled=True,
)


item_agent = Agent(
    name="item agent",
    instructions="You provide the player with rewards and prizes after defeating a monster.",
    model=model_ai
)

monster_agent = Agent(
    name="monster agent",
    instructions="Your role is to handle monster encounters using `roll_dice` and `generate_event`.",
    model=model_ai,
    tools=[roll_dice, generate_event],
    handoffs=[
        handoff(agent=item_agent)  
    ]
)

narrator_agent = Agent(
    name="narrator",
    instructions=(
        "You are the narrator of a text-based adventure game. "
        "You will describe the world, characters, and events to the player. "
        "If the player enters the forest, hand off to the monster agent."
    ),
    model=model_ai,
    handoffs=[
        handoff(agent=monster_agent)
    ]
)

def main():
    print("Welcome to Fantasy Games 🎲🎮")
    choice = input("Would you enter the forest or turn back? ")
    if choice.lower() == "turn back":
        print("You chose to turn back. Game over.")
        return

    current_agent = narrator_agent
    user_input = choice

    while True:
        result = Runner.run_sync(
            starting_agent=current_agent,
            input=user_input,
            run_config=config
        )
        print("\nRESULT:", result.final_output)

        # Ask for next move
        user_input = input("\nYour move (or type 'quit' to end): ")
        if user_input.lower() == "quit":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()
