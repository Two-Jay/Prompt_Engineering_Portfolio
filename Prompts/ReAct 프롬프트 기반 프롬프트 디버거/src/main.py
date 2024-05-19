from CUI import GPT_CUI as ChattingBox
from openai import OpenAI
from converter import load_injected_prompt, load, FileType, load_debug_prompt
import os
import signal
import argparse

def read_dotenv():
    envs = {}
    with open(f"{os.getcwd()}/.env", "r") as f:
        for line in f:
            if line[0] == "#":
                continue
            key, value = line.split("=")
            envs[key] = value
    return envs

def signal_handler(sig, frame):
    if sig == signal.SIGINT:
        print("Exiting...")
        exit(0)

def main(args):
    signal.signal(signal.SIGINT, signal_handler)
    prompt = load_injected_prompt(os.getcwd() + "/resources/prompt")
    if args.debug == True:
        print("Debug mode")

    hyperparameters = load(os.getcwd() + '/resources/hyperparameter', "hyperparameters.json",  FileType.JSON)
    envs = read_dotenv()
    
    gpt = OpenAI(api_key=envs["API_KEY"])

    chatbot = ChattingBox(
        gpt=gpt,
        assistant_name="Ve-sta",
        hyperparameters=hyperparameters,
        debug=args.debug,
    )
    if args.verbose:
        print(f'{prompt}\n===========================================================')
    chatbot.init_system_prompt(prompt)
    chatbot.run(chatbot_first=True)

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--debug", action="store_true")
    argparse.add_argument("--verbose", action="store_true", help="Prints the final system prompt.")
    args = argparse.parse_args()
    main(args)