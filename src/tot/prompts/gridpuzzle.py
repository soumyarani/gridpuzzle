# 5 shot
standard_prompt = '''
Solve 4x3 grid world puzzle. Given an input of values and clues , generate an output of 4 rows, where each row has one option from data, separated by space.

Input:
"Nicholas and Edith are having a small dinner party this evening at their home in Cedar Valley, and they've decided to open a select number of rare wines from their personal collection to celebrate the occasion. Using only the clues below, match the vintages to the options from wines and types. Remember, as with all grid-based logic puzzles, no option in any category will ever be used more than once.
vintages : 1984, 1988, 1992, 1996.
wines : Annata Branco, Bianca Flaux, Ece Suss, Vendemmia.
types : gewurztraminer, merlot, pinot noir, riesling.

Clues:
1. The Ece Suss was bottled sometime after the Annata Branco.
2. The Bianca Flaux was bottled 4 years before the Vendemmia.
3. The 1988 bottle is a pinot noir.
4. The merlot is either the Annata Branco or the Bianca Flaux.
5. The Bianca Flaux was bottled sometime after the Ece Suss.
6. The 1984 bottle is a gewurztraminer.

While answering use the following format:
Step-by-step solution:
Your steps showing how you are solving the puzzle

Final Answer:
Fill the following table to show your final answer.
1984 | correct option from wines | correct option from types
1988 | correct option from wines | correct option from types
1992 | correct option from wines | correct option from types
1996 | correct option from wines | correct option from types


Step-by-step solution:
 1. From clue 6, we know that the 1984 bottle is a gewurztraminer.
    1984 |          | gewurztraminer
    1988 |          | 
    1992 |          | 
    1996 |          | 
 2. From clue 3, we know that the 1988 bottle is a pinot noir.
    1984 |          | gewurztraminer
    1988 |          | pinot noir
    1992 |          | 
    1996 |          | 
    Remaining options for 1992 and 1996 are merlot or riesling.
    1984 |          | gewurztraminer
    1988 |          | pinot noir
    1992 |          | merlot or riesling
    1996 |          | merlot or riesling
 3. From clue 4, we know that the merlot is either the Annata Branco or the Bianca Flaux.
    Not clear yet, but lets fill the table with the possible options from vines.
    1984 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | gewurztraminer
    1988 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | pinot noir
    1992 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | merlot or riesling
    1996 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | merlot or riesling

 4. From clue 5, we know that the Bianca Flaux was bottled sometime after the Ece Suss.
    From clue 2, we know that the Bianca Flaux was bottled 4 years before the Vendemmia.
    Using clues 2,5, the order of the options is  Ece Suss is before Bianca Flaux and Bianca Flaux is before Vendemmia. 
    So, Bianca FLaux cannot be in 1984 and Vendemmia cannot be in 1984 and 1988. Eliminate the otions from 1984 and 1988.

    1984 | Annata Branco or Ece Suss                   | gewurztraminer
    1988 | Annata Branco or Ece Suss or Bianca Flaux   | pinot noir
    1992 | Annata Branco or Bianca Flaux or Vendemmia  | merlot or riesling
    1996 | Annata Branco or Vendemmia                  | merlot or riesling
 5. From clue 1, we know that the Ece Suss was bottled sometime after the Annata Branco.
    Ece Suss cannot be in 1984 and Annata Branco cannot be in 1988.
    Bianca Flaux cannot be in 1988 with Ece Suss.
    1984 | Annata Branco                               | gewurztraminer
    1988 | Ece Suss                                    | pinot noir
    1992 | Bianca Flaux               | merlot or riesling
    1996 | Vendemmia                  | merlot or riesling
 
6. From clue 4, we know that the merlot is either the Annata Branco or the Bianca Flaux.

    Since the Annata Branco is in 1984, the merlot must be the Bianca Flaux.
    1984 | Annata Branco                               | gewurztraminer
    1988 | Ece Suss                                    | pinot noir
    1992 | Bianca Flaux                               | merlot      
    1996 | Vendemmia                  | riesling
 Based on the above clues, we can fill in the table as follows:

 
 1984 | Annata Branco | gewurztraminer
 1988 | Ece Suss | pinot noir
 1992 | Bianca Flaux | merlot
 1996 | Vendemmia | riesling
 
 Final Answer:
 1984 | Annata Branco | gewurztraminer
 1988 | Ece Suss | pinot noir
 1992 | Bianca Flaux | merlot
 1996 | Vendemmia | riesling

Input:
{input}
'''



