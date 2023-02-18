import json
from revChatGPT.V1 import Chatbot

class ChatModel:
    isCreated = False
    prev_text = ""
    respond = ""
    chatbot = None

    def __init__(self):
        pass

    def create(self):
        with open("assets/config.json") as config_file:
            config = json.load(config_file)
        print("init ChatGPT...")
        print(f"detect config.json:\n{config}")
        self.chatbot = Chatbot(config)
        self.isCreated = True

    def query(self, question):
        # validation
        if not self.isCreated:
            self.create()
        # begin chat
        print(f"User:\t{question}")
        print("ChatGPT:", end="\t")
        self.respond = ""

        for data in self.chatbot.ask(
                question,
        ):
            message = data["message"][len(self.prev_text):]
            self.respond += message
            print(message, end="", flush=True)
            self.prev_text = data["message"]
        return self.respond

    def clear(self):
        pass
