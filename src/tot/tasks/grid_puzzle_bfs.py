
import re 
import os
import sympy
import pandas as pd
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.game24 import * 


class GridPuzzle(Task):


    def __init__(self, file = 'GridPuzzle.csv'):

        super().__init__()
        path = os.path.join(DATA_PATH, 'gridpuzzle', file)
        self.data = list(pd.read_csv(path)['question'])
        self.value_cache = {}
        self.steps = 8
        self.stops = ['\n']*4

    def __len__(self) -> int:
        return len(self.data)

    def get_input(self, idx:int) -> str:
        return self.data[idx]
    
    def parse_output(string1):
        ls = []
        for line in string1.split('\n'):
            ls.append([n.strip() for n in line.split('|')])
        return ls

    def test_output(self, idx:int, output:str):
        answer = self.data[idx]['answer']
        print("output by llm", output)
        print("actual answer", answer)
        return parse_output(answer) == parse_output(output)