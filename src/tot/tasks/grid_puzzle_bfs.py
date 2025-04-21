
import re 
import os
import sympy
import pandas as pd
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.gridpuzzle import * 


class GridPuzzle(Task):


    def __init__(self, file = 'GridPuzzle.csv',  start=1, end=200):

        super().__init__()
        path = os.path.join(DATA_PATH, 'gridpuzzle', file)
        self.value_cache = {}
        self.steps = 8
        self.stops = ['\n']*4
        df = pd.read_csv(path)
        
        if end is None:
            end = len(df)

        self.questions = df['question'].tolist()[start:end]
        self.answers = df['answer'].tolist()[start:end]
        self.value_cache = {}
        self.steps = 4
        self.stops = ['Final Answer:']
        self.start = start
        self.end = end

    def __len__(self):
        return len(self.questions)

    def get_input(self, idx: int) -> str:
        return self.questions[idx]

    import re
    def parse_output(self, string1):
        ls = []
        for line in string1.strip().split('\n'):
                if '|' in line:
                    parts = [n.strip() for n in line.split('|')]
                    if len(parts) == 3 or len(parts) == 4:
                        ls.append(tuple(parts))
        return ls
    
    @staticmethod
    def extract_answer_table(text: str):
        """
        Extracts the final answer table regardless of formatting:
        - Handles with or without code block (```).
        - Accepts extra spaces, inconsistent alignment.
        - Returns sorted list of (score, name, institution).
        """
        print("text",text)
        # Capture everything after 'Final Answer:'
        after_final_answer = text.split('Final Answer:')[-1]

        # Pattern to match lines like: 55% | Name | Institution
        pattern = r'(\d{2,3}%)\s*\|\s*([^\|]+?)\s*\|\s*([^\n\r`]+)'

        # Find all matches
        matches = re.findall(pattern, after_final_answer)
        print(matches)

        # Normalize and return
        return sorted([tuple(map(str.strip, match)) for match in matches])

    def test_output(self, idx: int, output: str):
        try:
            print("###############")
            print("output", output)
            print("final answer", self.extract_answer_table(output))
            print("Ground truth", self.answers[idx])

            pred = self.extract_answer_table(output)
            gt = self.parse_output(self.answers[idx])

            r = int(sorted(pred) == sorted(gt))
            print("value of ", r)
            return {'r': r}
        except:
            return {'r': 0}


    @staticmethod
    def standard_prompt_wrap(x: str, y: str = '') -> str:
        return standard_prompt.format(input=x) + y


    @staticmethod
    def cot_prompt_wrap(x: str, y: str = '') -> str:
        return cot_prompt.format(input=x) + y
    

    @staticmethod
    def propose_prompt_wrap(x: str, y: str = '') -> str:
        """
        Wraps the current partial grid state into a propose-style prompt.
        If solution is not yet fully assigned, ask the LLM to propose next thoughts.
        """
        # If current state has fewer than 4 lines, it's still partial
        num_lines = len([line for line in y.strip().split('\n') if line.strip()])
        if num_lines < 4:
            prompt = propose_prompt.format(current=y.strip(), input=x.strip())
        else:
            prompt = value_last_step_prompt.format(your_solution=y.strip())
        print("propose prompt", prompt)
        return prompt


    @staticmethod
    def value_prompt_wrap(x: str, y: str) -> str:
        """
        If the solution is complete (all rows filled), use value_last_step_prompt to validate.
        Otherwise, this could call a different prompt for scoring intermediate steps (not always needed for grid puzzles).
        """
        num_lines = len([line for line in y.strip().split('\n') if line.strip()])
        if num_lines < 4:
            return value_prompt.format(input=x)
        return value_last_step_prompt.format(input=x,answer=y.strip())

    @staticmethod
    def value_outputs_unwrap(x: str, y: str, value_outputs: list) -> float:
        value_names = [_.strip().lower() for _ in value_outputs]
        value_map = {'incorrect': 0.01, 'partial': 1, 'correct': 20}
        return sum(value_map.get(name, 0) for name in value_names)

'''
task = GridPuzzle(file='GridPuzzle.csv', start=0, end=None)
print(task.get_input(5))
print(task.__len__())
'''