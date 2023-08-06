import json
import os

class Prompter:
    def __init__(
        self,
        facts: list = [],
        fact_tag_filter: list = [],
        persona: str = "",
        task_parameters: dict = {},
        task_template: str = "",
    ):
        self.facts = facts
        self.fact_tag_filter = fact_tag_filter
        self.persona = persona
        self.task_parameters = task_parameters
        self.task_template = task_template

    def read_file_content(self,file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
        except Exception as e:
            print(f"Error occurred while reading file {file_path}: {str(e)}")
            return None

    def loadFactsFromFolder(self, folder: str):
        file_path = os.path.join("prompts/"+folder, "facts.json")
        self.facts = self.read_file_content(file_path)


    def getOpenAIPrompt(self):
        # filtered_facts = [
        #     fact for fact in self.facts if fact["tag"] in self.fact_tag_filter
        # ]

        return [
            {
                "role": "system",
                "content": self.persona,
            },
            {
                "role": "system",
                "content": f"---FACTS---\n{json.dumps(self.facts)}\n---END-FACTS---",
            },
            {
                "role": "user",
                "content": self.task_template.format(**self.task_parameters),
            },
        ]
