from datetime import datetime
import json
import os

class Files:

    def set_data(self, data):
        self.json_codding = json.dumps(data)

    def write_file(self, descriptor: str):

        try:
            with open(descriptor, "a+", encoding="utf-8") as file:
                file.write(self.json_codding)
            with open(descriptor, "a+", encoding="utf-8") as file:
                file.write("\n")

        except FileNotFoundError:
            print(f"--- Указан не корректный путь --- ❌")







    