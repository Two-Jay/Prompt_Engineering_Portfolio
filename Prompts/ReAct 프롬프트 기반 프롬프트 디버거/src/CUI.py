from abc import ABC, abstractmethod
from openai import OpenAI
from typing import List
import os
import converter
import json
import platform

# ANSI 색상 코드
colors = {
    'thought': '\033[91m',  # 빨강
    'decision': '\033[92m',  # 녹색
    'action': '\033[94m',  # 파랑
    'response': '\033[96m',  # 시안
    'reset': '\033[0m'  # 리셋
}

class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass

class Flushable(ABC):
    @abstractmethod
    def flush(self):
        pass

class Messages(Flushable):
    def __init__(self, memory_limits = 30):
        self.memory = []
        self.memory_limits = memory_limits

    def flush(self):
        if len(self.memory) < 0:
            raise Exception("Messages is empty")
        self.memory = [self.memory[0]] # remains it's system_prompt
    
    def insert(self, text, role=None):
        if role not in ["user", "assistant", "system"]:
            role = "assistant"
        self.memory.append({"role": role, "content": text})
        if len(self.memory) > self.memory_limits:
            self.flush()

    def get(self):
        return self.memory

class GPT_CUI(Runnable):
    def __init__(self,
            memory_limits = 30,
            gpt : OpenAI = None,
            exit_commants : List[str]= ["exit", "quit", "bye"],
            assistant_name = "assistant",
            hyperparameters = {},
            debug = False,
            debug_mode = "react"
        ):
        self.memory = Messages(memory_limits)
        if debug and hyperparameters.get("max_tokens") > 100:
            hyperparameters["max_tokens"] += 200
        self.caller = Caller(gpt, hyperparameters, assistant_name)
        self.exit_commants = exit_commants
        self.assistant_name = assistant_name
        self.debug_params = {
            "is_debug_mode": debug,
            "mode": debug_mode
        }

    
    def init_system_prompt(self, system_prompt):
        self.memory.insert(system_prompt, "system")

    def run(self, chatbot_first = False):
        while True:
            if chatbot_first:
                inference_result = self.caller.call(self.memory.get(), self.debug_params.get("is_debug_mode"), self.debug_params.get("mode"))
                self.memory.insert(inference_result)
                chatbot_first = False
            user_input = self.get_userInput()
            if user_input in self.exit_commants:
                break
            inference_result = self.caller.call(self.memory.get(), self.debug_params.get("is_debug_mode"), self.debug_params.get("mode"))
            self.memory.insert(inference_result, self.assistant_name)

    def get_userInput(self):
        user_input = input("You: ")
        self.memory.insert(user_input, "user")
        return user_input

class Caller():
    def __init__(self, gpt: OpenAI, hyperparameters = {}, caller_name = "GPT"):
        self.gpt = gpt
        self.hyperparameters = hyperparameters
        self.caller_name = caller_name

    def inference(self, messages, debug = False, debug_mode = "react"):
        if debug and debug_mode == "react":
            return gpt_inference_react(self.gpt, self.hyperparameters, messages)
        else:
            return gpt_inference_normal(self.gpt, self.hyperparameters, messages)
    
    def call(self, messages, debug = False, debug_mode = "react"):
        response_content = self.inference(messages, debug, debug_mode)
        if not debug:
            print(f"{self.caller_name} : {response_content}")
        else:
            print(f"{response_content}")
        return response_content
    

def gpt_inference_normal(gpt : OpenAI, hyperparameters : dict, messages):
    response = gpt.chat.completions.create(
        **hyperparameters,
        messages=messages
    )
    return response.choices[0].message.content

react_response_scheme = {
    "type": "object",
    "properties": {
        "thought": {
            "type": "string",
            "description": "what you think about user request."
        },
        "decision": {
            "type": "string",
            "description": "what you decide about what you think."
        },
        "action": {
            "type": "string",
            "description": "what you do about what you decide."
        },
        "response": {
            "type": "string",
            "description": "what you say about what you do."
        }
    },
    "required": ["thought", "decision", "action", "response"]
}

react_fuction_param =[{
    "name": "inspect",
    "description": converter.load(os.getcwd() + '/resources/prompt', "ReAct.md", converter.FileType.FILE),
    "parameters": react_response_scheme
}]

def gpt_inference_react(gpt : OpenAI, hyperparameters : dict, messages, pretty = True):
    response = gpt.chat.completions.create(
        **hyperparameters,
        messages=messages,
        functions = react_fuction_param,
        function_call = {
            "name" : "inspect"
        },
    )
    if pretty:
        return pretty_callback(response.choices[0].message.function_call.arguments)
    return response.choices[0].message.function_call.arguments

def pretty_callback(json_string):
    data = json.loads(json_string)
    if platform.system() is not "Windows":
        for key, value in data.items():
            color = colors.get(key, colors['reset'])
            data[key] = f"{color}{value}{colors['reset']}"
    return json.dumps(data, indent=4)