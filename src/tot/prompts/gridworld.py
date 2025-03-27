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


Let's solve the puzzle step by step.
 
 Step 1:
 From clue 6, we know that the 1984 bottle is a gewurztraminer. Since there's only one gewurztraminer option (riesling), we can conclude that the 1984 bottle is a riesling.
 
 Step 2:
 From clue 1, we know that the Ece Suss was bottled sometime after the Annata Branco. This means that the Ece Suss cannot be the Annata Branco.
 
 Step 3:
 From clue 4, we know that the merlot is either the Annata Branco or the Bianca Flaux. Since the Ece Suss is not the Annata Branco, the Annata Branco must be the merlot.
 
 Step 4:
 From clue 2, we know that the Bianca Flaux was bottled 4 years before the Vendemmia. This means that the Bianca Flaux cannot be the Vendemmia.
 
 Step 5:
 From clue 5, we know that the Bianca Flaux was bottled sometime after the Ece Suss. This means that the Ece Suss must be bottled before the Bianca Flaux.
 
 Step 6:
 From clue 3, we know that the 1988 bottle is a pinot noir. Since there's only one pinot noir option (pinot noir), we can conclude that the 1988 bottle is a pinot noir.
 
 Step 7:
 From the remaining options, we can conclude that the 1992 bottle is the Vendemmia (since it's not the Annata Branco, Bianca Flaux, or Ece Suss).
 
 Step 8:
 From the remaining options, we can conclude that the 1996 bottle is the Branco (since it's not the Annata Branco, Bianca Flaux, Ece Suss, or Vendemmia).
 
 Final Answer:
 
 1984 | Riesling | Gewurztraminer
 1988 | Pinot Noir | Pinot Noir
 1992 | Vendemmia | Merlot
 1996 | Branco | Annata"

Input:
{input}

Output:
'''



#cot_prompt


propose_prompt = '''Let's play a 5 x 5 mini crossword, where each word should have exactly 5 letters.

{input}

Given the current status, list all possible answers for unfilled or changed words, and your confidence levels (certain/high/medium/low), using the format "h1. apple (medium)". Use "certain" cautiously and only when you are 100% sure this is the correct word. You can list more then one possible answer for each word.
'''


value_prompt = '''Evaluate if there exists a five letter word of some meaning that fit some letter constraints (sure/maybe/impossible).

Incorrect; to injure: w _ o _ g
The letter constraint is: 5 letters, letter 1 is w, letter 3 is o, letter 5 is g.
Some possible words that mean "Incorrect; to injure":
wrong (w r o n g): 5 letters, letter 1 is w, letter 3 is o, letter 5 is g. fit!
sure

A person with an all-consuming enthusiasm, such as for computers or anime: _ _ _ _ u
The letter constraint is: 5 letters, letter 5 is u.
Some possible words that mean "A person with an all-consuming enthusiasm, such as for computers or anime":
geek (g e e k): 4 letters, not 5
otaku (o t a k u): 5 letters, letter 5 is u
sure

Dewy; roscid: r _ _ _ l
The letter constraint is: 5 letters, letter 1 is r, letter 5 is l.
Some possible words that mean "Dewy; roscid":
moist (m o i s t): 5 letters, letter 1 is m, not r
humid (h u m i d): 5 letters, letter 1 is h, not r
I cannot think of any words now. Only 2 letters are constrained, it is still likely
maybe

A woodland: _ l _ d e
The letter constraint is: 5 letters, letter 2 is l, letter 4 is d, letter 5 is e.
Some possible words that mean "A woodland":
forest (f o r e s t): 6 letters, not 5
woods (w o o d s): 5 letters, letter 2 is o, not l
grove (g r o v e): 5 letters, letter 2 is r, not l
I cannot think of any words now. 3 letters are constrained, and _ l _ d e seems a common pattern
maybe

An inn: _ d _ w f
The letter constraint is: 5 letters, letter 2 is d, letter 4 is w, letter 5 is f.
Some possible words that mean "An inn":
hotel (h o t e l): 5 letters, letter 2 is o, not d
lodge (l o d g e): 5 letters, letter 2 is o, not d
I cannot think of any words now. 3 letters are constrained, and it is extremely unlikely to have a word with pattern _ d _ w f to mean "An inn"
impossible

Chance; a parasitic worm; a fish: w r a k _
The letter constraint is: 5 letters, letter 1 is w, letter 2 is r, letter 3 is a, letter 4 is k.
Some possible words that mean "Chance; a parasitic worm; a fish":
fluke (f l u k e): 5 letters, letter 1 is f, not w
I cannot think of any words now. 4 letters are constrained, and it is extremely unlikely to have a word with pattern w r a k _ to mean "Chance; a parasitic worm; a fish"
impossible

{input}
'''