cot_prompt = '''
Solve 4x3 grid world puzzle. Given an input of values and clues , generate an output of 4 rows, where each row has one option from data, separated by space.

Input:
"Nicholas and Edith are having a small dinner party this evening at their home in Cedar Valley, and they've decided to open a select number of rare wines from their personal collection to celebrate the occasion. Using only the clues below, match the vintages to the options from wines and types. Remember, as with all grid-based logic puzzles, no option in any category will ever be used more than once.
vintages : 1984, 1988, 1992, 1996.
wines : Annata Branco, Bianca Flaux, Ece Suss, Vendemmia.
types : gewurztraminer, merlot, pinot noir, riesling.

Clues:
1. The Ece Suss was bottled sometime after the Annata Branco.
2. The Bianca Flaux was bottled 4 years before the Vendemmia.
3. The 1988 bottle is a pinot noir.
4. The merlot is either the Annata Branco or the Bianca Flaux.
5. The Bianca Flaux was bottled sometime after the Ece Suss.
6. The 1984 bottle is a gewurztraminer.

While answering use the following format:
Step-by-step solution:
Your steps showing how you are solving the puzzle

Final Answer:
Fill the following table to show your final answer.
1984 | correct option from wines | correct option from types
1988 | correct option from wines | correct option from types
1992 | correct option from wines | correct option from types
1996 | correct option from wines | correct option from types


Step-by-step solution:
 1. From clue 6, we know that the 1984 bottle is a gewurztraminer.
    1984 |          | gewurztraminer
    1988 |          | 
    1992 |          | 
    1996 |          | 
 2. From clue 3, we know that the 1988 bottle is a pinot noir.
    1984 |          | gewurztraminer
    1988 |          | pinot noir
    1992 |          | 
    1996 |          | 
    Remaining options for 1992 and 1996 are merlot or riesling.
    1984 |          | gewurztraminer
    1988 |          | pinot noir
    1992 |          | merlot or riesling
    1996 |          | merlot or riesling
 3. From clue 4, we know that the merlot is either the Annata Branco or the Bianca Flaux.
    Not clear yet, but lets fill the table with the possible options from vines.
    1984 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | gewurztraminer
    1988 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | pinot noir
    1992 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | merlot or riesling
    1996 | Annata Branco or Bianca Flaux or Ece Suss or Vendemmia  | merlot or riesling

 4. From clue 5, we know that the Bianca Flaux was bottled sometime after the Ece Suss.
    From clue 2, we know that the Bianca Flaux was bottled 4 years before the Vendemmia.
    Using clues 2,5, the order of the options is  Ece Suss is before Bianca Flaux and Bianca Flaux is before Vendemmia. 
    So, Bianca FLaux cannot be in 1984 and Vendemmia cannot be in 1984 and 1988. Eliminate the otions from 1984 and 1988.

    1984 | Annata Branco or Ece Suss                   | gewurztraminer
    1988 | Annata Branco or Ece Suss or Bianca Flaux   | pinot noir
    1992 | Annata Branco or Bianca Flaux or Vendemmia  | merlot or riesling
    1996 | Annata Branco or Vendemmia                  | merlot or riesling
 5. From clue 1, we know that the Ece Suss was bottled sometime after the Annata Branco.
    Ece Suss cannot be in 1984 and Annata Branco cannot be in 1988.
    Bianca Flaux cannot be in 1988 with Ece Suss.
    1984 | Annata Branco                               | gewurztraminer
    1988 | Ece Suss                                    | pinot noir
    1992 | Bianca Flaux               | merlot or riesling
    1996 | Vendemmia                  | merlot or riesling
 
6. From clue 4, we know that the merlot is either the Annata Branco or the Bianca Flaux.

    Since the Annata Branco is in 1984, the merlot must be the Bianca Flaux.
    1984 | Annata Branco                               | gewurztraminer
    1988 | Ece Suss                                    | pinot noir
    1992 | Bianca Flaux                               | merlot      
    1996 | Vendemmia                  | riesling
 Based on the above clues, we can fill in the table as follows:

 
 1984 | Annata Branco | gewurztraminer
 1988 | Ece Suss | pinot noir
 1992 | Bianca Flaux | merlot
 1996 | Vendemmia | riesling
 
 Final Answer:
 1984 | Annata Branco | gewurztraminer
 1988 | Ece Suss | pinot noir
 1992 | Bianca Flaux | merlot
 1996 | Vendemmia | riesling

Input:
{input}
'''


propose_prompt = '''Let's solve a grid world puzzle where you have to mach different categories of items using only clues.

Current partial solution:
    1984 |          | gewurztraminer
    1988 |          | pinot noir
    1992 |          | 
    1996 |          | 

Clues:
1. Ece Suss was bottled after Annata Branco.
2. Bianca Flaux was bottled 4 years before Vendemmia.
3. The 1988 bottle is a pinot noir.
4. The merlot is either the Annata Branco or the Bianca Flaux.
5. Bianca Flaux was bottled after Ece Suss.
6. The 1984 bottle is a gewurztraminer.

Your task is to propose multiple possible next steps that could be explored from this state.

Propose 3-5 possible thoughts:

Thought 1: Assign 1984 to Annata Branco to satisfy the clue about Ece Suss being after it.
    1984 |  Annata Branco        | gewurztraminer
    1988 |          | pinot noir
    1992 |          | 
    1996 |          | 

Thought 2: Try assigning 1992 to Bianca Flaux and 1996 to Vendemmia to satisfy the 4-year gap.
   1984 |                     | gewurztraminer
    1988 |                    | pinot noir
    1992 |   Bianca Flaux     | 
    1996 |   Vendemmia       | 
Thought 3: Explore assigning 1992 to Ece Suss and 1996 to Bianca Flaux to check Clue 5.
   1984 |                   | gewurztraminer
    1988 |                  | pinot noir
    1992 |  Ece Suss        | 
    1996 |  Bianca Flaux       | 

Thought 4: Assign riesling or merlot to 1996 and 1992 the possibilities 
   1984 |                  | gewurztraminer
   1988 |                  | pinot noir
   1992 |                  | merlot or riesling
   1996 |                  | merlot or riesling
Input: {input}
Current partial solution:{current}
Possible next steps:
'''


value_prompt = '''Evaluate if the there exists a matching between values using only clues, output(sure/maybe/impossible).



Clues:
1. The Ece Suss was bottled sometime after the Annata Branco.
2. The Bianca Flaux was bottled 4 years before the Vendemmia.
3. The 1988 bottle is a pinot noir.
4. The merlot is either the Annata Branco or the Bianca Flaux.
5. The Bianca Flaux was bottled sometime after the Ece Suss.
6. The 1984 bottle is a gewurztraminer.

 
1984 |          | gewurztraminer
1988 | Ece Suss | pinot noir
1992 | Bianca Flaux or  Annata Branco | merlot
1996 | Vendemmia | riesling
From clue 6, we know that the 1984 bottle is a gewurztraminer.
sure


1984 |          | 
1988 | Ece Suss | pinot noir
1992 | Bianca Flaux or  Annata Branco | gewurztraminer
1996 | Vendemmia | riesling

 From clue 6, we know that the 1984 bottle is a gewurztraminer.
 But it is incorrectly assigned,
 impossible

 
1984 |  Annata Branco or Ece Suss                   | gewurztraminer
1988 | Annata Branco or Ece Suss or Bianca Flaux    | pinot noir
1992 | Annata Branco or Bianca Flaux or Vendemmia   | merlot or riesling
1996 | Vendemmia                                    | merlot or riesling

From clue 1, we know that the Ece Suss was bottled sometime after the Annata Branco.
Ece Suss cannot be in 1984 and Annata Branco cannot be in 1988.
Bianca Flaux cannot be in 1988 with Ece Suss.

impossible


1984 | Annata Branco or Ece Suss                   | gewurztraminer
1988 | Annata Branco or Ece Suss or Bianca Flaux   | pinot noir
1992 | Annata Branco or Bianca Flaux or Vendemmia  | merlot or riesling
1996 | Annata Branco or Vendemmia                  | merlot or riesling


we know that the Bianca Flaux was bottled sometime after the Ece Suss.
From clue 2, we know that the Bianca Flaux was bottled 4 years before the Vendemmia.
Using clues 2,5, the order of the options is  Ece Suss is before Bianca Flaux and Bianca Flaux is before Vendemmia. 
So, Bianca FLaux cannot be in 1984 and Vendemmia cannot be in 1984 and 1988. Looks these are possible

maybe
{input}
'''

value_last_step_prompt = '''You are solving a grid-based logic puzzle. Each row in the solution includes a year, a wine name, and a wine type. Each item in a category (vintages, wines, types) must be used exactly once. Use the following clues to judge whether the given solution is valid.

Clues:
1. The Ece Suss was bottled sometime after the Annata Branco.
2. The Bianca Flaux was bottled 4 years before the Vendemmia.
3. The 1988 bottle is a pinot noir.
4. The merlot is either the Annata Branco or the Bianca Flaux.
5. The Bianca Flaux was bottled sometime after the Ece Suss.
6. The 1984 bottle is a gewurztraminer.

Example:

Solution:
1984 | Annata Branco | merlot  
1988 | Bianca Flaux  | pinot noir  
1992 | Ece Suss      | riesling  
1996 | Vendemmia     | gewurztraminer  

Judge:  
impossible

Reason:  
The 1984 bottle is supposed to be a gewurztraminer, but it's marked merlot. Also, Bianca Flaux must be after Ece Suss, but here it’s earlier.

---

Solution:
1984 | Annata Branco | gewurztraminer  
1988 | Ece Suss      | pinot noir  
1992 | Bianca Flaux  | merlot  
1996 | Vendemmia     | riesling  

Judge:  
sure

Reason:  
All clues are satisfied. Every item is used once. The 1984 bottle is gewurztraminer, 1988 is pinot noir, Ece Suss is after Annata Branco, and Bianca Flaux is 4 years before Vendemmia.

Input: {input}
Answer: {answer}
Judge:'''
