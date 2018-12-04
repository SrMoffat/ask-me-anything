import pandas as pd
import re
import spacy

from helpers import get_data_set, get_user_input, post_question_to_df

nlp = spacy.load('en')
print('done')
get_data_set()
df = post_question_to_df()

a = df['sentence']
print('done')



  
############################################
# SELECT QUESTIONS STARTING WITH QWORDS1
############################################

# ALTERNATIVE QUESTIONS ARE AN EXCEPTION FOR QWORDS1: Who is better Trump or Clinton?
qwords1 = [('What is'), ('What was'), ('What are'), ('What were'), ('Which is'), ('Which was'), ('Which are'), ('Which were'), ('Who is')] # 30%
qwords2 = [('How do ')] # 10% # 'How did' is the same, except the verb must be converted to past tense
# "How will" is same: I now only insert 'will' befor VB, but more verb tags should be added like with qwords5
qwords3 = [('How can'), ('How could'), ('How would'), ('How should')] # 6% 
qwords4 = [('Why do ')] # 2% 'Why' did' is the same, except the verb must be converted to past tense
qwords5x= [('Why is it that')] # 2%
qwords5 = [('Why is'), ('Why is it that'), ('Why was it that'), ('Why was'), ('Why are'), ('Why were')]
qwords6 = [('Is it'), ('Was it')]
qwords7 = [('What do ')] # 'What did' is the same, except the verb must be converted to past tense
qwords8 = [('What does')]
qwords9 = [('How does')]
qwords10 = [('Is there'), ('Are there'), ('Was there'), ('Were there')]
qwords11 = [('Where can'), ('Where could'), ('Where would'), ('Where should')]
qwords12 = [('Why does')]
qwords13 = [('How is'), ('How was'), ('How are'), ('How were')]
qwords14 = [('What will')]
#qwords15 = 
#qwords14 = [('How much')]
#qwords15 = [('Why are')]


def findq1(row):
    for i in qwords1:
        if i in row:
            return row       
    return ''

df['qwords1'] = a.apply(findq1) # From quoratrain, extract questions that start with qword1
#df['qwords1'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords1'], inplace=True)
b = df['qwords1']



def findq2(row):
    for j in qwords2:
        if j in row:
            return row       
    return ''

df['qwords2'] = a.apply(findq2) # From quoratrain, extract questions that start with qword2
#df['qwords2'].replace('', np.nan, inplace=True)
#df.dropna(subset=['qwords2'], inplace=True)
c = df['qwords2']



def findq3(row):
    for j in qwords3:
        if j in row:
            return row       
    return ''

df['qwords3'] = a.apply(findq3) # From quoratrain, extract questions that start with qword3
#df['qwords2'].replace('', np.nan, inplace=True)
#df.dropna(subset=['qwords2'], inplace=True)
d = df['qwords3']



def findq4(row):
    for i in qwords4:
        if i in row:
            return row       
    return ''

df['qwords4'] = a.apply(findq4) # From quoratrain, extract questions that start with qword1
#df['qwords1'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords1'], inplace=True)
e = df['qwords4']



def findq5x(row):
    for i in qwords5:
        if i in row:
            return row       
    return ''

df['qwords5x'] = a.apply(findq5x) # From quoratrain, extract questions that start with qword1
#df['qwords1'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords1'], inplace=True)
fx = df['qwords5x']



def findq5(row):
    for i in qwords5:
        if i in row:
            return row       
    return ''

df['qwords5'] = a.apply(findq5) # From quoratrain, extract questions that start with qword1
#df['qwords1'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords1'], inplace=True)
f = df['qwords5']



def findq6(row):
    for i in qwords6:
        if i in row:
            return row       
    return ''

df['qwords6'] = a.apply(findq6) # From quoratrain, extract questions that start with qword1
#df['qwords1'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords1'], inplace=True)
g = df['qwords6']



def findq7(row):
    for i in qwords7:
        if i in row:
            return row       
    return ''

df['qwords7'] = a.apply(findq7) # From quoratrain, extract questions that start with qword1
#df['qwords1'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords1'], inplace=True)
h = df['qwords7']



def findq8(row):
    for i in qwords8:
        if i in row:
            return row       
    return ''

df['qwords8'] = a.apply(findq8) # From quoratrain, extract questions that start with qword1
#df['qwords8'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords8'], inplace=True)
k1 = df['qwords8']



def findq9(row):
    for i in qwords9:
        if i in row:
            return row       
    return ''

df['qwords9'] = a.apply(findq9) # From quoratrain, extract questions that start with qword1
#df['qwords9'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords9'], inplace=True)
k2 = df['qwords9']



def findq10(row):
    for i in qwords10:
        if i in row:
            return row       
    return ''

df['qwords10'] = a.apply(findq10) # From quoratrain, extract questions that start with qword1
#df['qwords10'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords10'], inplace=True)
k3 = df['qwords10']



def findq11(row):
    for i in qwords11:
        if i in row:
            return row       
    return ''

df['qwords11'] = a.apply(findq11) # From quoratrain, extract questions that start with qword1
#df['qwords11'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords11'], inplace=True)
k4 = df['qwords11']



def findq12(row):
    for i in qwords12:
        if i in row:
            return row       
    return ''

df['qwords12'] = a.apply(findq12) # From quoratrain, extract questions that start with qword1
#df['qwords11'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords12'], inplace=True)
k5 = df['qwords12']



def findq13(row):
    for i in qwords13:
        if i in row:
            return row       
    return ''

df['qwords13'] = a.apply(findq13) # From quoratrain, extract questions that start with qword1
#df['qwords11'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords12'], inplace=True)
k6 = df['qwords13']



qwords14 = [('What should')]

def findq14(row):
    for i in qwords14:
        if i in row:
            return row       
    return ''

df['qwords14'] = a.apply(findq14) # From quoratrain, extract questions that start with qword1
#df['qwords14'].replace('', np.nan, inplace=True) # Replace empty rows
#df.dropna(subset=['qwords14'], inplace=True)
k7 = df['qwords14']


print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 1+2
############################################

def template1(row):
    i = row
    if i == '':
        return i
    i = re.sub(r'\bmy\b', 'yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\byour\b', 'myy', i)
    i = re.sub(r'\byou\b', 'II!az', i)
    i = re.sub(r'\bI\b', 'youu', i)
    i = re.sub(r'\bmine\b', 'yourss', i)
    i = re.sub(r'\byours\b', 'minee', i)
    
    i = re.sub(r'\bit like\b', '', i) 
    i = re.sub(r'\blikes me\b', 'likes you', i)
    i = re.sub(r'\blike as\b', 'is ANSWER as', i)
    i = re.sub(r'\bbe like as\b', 'as', i)
    i = re.sub(r'\bit be like\b', '', i)
    i = re.sub(r'\bit like as\b', 'as', i)
    i = re.sub(r'\blike in\b', 'in', i)
    i = re.sub(r'\blook like\b', '', i)
    i = re.sub(r'\bbe like\b', '', i) 
    i = i.split()
    if len(i) > 1:
        if i[-1] == 'like?':
            i.pop(-1)
        # This is the conversion for qwords1
        i.pop(0)
        i.insert(len(i), i.pop(0)) # Take the first word and put it at the ends
        i = [i.replace('?', '') for i in i] # remove question mark
        i = [i[0].capitalize()] + i[1:] # Capitalise first word

        # Correct the words
        i = [i.replace('yourr', 'your') for i in i] 
        i = [i.replace('myy', 'my') for i in i]
        i = [i.replace('II!az', 'I') for i in i]
        i = [i.replace('youu', 'you') for i in i]
        i = [i.replace('yourss', 'yours') for i in i]
        i = [i.replace('minee', 'mine') for i in i]
        
        # In case the word is now the first word, use capitals
        i = [i.replace('Yourr', 'Your') for i in i]
        i = [i.replace('Myy', 'My') for i in i]
        i = [i.replace('Ii!az', 'I') for i in i]
        i = [i.replace('Youu', 'You') for i in i]
        i = [i.replace('Yourss', 'Yours') for i in i]
        i = [i.replace('Minee', 'Mine') for i in i]
        i = " ".join(i)
        
        if 'is ANSWER as' in i:
            i = i.split()
            if i[-1] == 'is': # Present tense
                i.pop(-1) # Remove 'is' as last word
                i = " ".join(i) + "." # Add full stop
            if i[-1] == 'was': # Past tense
                i.pop(-1)
                i = " ".join(i) + "."
                i = re.sub(r'\bis ANSWER\b', 'was ANSWER', i)
        
        return i
    else:
        return ''

def template2(row):
    j = row
    if j == '':
        return j
    j = re.sub(r'\bmy\b', 'yourr', j) # To avoid words being converted back by the next line
    j = re.sub(r'\byour\b', 'myy', j)
    j = re.sub(r'\byou\b', 'II', j)
    j = re.sub(r'\bI\b', 'youu', j)
    j = re.sub(r'\bmine\b', 'yourss', j)
    j = re.sub(r'\byours\b', 'minee', j)
    
    j = re.sub(r'\bit like\b', '', j) 
    j = re.sub(r'\blikes me\b', 'likes you', j)
    i = re.sub(r'\blike as\b', 'is ANSWER as', j)
    j = re.sub(r'\bbe like as\b', 'as', j)
    j = re.sub(r'\bit be like\b', '', j)
    j = re.sub(r'\bit like as\b', 'as', j)
    j = re.sub(r'\blike in\b', 'in', j)
    j = re.sub(r'\blook like\b', '', j)
    j = re.sub(r'\bbe like\b', '', j)    
    j = j.split()
    if len(j) > 1:
        if j[-1] == 'like?':
            j.pop(-1)
        # This is the conversion for qwords2
        j.pop(0) # Remove first two words
        j.pop(0)
        j.insert(len(j), 'by') # Add 'by' to the end of the sentence
        j = [j.replace('?', '') for j in j] # remove question mark
        j = [j[0].capitalize()] + j[1:] # Capitalise first word
        
        # Correct the words
        j = [j.replace('yourr', 'your') for j in j] 
        j = [j.replace('myy', 'my') for j in j]
        j = [j.replace('II', 'I') for j in j]
        j = [j.replace('youu', 'you') for j in j]
        j = [j.replace('yourss', 'yours') for j in j]
        j = [j.replace('minee', 'mine') for j in j]
        
        # In case the word is now the first word, use capitals
        j = [j.replace('Yourr', 'Your') for j in j]
        j = [j.replace('Myy', 'My') for j in j]
        j = [j.replace('Ii', 'I') for j in j]
        j = [j.replace('Youu', 'You') for j in j]
        j = [j.replace('Yourss', 'Yours') for j in j]
        j = [j.replace('Minee', 'Mine') for j in j]        
        j = " ".join(j)
        
        # In case the question involves 'What is/was XYZ like as a person'
        if 'is ANSWER as' in j:
            j = j.split()
            if j[-1] == 'is': # Present tense
                j.pop(-1) # Remove 'is' as last word added the the standards procedure above
                j = " ".join(j) + "." # Add full stop
            if j[-1] == 'was': # Past tense
                j.pop(-1)
                j = " ".join(j) + "."
                j = re.sub(r'\bis ANSWER\b', 'was ANSWER', j)
        
        return j
    else:
        return ''

df['qwords1_template'] = b.apply(template1)
df['qwords2_template'] = c.apply(template2)

print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 3
############################################

def template3(row):
    ################ 1 Lines marked '1' are for actual usages, '2' for easier testing
    k = row
    # Inserting 'can' before the next verb, parsing using spacy
    sentence_spacy = nlp(k)
    pos = []
    for token in sentence_spacy:
        pos.append(token.tag_)
    ################ 1
    ################ 2    
    #k = row['qwords3'] 
    #pos = list(row['question1_pos'])
    ################ 2    

    # Find the index of the verb and add 'can' before verb
    try:
        x = pos.index("VB")
        k = k.split()
        k.insert(x, 'can')
    except ValueError: # If spacy finds no verb, we insert 'can' at index 1
        k = k.split()
        k.insert(1, 'can')
            
    k = " ".join(k)        
    k = re.sub(r'\bmy\b', 'yourr', k) # To avoid words being converted back by the next line
    k = re.sub(r'\byour\b', 'myy', k)
    k = re.sub(r'\byou\b', 'II!az', k)
    k = re.sub(r'\bI\b', 'youu', k)
    k = re.sub(r'\bmine\b', 'yourss', k)
    k = re.sub(r'\byours\b', 'minee', k)
    
    k = re.sub(r'\bit like\b', '', k) 
    k = re.sub(r'\blikes me\b', 'likes you', k)
    k = re.sub(r'\bbe like as\b', 'as', k)
    k = re.sub(r'\bit be like\b', '', k)
    k = re.sub(r'\bit like as\b', 'as', k)
    k = re.sub(r'\blike in\b', 'in', k)
    k = re.sub(r'\blook like\b', '', k)
    k = re.sub(r'\bbe like\b', '', k) 
    k = k.split()
    if len(k) > 1:
        if k[-1] == 'like?':
            k.pop(-1)
        # This is the conversion for qwords3
        k.pop(0) # Remove first two words
        k.pop(0)
        k.insert(len(k), 'by') # Add 'by' to the end of the sentence

        k = [k.replace('?', '') for k in k] # remove question mark
        k = [k[0].capitalize()] + k[1:] # Capitalise first word

        # Correct the words
        k = [k.replace('yourr', 'your') for k in k] 
        k = [k.replace('myy', 'my') for k in k]
        k = [k.replace('II!az', 'I') for k in k]
        k = [k.replace('youu', 'you') for k in k]
        k = [k.replace('yourss', 'yours') for k in k]
        k = [k.replace('minee', 'mine') for k in k]
        
        # In case the word is now the first word, use capitals
        k = [k.replace('Yourr', 'Your') for k in k]
        k = [k.replace('Myy', 'My') for k in k]
        k = [k.replace('Ii!az', 'I') for k in k]
        k = [k.replace('Youu', 'You') for k in k]
        k = [k.replace('Yourss', 'Yours') for k in k]
        k = [k.replace('Minee', 'Mine') for k in k]
        k = " ".join(k)
        
        return k
    else:
        return ''

#Using the dataframe df.apply, to select the question and corresponding POS tags (at start of function)
################ 2 
df['qwords3_template'] = d.apply(template3) 
################ 2

################ 1
#df['qwords3_template'] = d.apply(template3)
################ 1
print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 4
############################################

def template4(row):
    l = row
    if l == '':
        return l
    l = re.sub(r'\bmy\b', 'yourr', l) # To avoid words being converted back by the next line
    l = re.sub(r'\byour\b', 'myy', l)
    l = re.sub(r'\byou\b', 'II', l)
    l = re.sub(r'\bI\b', 'youu', l)
    l = re.sub(r'\bmine\b', 'yourss', l)
    l = re.sub(r'\byours\b', 'minee', l)
    
    l = re.sub(r'\bit like\b', '', l) 
    l = re.sub(r'\blikes me\b', 'likes you', l)
    i = re.sub(r'\blike as\b', 'is ANSWER as', l)
    l = re.sub(r'\bbe like as\b', 'as', l)
    l = re.sub(r'\bit be like\b', '', l)
    l = re.sub(r'\bit like as\b', 'as', l)
    l = re.sub(r'\blike in\b', 'in', l)
    l = re.sub(r'\blook like\b', '', l)
    l = re.sub(r'\bbe like\b', '', l)    
    l = l.split()
    if len(l) > 1:
        if l[-1] == 'like?':
            l.pop(-1)
        # This is the conversion for qwords2
        l.pop(0) # Remove first two words
        l.pop(0)
        l.insert(len(l), 'because') # Add 'by' to the end of the sentence
        l = [l.replace('?', '') for l in l] # remove question mark
        l = [l[0].capitalize()] + l[1:] # Capitalise first word
        
        # Correct the words
        l = [l.replace('yourr', 'your') for l in l] 
        l = [l.replace('myy', 'my') for l in l]
        l = [l.replace('II', 'I') for l in l]
        l = [l.replace('youu', 'you') for l in l]
        l = [l.replace('yourss', 'yours') for l in l]
        l = [l.replace('minee', 'mine') for l in l]
        
        # In case the word is now the first word, use capitals
        l = [l.replace('Yourr', 'Your') for l in l]
        l = [l.replace('Myy', 'My') for l in l]
        l = [l.replace('Ii', 'I') for l in l]
        l = [l.replace('Youu', 'You') for l in l]
        l = [l.replace('Yourss', 'Yours') for l in l]
        l = [l.replace('Minee', 'Mine') for l in l]        
        l = " ".join(l)
        
        # In case the question involves 'What is/was XYZ like as a person'
        if 'is ANSWER as' in l:
            l = l.split()
            if l[-1] == 'is': # Present tense
                l.pop(-1) # Remove 'is' as last word added the the standards procedure above
                l = " ".join(l) + "." # Add full stop
            if l[-1] == 'was': # Past tense
                l.pop(-1)
                l = " ".join(l) + "."
                l = re.sub(r'\bis ANSWER\b', 'was ANSWER', l)
        
        return l
    else:
        return ''

df['qwords4_template'] = e.apply(template4)

print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 5
############################################

# in 'Why is' questions, we insert 'is' into the sentence according to the following rule:
# Insert 'is' after the first entity that is followed by 2 or more non-entities. 
# So we group all POS tags that signify entities in 'members' and all non-entities POS tags in non-members
# The conversion does NOT go well for questions that start with: "WHY IS IT THAT ..."

members = ['NN', 'NNP', 'NNPS', 'NNS', 'PRP']
non_members = ['$', 'ADD', 'AFX', 'BES', 'CC', 'CD', 'DT', 'EX', 'FW', 'GW', 'HVS', 'HYPH', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NFP', 'NIL', 'PDT', 'POS', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', '_SP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'df', 'WP', 'WP$', 'WRB', 'XX']

def template5(row):
    L = row
    if L == '':
        return L
    if 'Why is it that' in L:
        L = L.split()
        L.pop(0) # Remove first two words
        L.pop(0) 
        L = " ".join(L)
        return L
    elif 'Why was it that' in L:
        L = L.split()
        L.pop(0) # Remove first two words
        L.pop(0) 
        L = " ".join(L)
        return L
    else:
        sentence_spacy = nlp(L)
        pos = []
        for token in sentence_spacy:
            pos.append(token.tag_)

        look = 2 # Look two words ahead
        for i in range(len(pos)-look):
            if (pos[i] in members) & (pos[i+1] in non_members) & (pos[i+2] in non_members):
                # if the condition is met, return the list with the 1 added where you want
                L = L.split()
                L.insert(i+1, L[1])
                L = " ".join(L)
                return L
            elif(pos[i] in members) & (pos[i+1] in non_members) & (pos[i+2] == '.'):
                L = L.split()
                L.insert(i+1, L[1])
                L = " ".join(L)
                return L
        return ''

x = f.apply(template5)

def func5(row):
    L = row
    L = re.sub(r'\bmy\b', 'yourr', L) # To avoid words being converted back by the next line
    L = re.sub(r'\byour\b', 'myy', L)
    L = re.sub(r'\byou\b', 'II', L)
    L = re.sub(r'\bI\b', 'youu', L)
    L = re.sub(r'\bmine\b', 'yourss', L)
    L = re.sub(r'\byours\b', 'minee', L)
    
    L = re.sub(r'\bit like\b', '', L) 
    L = re.sub(r'\blikes me\b', 'likes you', L)
    L = re.sub(r'\blike as\b', 'is ANSWER as', L)
    L = re.sub(r'\bbe like as\b', 'as', L)
    L = re.sub(r'\bit be like\b', '', L)
    L = re.sub(r'\bit like as\b', 'as', L)
    L = re.sub(r'\blike in\b', 'in', L)
    L = re.sub(r'\blook like\b', '', L)
    L = re.sub(r'\bbe like\b', '', L)    
    L = L.split()
    if len(L) > 1:
        if L[-1] == 'like?':
            L.pop(-1)
        # This is the conversion for qwords5
        L.pop(0) # Remove first two words
        L.pop(0)
        L.insert(len(L), 'because') # Add 'because' to the end of the sentence

        L = [L.replace('?', '') for L in L] # remove question mark
        L = [L[0].capitalize()] + L[1:] # Capitalise first word

        # Correct the words
        L = [L.replace('yourr', 'your') for L in L] 
        L = [L.replace('myy', 'my') for L in L]
        L = [L.replace('II!az', 'I') for L in L]
        L = [L.replace('youu', 'you') for L in L]
        L = [L.replace('yourss', 'yours') for L in L]
        L = [L.replace('minee', 'mine') for L in L]

        # In case the word is now the first word, use capitals
        L = [L.replace('Yourr', 'Your') for L in L]
        L = [L.replace('Myy', 'My') for L in L]
        L = [L.replace('Ii!az', 'I') for L in L]
        L = [L.replace('Youu', 'You') for L in L]
        L = [L.replace('Yourss', 'Yours') for L in L]
        L = [L.replace('Minee', 'Mine') for L in L]
        L = " ".join(L)
        return L
    else:
        return ''   

#y = x.apply(func5)          
    

#Using the dataframe df.apply, to select the question and corresponding POS tags (at start of function)
################ 2 
#df['qwords5_template'] = df.apply(template5, axis=1)
################ 2

################ 1
df['qwords5_template'] = x.apply(func5)
################ 1
print('done')


  
def template6(row):
    m = row
    if m == '':
        return m    
    m = re.sub(r'\bmy\b', 'yourr', m) # To avoid words being converted back by the next line
    m = re.sub(r'\byour\b', 'myy', m)
    m = re.sub(r'\bme\b', 'youu', m)
    m = re.sub(r'\byou\b', 'II!az', m)
    m = re.sub(r'\bI\b', 'youu', m)
    m = re.sub(r'\bmine\b', 'yourss', m)
    m = re.sub(r'\byours\b', 'minee', m)
    
    m = re.sub(r'\bit like\b', '', m) 
    m = re.sub(r'\blikes me\b', 'likes you', m)
    m = re.sub(r'\bbe like as\b', 'as', m)
    m = re.sub(r'\bit be like\b', '', m)
    m = re.sub(r'\bit like as\b', 'as', m)
    m = re.sub(r'\blike in\b', 'in', m)
    m = re.sub(r'\blook like\b', '', m)
    m = re.sub(r'\bbe like\b', '', m) 
    m = m.split()
    if len(m) > 1:
        if m[-1] == 'lime?':
            m.pop(-1)
        # This is the conversion for qwords3
        m.pop(0) # Remove first two words
        m.pop(0) # Remove first two words
        m.insert(0, 'Yes/No, I think it is/is not') # Add 'by' to the end of the sentence
        m = [m.replace('?', '') for m in m] # remove question mark
#        m = [m[0].capitalize()] + m[1:] # Capitalise first word

        # Correct the words
        m = [m.replace('yourr', 'your') for m in m] 
        m = [m.replace('myy', 'my') for m in m]
        m = [m.replace('II!az', 'I') for m in m]
        m = [m.replace('youu', 'you') for m in m]
        m = [m.replace('yourss', 'yours') for m in m]
        m = [m.replace('minee', 'mine') for m in m]
        
        # In case the word is now the first word, use capitals
        m = [m.replace('Yourr', 'Your') for m in m]
        m = [m.replace('Myy', 'My') for m in m]
        m = [m.replace('Ii!az', 'I') for m in m]
        m = [m.replace('Youu', 'You') for m in m]
        m = [m.replace('Yourss', 'Yours') for m in m]
        m = [m.replace('Minee', 'Mine') for m in m]
        m = " ".join(m) + "."
        m = m + ' According to [add RELIABLE SOURCE], [add reason from this source].'
        
        return m
    else:
        return ''

df['qwords6_template'] = g.apply(template6)
print('done')


  
def template7(row):
    n = row
    if n == '':
        return n    
    n = re.sub(r'\bmy\b', 'yourr', n) # To avoid words being converted back by the next line
    n = re.sub(r'\byour\b', 'myy', n)
    n = re.sub(r'\bme\b', 'youu', n)
    n = re.sub(r'\byou\b', 'II!az', n)
    n = re.sub(r'\bI\b', 'youu', n)
    n = re.sub(r'\bmine\b', 'yourss', n)
    n = re.sub(r'\byours\b', 'minee', n)
    
    n = re.sub(r'\bit like\b', '', n) 
    n = re.sub(r'\blikes me\b', 'likes you', n)
    n = re.sub(r'\bbe like as\b', 'as', n)
    n = re.sub(r'\bit be like\b', '', n)
    n = re.sub(r'\bit like as\b', 'as', n)
    n = re.sub(r'\blike in\b', 'in', n)
    n = re.sub(r'\blook like\b', '', n)
    n = re.sub(r'\bbe like\b', '', n) 
    n = n.split()
    if len(n) > 1:
        if n[-1] == 'like?':
            n.pop(-1)
        # This is the conversion for qwords3
        n.pop(1) # Remove second words
        n.insert(len(n), 'is') # Add 'by' to the end of the sentence
        n = [n.replace('?', '') for n in n] # remove question mark

        # Correct the words
        n = [n.replace('yourr', 'your') for n in n] 
        n = [n.replace('myy', 'my') for n in n]
        n = [n.replace('II!az', 'I') for n in n]
        n = [n.replace('youu', 'you') for n in n]
        n = [n.replace('yourss', 'yours') for n in n]
        n = [n.replace('minee', 'mine') for n in n]
        
        # In case the word is now the first word, use capitals
        n = [n.replace('Yourr', 'Your') for n in n]
        n = [n.replace('Myy', 'My') for n in n]
        n = [n.replace('Ii!az', 'I') for n in n]
        n = [n.replace('Youu', 'You') for n in n]
        n = [n.replace('Yourss', 'Yours') for n in n]
        n = [n.replace('Minee', 'Mine') for n in n]
        n = " ".join(n)
        
        return n
    else:
        return ''

df['qwords7_template'] = h.apply(template7)
print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 8
############################################
def template8(row):
    L = row
    if L == '':
        return L    
    doc = nlp(L)
    chunks = []
    pos = []
    vblist = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']    
    if 'What does it mean when' in L:
        L = L.split()
        del L[:4]
        L = " ".join(L) + ','
        L = L.split()
        L.insert(len(L), 'it means 1') # Take the first word and put it at the ends
        L = [L.replace('?', '') for L in L] # remove question mark
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:] # Capitalise first word
        L = " ".join(L)
#        print(L)
        return L
    elif 'What does it mean if' in L:
        L = L.split()
        del L[:4]
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:] # Capitalise first word 
        L = " ".join(L) + ','
        L = L.split()
        L.insert(len(L), 'it means 2') # Take the first word and put it at the ends
        L = [L.replace('?', '') for L in L] # remove question mark
        L = " ".join(L)
#        print(L)
        return L
    elif 'What does it mean' in L:
        L = L.split()
        del L[:4]
        L = [L.replace('?', '') for L in L] # remove question mark     
        L.insert(len(L), 'means 3') # Take the first word and put it at the ends
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:] # Capitalise first word   
        L = " ".join(L)
#        print(L)
        return L
    elif 'What does it' in L:
        L = L.split()
        if L[4] == 'like':
            L.pop(4)
        L.insert(len(L), L[3])
        del L[:4]
#        L.pop(0) # Remove first two words
#        L.pop(0) # This way, sentence can be further processed same as the other'What does'
#        L.pop(0)
#        L.pop(0)
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:] # Capitalise first word
        L = [L.replace('?', '') for L in L] # remove question mark
        L = " ".join(L) + 's'
        return L
    elif 'What does' in doc.text:    
            ran = False
            for token in doc:
                pos.append(token.tag_)
                if token.tag_ in vblist and not ran:
                    if 'mean' in doc.text: # check for 'do'
                        if token.text == 'mean':
                            chunks.append(token.text + 's' + token.whitespace_)
                            ran = True
                        else:
                            chunks.append(token.text_with_ws)
                    elif token.text == 'do': # check for 'do'
                        chunks.append(token.text + 'es' + token.whitespace_)
                        ran = True                        
                    else:
                        if token.text != 'does': # to skip the first verb 'does'
                            chunks.append(token.text + 's' + token.whitespace_)
                            ran = True                        
                else:
                    chunks.append(token.text_with_ws)
            L = chunks
            if L[1] == 'does ':
                L.pop(1)
            L = [L.replace('?', '') for L in L]
            L.insert(len(L), ' is 5')
            L = "".join(L)
            return L
    else:
        return""

x = k1.apply(template8)
#print(x)


def func1(row):
    i = str(row)   
    i = re.sub(r'\bmy\b', 'yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bI\b', 'youu', i)
    i = re.sub(r'\bmine\b', 'yourss', i)
    i = re.sub(r'\dos\b', 'does', i)
    
    i = re.sub(r'\bit like\b', '', i) 
    i = re.sub(r'\blikes me\b', 'likes you', i)
    i = re.sub(r'\blike as\b', 'is ANSWER as', i)
    i = re.sub(r'\bbe like as\b', 'as', i)
    i = re.sub(r'\bit be like\b', '', i)
    i = re.sub(r'\bit like as\b', 'as', i)
    i = re.sub(r'\blike in\b', 'in', i)
    i = re.sub(r'\blook like\b', '', i)
    i = re.sub(r'\bbe like\b', '', i) 
    i = i.split()

    # Correct the words
    i = [i.replace('yourr', 'your') for i in i] 
    i = [i.replace('myy', 'my') for i in i]
    i = [i.replace('II!az', 'I') for i in i]
    i = [i.replace('youu', 'you') for i in i]
    i = [i.replace('yourss', 'yours') for i in i]
    i = [i.replace('minee', 'mine') for i in i]

    # In case the word is now the first word, use capitals
    i = [i.replace('Yourr', 'Your') for i in i]
    i = [i.replace('Myy', 'My') for i in i]
    i = [i.replace('Ii!az', 'I') for i in i]
    i = [i.replace('Youu', 'You') for i in i]
    i = [i.replace('Yourss', 'Yours') for i in i]
    i = [i.replace('Minee', 'Mine') for i in i]
    i = " ".join(i)

    if 'is ANSWER as' in i:
        i = i.split()
        if i[-1] == 'is': # Present tense
            i.pop(-1) # Remove 'is' as last word
            i = " ".join(i) + "." # Add full stop
        if i[-1] == 'was': # Past tense
            i.pop(-1)
            i = " ".join(i) + "."
            i = re.sub(r'\bis ANSWER\b', 'was ANSWER', i)
    return i
    
df['qwords8_template'] = x.apply(func1)
#print(df['qwords8_template'])
print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 9
############################################
# There are still small mistakes due to spaCy not correctly recognising verbs

def template9(row):
    L = row
    if L == '':
        return L
    doc = nlp(L)
    chunks = []
    pos = []
    vblist = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    if 'How does it ' in doc.text:
        L = L.split()
        if L[4] == 'like':
            L.pop(4)
        L.insert(len(L), L[3])
        del L[:4]
        L = [L[0].capitalize()] + L[1:] # Capitalise first word
        L = [L.replace('?', '') for L in L] # remove question mark
        L = " ".join(L) + 's'
        return L
    elif 'How does' in doc.text:
        ran = False
        for token in doc:
            pos.append(token.tag_)
            if token.tag_ in vblist and not ran:
                if 'mean' in doc.text: # check for 'do'
                    if token.text == 'mean':
                        chunks.append(token.text + 's' + token.whitespace_)
                        ran = True
                    else:
                        chunks.append(token.text_with_ws)
                elif token.text == 'do': # check for 'do'
                    chunks.append(token.text + 'es' + token.whitespace_)
                    ran = True                        
                else:
                    if token.text != 'does': # to skip the first verb 'does'
                        chunks.append(token.text + 's' + token.whitespace_)
                        ran = True                        
            else:
                chunks.append(token.text_with_ws)
        L = chunks
        if L[1] == 'does ':
            L.pop(1)
        L.pop(0)
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' [how:]')
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = "".join(L)
        return L
    else:
        return""        

x2 = k2.apply(template9)
#print(x)

def func2(row):
    i = str(row)   
    i = re.sub(r'\bmy\b', 'yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bI\b', 'youu', i)
    i = re.sub(r'\bmine\b', 'yourss', i)
    i = re.sub(r'\dos\b', 'does', i)
    
    i = re.sub(r'\bit like\b', '', i) 
    i = re.sub(r'\blikes me\b', 'likes you', i)
    i = re.sub(r'\blike as\b', 'is ANSWER as', i)
    i = re.sub(r'\bbe like as\b', 'as', i)
    i = re.sub(r'\bit be like\b', '', i)
    i = re.sub(r'\bit like as\b', 'as', i)
    i = re.sub(r'\blike in\b', 'in', i)
    i = re.sub(r'\blook like\b', '', i)
    i = re.sub(r'\bbe like\b', '', i) 
    i = i.split()

    # Correct the words
    i = [i.replace('yourr', 'your') for i in i] 
    i = [i.replace('myy', 'my') for i in i]
    i = [i.replace('II!az', 'I') for i in i]
    i = [i.replace('youu', 'you') for i in i]
    i = [i.replace('yourss', 'yours') for i in i]
    i = [i.replace('minee', 'mine') for i in i]

    # In case the word is now the first word, use capitals
    i = [i.replace('Yourr', 'Your') for i in i]
    i = [i.replace('Myy', 'My') for i in i]
    i = [i.replace('Ii!az', 'I') for i in i]
    i = [i.replace('Youu', 'You') for i in i]
    i = [i.replace('Yourss', 'Yours') for i in i]
    i = [i.replace('Minee', 'Mine') for i in i]
    i = " ".join(i)

    if 'is ANSWER as' in i:
        i = i.split()
        if i[-1] == 'is': # Present tense
            i.pop(-1) # Remove 'is' as last word
            i = " ".join(i) + "." # Add full stop
        if i[-1] == 'was': # Past tense
            i.pop(-1)
            i = " ".join(i) + "."
            i = re.sub(r'\bis ANSWER\b', 'was ANSWER', i)
    return i
    
df['qwords9_template'] = x2.apply(func2)
#print(df['qwords8_template'])
print('done')


  
def template10(row):
    lx  = row
    if lx == '':
        return lx    
    lx  = re.sub(r'\bmy\b', 'yourr', lx ) # To avoid words being converted back by the next lx ine
    lx  = re.sub(r'\byour\b', 'myy', lx )
    lx  = re.sub(r'\byou\b', 'II', lx )
    lx  = re.sub(r'\bI\b', 'youu', lx )
    lx  = re.sub(r'\bme\b', 'youu', lx )    
    lx  = re.sub(r'\bmine\b', 'yourss', lx )
    lx  = re.sub(r'\byours\b', 'minee', lx )
    
    lx  = re.sub(r'\bit like\b', '', lx ) 
    lx  = re.sub(r'\blikes me\b', 'likes you', lx )
    lx  = re.sub(r'\blike as\b', 'is ANSWER as', lx )
    lx  = re.sub(r'\bbe like as\b', 'as', lx )
    lx  = re.sub(r'\bit be like\b', '', lx )
    lx  = re.sub(r'\bit like as\b', 'as', lx )
    lx  = re.sub(r'\blike in\b', 'in', lx )
    lx  = re.sub(r'\blook like\b', '', lx )
    lx  = re.sub(r'\bbe like\b', '', lx )    
    lx  = lx .split()
    if len(lx ) > 1:
        if lx [-1] == 'like?':
            lx.pop(-1)
        # This is the conversion for qwords3
#        lx.lowercase(0) # Lowercase the first word
        lx = [lx[0].lower()] + lx[1:] # Lowercase first word
        lx.pop(1) # Remove second word
        if lx[1] == 'any':
            lx.pop(1)
                
        lx.insert(1, '/no')
        lx.insert(0, 'Yes/No, according to [SOURCE] there') # Add 'by' to the end of the sentence
        lx = [lx.replace('?', '') for lx in lx] # remove question mark
#        m = [m[0].capitalize()] + m[1:] # Capitalise first word

        # Correct the words
        lx  = [lx.replace('yourr', 'your') for lx  in lx ] 
        lx  = [lx.replace('myy', 'my') for lx  in lx ]
        lx  = [lx.replace('II', 'I') for lx  in lx ]
        lx  = [lx.replace('youu', 'you') for lx  in lx ]
        lx  = [lx.replace('yourss', 'yours') for lx  in lx ]
        lx  = [lx.replace('minee', 'mine') for lx  in lx ]
        
        # In case the word is now the first word, use capitals
        lx  = [lx.replace('Yourr', 'Your') for lx  in lx ]
        lx  = [lx.replace('Myy', 'My') for lx  in lx ]
        lx  = [lx.replace('Ii', 'I') for lx  in lx ]
        lx  = [lx.replace('Youu', 'You') for lx  in lx ]
        lx  = [lx.replace('Yourss', 'Yours') for lx  in lx ]
        lx  = [lx.replace('Minee', 'Mine') for lx  in lx ]        
        lx = " ".join(lx) + "."
#        lx = lx + ' According to [add RELIABLE SOURCE], [add reason from this source].'
#        print(lx)
        return lx
    else:
        return ''

df['qwords10_template'] = k3.apply(template10)
print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 3
############################################

def template11(row):
    ################ 1 Lines marked '1' are for actual usages, '2' for easier testing
    k = row
    if k == '':
        return k    
    # Inserting 'can' before the next verb, parsing using spacy
    sentence_spacy = nlp(k)
    pos = []
    for token in sentence_spacy:
        pos.append(token.tag_)
    ################ 1
    ################ 2    
    #k = row['qwords3'] 
    #pos = list(row['question1_pos'])
    ################ 2    

    # Find the index of the verb and add 'can' before verb
    try:
        x = pos.index("VB")
        k = k.split()
        k.insert(x, 'can')
    except ValueError: # If spacy finds no verb, we insert 'can' at index 1
        k = k.split()
        k.insert(1, 'can')
            
    k = " ".join(k)        
    k = re.sub(r'\bmy\b', 'yourr', k) # To avoid words being converted back by the next line
#    k = re.sub(r'\byour\b', 'myy', k)
#    k = re.sub(r'\byou\b', 'II!az', k)
    k = re.sub(r'\bI\b', 'youu', k)
    k = re.sub(r'\bmine\b', 'yourss', k)
    k = re.sub(r'\byours\b', 'minee', k)
    
    k = re.sub(r'\bit like\b', '', k) 
    k = re.sub(r'\blikes me\b', 'likes you', k)
    k = re.sub(r'\bbe like as\b', 'as', k)
    k = re.sub(r'\bit be like\b', '', k)
    k = re.sub(r'\bit like as\b', 'as', k)
    k = re.sub(r'\blike in\b', 'in', k)
    k = re.sub(r'\blook like\b', '', k)
    k = re.sub(r'\bbe like\b', '', k) 
    k = k.split()
    if len(k) > 1:
        if k[-1] == 'like?':
            k.pop(-1)
        # This is the conversion for qwords3
        k.pop(0) # Remove first two words
        k.pop(0)
        k.insert(len(k), 'at') # Add 'by' to the end of the sentence

        k = [k.replace('?', '') for k in k] # remove question mark
        k = [k[0].capitalize()] + k[1:] # Capitalise first word

        # Correct the words
        k = [k.replace('yourr', 'your') for k in k] 
        k = [k.replace('myy', 'my') for k in k]
        k = [k.replace('II!az', 'I') for k in k]
        k = [k.replace('youu', 'you') for k in k]
        k = [k.replace('yourss', 'yours') for k in k]
        k = [k.replace('minee', 'mine') for k in k]
        
        # In case the word is now the first word, use capitals
        k = [k.replace('Yourr', 'Your') for k in k]
        k = [k.replace('Myy', 'My') for k in k]
        k = [k.replace('Ii!az', 'I') for k in k]
        k = [k.replace('Youu', 'You') for k in k]
        k = [k.replace('Yourss', 'Yours') for k in k]
        k = [k.replace('Minee', 'Mine') for k in k]
        k = " ".join(k)
        return k
    else:
        return ''

#Using the dataframe df.apply, to select the question and corresponding POS tags (at start of function)
################ 2 
df['qwords11_template'] = k4.apply(template11) 
################ 2

################ 1
#df['qwords3_template'] = d.apply(template3)
################ 1
print('done')


  
def template12(row, max_verbs):
    L = row
    if L == '':
        return L
    doc = nlp(L)
    chunks = []
    pos = []
#    for token in nlp(L):
#        pos.append(token.tag_)
#    print(pos)
    if "Why does not" in doc.text:
        chunks = []
        pos = []
        verbs = 0
        for token in doc:
            if token.tag_ in ['VB', 'VBZ', 'VBP']:
                if verbs < max_verbs:

                    token_index = token.i  # this is the token index in the document
                    prev_token = doc[token_index - 1]  # the previous token in the document
                    if prev_token.tag_ == 'TO':
                        chunks.append(token.text_with_ws)  # token text + whitespace                        
                    elif token.text == 'do':
                        chunks.append("does not " + token.text + token.whitespace_)
                        verbs += 1
                    elif token.text == 'go':
                        chunks.append(token.text + 'es' + token.whitespace_)
                        verbs += 1                        
                    elif token.text == 'be':
                        chunks.append(token.text + token.whitespace_)
                        verbs += 1
                    elif token.text[-1] == 's':
                        chunks.append(token.text + token.whitespace_)
                        verbs += 1                  
                    else: 
                        count = 0
                        if count < 2:
                            if token.text == "doesn't":
                                chunks.append(token.text + token.whitespace_)
                                count += 0
                            else:
                                chunks.append("does not " + token.text + token.whitespace_)                            
                                count += 0
                else:
                    chunks.append(token.text_with_ws)
            else:
                chunks.append(token.text_with_ws)          
        L = chunks
        L.pop(0)
        L.pop(0)
        L.pop(0)
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:] # Only capitalizes first letter of first word
        L = [L.replace('haves', 'has') for L in L]        
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' because 6')
        L = "".join(L)
        return L 
    elif "Why does "  in doc.text:
        chunks = []
        pos = []
        verbs = 0
        # In case of a negation in the form of 'Why does X not ...":        
        if 'not' in L: 
            for token in doc:
                if token.text == 'not':
                    token_index = token.i  # this is the token index in the document
                    next_token = doc[token_index + 1]  # the next token in the document
                    if next_token.tag_ in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                        chunks.append('does' + token.whitespace_)              
                if token.tag_ in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                    if verbs < max_verbs:
                        token_index = token.i  # this is the token index in the document
                        prev_token = doc[token_index - 1]  # the previous token in the document
                        if prev_token.tag_ == 'TO':
                            chunks.append(token.text_with_ws)  # token text + whitespace
                        elif prev_token.text == 'not':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1
                        elif token.text == 'do':
                            chunks.append(token.text + 'es' + token.whitespace_)
                            verbs += 1
                        elif token.text == 'go':
                            chunks.append(token.text + 'es' + token.whitespace_)
                            verbs += 1                            
                        elif token.text == 'be':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1
                        elif token.text[-1] == 's':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1                            
                        elif token.text == 'does':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 0
                        else:
                            chunks.append(token.text + 's' + token.whitespace_)
                            verbs += 1
                    else:
                        chunks.append(token.text_with_ws)
                else:
                    chunks.append(token.text_with_ws)                        
        # In case of normal 'Why does ..." without negation:        
        else:
            for token in doc:
                if token.tag_ in ['VB', 'VBZ', 'VBP']:
                    if verbs < max_verbs:

                        token_index = token.i  # this is the token index in the document
                        prev_token = doc[token_index - 1]  # the previous token in the document
                        if prev_token.tag_ == 'TO':
                            chunks.append(token.text_with_ws)  # token text + whitespace

                        elif token.text == 'do':
                            chunks.append(token.text + 'es' + token.whitespace_)
                            verbs += 1
                        elif token.text == 'go':
                            chunks.append(token.text + 'es' + token.whitespace_)
                            verbs += 1                            
                        elif token.text == 'be':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1
                        elif token.text[-1] == 's':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1                            
                        elif token.text == 'does':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 0
                        else:
                            chunks.append(token.text + 's' + token.whitespace_)
                            verbs += 1
                    else:
                        chunks.append(token.text_with_ws)
                else:
                    chunks.append(token.text_with_ws)    
        L = chunks
        L.pop(0)
        L.pop(0)
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = [L.replace('haves', 'has') for L in L]
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' because 7')
        L = "".join(L)
        return L
    else: 
        if "Why doesn't" in doc.text:
            chunks = []
            pos = []
            verbs = 0
    #        for token in nlp(L):
    #            pos.append(token.tag_)        
            for token in doc:
                if token.tag_ in ['VB', 'VBZ', 'VBP']:
                    if verbs < max_verbs:

                        token_index = token.i  # this is the token index in the document
                        prev_token = doc[token_index - 1]  # the previous token in the document
                        if prev_token.tag_ == 'TO':
                            chunks.append(token.text_with_ws)  # token text + whitespace

                        if token.text == 'do':
                            chunks.append("doesn't " + token.text + token.whitespace_)
                            verbs += 1
                        elif token.text == 'go':
                            chunks.append(token.text + 'es' + token.whitespace_)
                            verbs += 1                        
                        elif token.text == 'be':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1
                        elif token.text[-1] == 's':
                            chunks.append(token.text + token.whitespace_)
                            verbs += 1                        
                        elif token.text == "doesn't":
                            chunks.append(token.text + token.whitespace_)
                            verbs += 0
                        else:
                            chunks.append("doesn't " + token.text + token.whitespace_)
                            verbs += 1
                    else:
                        chunks.append(token.text_with_ws)
                else:
                    chunks.append(token.text_with_ws)
            L = chunks
            L.pop(0)
            L.pop(0)
            L.pop(0)
            L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
            L = [L.replace('haves', 'has') for L in L]        
            L = [L.replace('?', '') for L in L]
            L.insert(len(L), ' because 8')
            L = "".join(L)
            return L

x3 = k5.apply(template12, max_verbs=4)

def func3(row):
    i = str(row)   
    i = re.sub(r'\bmy\b', 'yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bMy\b', 'Yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bI\b', 'youu', i)
    i = re.sub(r'\bmine\b', 'yourss', i)
    i = re.sub(r'\bme\b', 'youu', i)
    i = re.sub(r'\bams\b', 'are', i)
    
    i = re.sub(r'\bit like\b', '', i) 
    i = re.sub(r'\blikes me\b', 'likes you', i)
    i = re.sub(r'\blike as\b', 'is ANSWER as', i)
    i = re.sub(r'\bbe like as\b', 'as', i)
    i = re.sub(r'\bit be like\b', '', i)
    i = re.sub(r'\bit like as\b', 'as', i)
    i = re.sub(r'\blike in\b', 'in', i)
    i = re.sub(r'\blook like\b', '', i)
    i = re.sub(r'\bbe like\b', '', i) 
    i = i.split()

    # Correct the words
    i = [i.replace('yourr', 'your') for i in i] 
    i = [i.replace('myy', 'my') for i in i]
    i = [i.replace('II!az', 'I') for i in i]
    i = [i.replace('youu', 'you') for i in i]
    i = [i.replace('yourss', 'yours') for i in i]
    i = [i.replace('minee', 'mine') for i in i]
    
    # In case the word is now the first word, use capitals
    i = [i.replace('Yourr', 'Your') for i in i]
    i = [i.replace('Myy', 'My') for i in i]
    i = [i.replace('Ii!az', 'I') for i in i]
    i = [i.replace('Youu', 'You') for i in i]
    i = [i.replace('Yourss', 'Yours') for i in i]
    i = [i.replace('Minee', 'Mine') for i in i]
    i = " ".join(i)

    if 'is ANSWER as' in i:
        i = i.split()
        if i[-1] == 'is': # Present tense
            i.pop(-1) # Remove 'is' as last word
            i = " ".join(i) + "." # Add full stop
        if i[-1] == 'was': # Past tense
            i.pop(-1)
            i = " ".join(i) + "."
            i = re.sub(r'\bis ANSWER\b', 'was ANSWER', i)
    
    return i
    
df['qwords12_template'] = x3.apply(func3)
#print(df['qwords12_template'])

print('done')


  
def template13(row):
    L = row
    if L == '':
        return L
    doc = nlp(L)
    chunks = []
    pos = []
    for token in nlp(L):
        pos.append(token.tag_)
#    print(pos)
    vblist = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    if "How is " in doc.text:
        c = sum(i in vblist for i in pos)
        ran = False
        for token in doc:
            if 'similar ' in doc.text:
                if token.text == 'similar':
                    chunks.append('is 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'different ' in doc.text:
                if token.text == 'different':
                    chunks.append('is 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'possible ' in doc.text:
                if token.text == 'possible':
                    chunks.append('is 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'able ' in doc.text:
                if token.text == 'able':
                    chunks.append('is 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)                    
            elif c == 1:
                if token == doc[-1]: # if verb is last word
                    chunks.insert(len(doc), ' is 2')
                else:
                    chunks.append(token.text_with_ws)
            elif c > 1:
                if token.tag_ in vblist and not ran:
                    if token.text != 'is': # making sure verb is not 'is'
                        if token.i == 2: # making sure 'is' does not become first word
                            chunks.append(token.text + token.whitespace_)
                            ran = False                        
                        else:
                            chunks.append('is 4 ' + token.text + token.whitespace_)
                            ran = True
                else:
                    chunks.append(token.text_with_ws)
        L = chunks
        L.pop(0)
        if L[0] == 'is ':
            L.pop(0)
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' ...')
        L = "".join(L)
        return L
    elif "How are " in doc.text:
        c = sum(i in vblist for i in pos)
        ran = False
        for token in doc:
            if 'similar ' in doc.text:
                if token.text == 'similar':
                    chunks.append('are 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'different ' in doc.text:
                if token.text == 'different':
                    chunks.append('are 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'possible ' in doc.text:
                if token.text == 'possible':
                    chunks.append('are 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'able ' in doc.text:
                if token.text == 'able':
                    chunks.append('are 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)                    
            elif c == 1:
                if token == doc[-1]: # if verb is last word
                    chunks.insert(len(doc), ' are 2')
                else:
                    chunks.append(token.text_with_ws)
            elif c > 1:
                if token.tag_ in vblist and not ran:
                    if token.text != 'are': # making sure verb is not 'are'
                        if token.i == 2: # making sure 'are' does not become first word
                            chunks.append(token.text + token.whitespace_)
                            ran = False                        
                        else:
                            chunks.append('are 4 ' + token.text + token.whitespace_)
                            ran = True
                else:
                    chunks.append(token.text_with_ws)
        L = chunks
        L.pop(0)
        if L[0] == 'are ':
            L.pop(0)
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' [how:]') 
        L = "".join(L)
        return L    
    elif "How was " in doc.text:
        c = sum(i in vblist for i in pos)
        ran = False
        for token in doc:
            if 'similar ' in doc.text:
                if token.text == 'similar':
                    chunks.append('was 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'different ' in doc.text:
                if token.text == 'different':
                    chunks.append('was 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'possible ' in doc.text:
                if token.text == 'possible':
                    chunks.append('was 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'able ' in doc.text:
                if token.text == 'able':
                    chunks.append('was 1 ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)                  
            elif c == 1:
                if token == doc[-1]: # if verb is last word
                    chunks.insert(len(doc), ' was 2')
                else:
                    chunks.append(token.text_with_ws)

            elif c > 1:
                if token.tag_ in vblist and not ran:
                    if token.text != 'was': # making sure 'was' is not placed next to verb 'was'
                        if token.i == 2: # making sure 'are' does not become first word
                            chunks.append(token.text + token.whitespace_)
                            ran = False                        
                        else:
                            chunks.append('was 5 ' + token.text + token.whitespace_)
                            ran = True
                else:
                    chunks.append(token.text_with_ws)
        L = chunks
        L.pop(0)
        if L[0] == 'was ':
            L.pop(0)            
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' [how:]') 
        L = "".join(L)
        return L
    elif "How were " in doc.text:
        c = sum(i in vblist for i in pos)
        ran = False
        for token in doc:
            if 'similar ' in doc.text:
                if token.text == 'similar':
                    chunks.append('were 1a ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'different ' in doc.text:
                if token.text == 'different':
                    chunks.append('were 1b ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'possible ' in doc.text:
                if token.text == 'possible':
                    chunks.append('were 1c ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)
            elif 'able ' in doc.text:
                if token.text == 'able':
                    chunks.append('were 1d ' + token.text + token.whitespace_)
                else:
                    chunks.append(token.text_with_ws)                    
            elif c == 1:
                if token == doc[-1]: # if verb is last word
                    chunks.insert(len(doc), ' were 2')

                else:
                    chunks.append(token.text_with_ws)

            elif c > 1:
                if token.tag_ in vblist and not ran:
                    if token.text != 'were': # making sure 'was' is not placed next to verb 'were'
                        if token.i == 2: # making sure 'were' does not become first word
                            chunks.append(token.text + token.whitespace_)
                            ran = False                        
                        else:
                            chunks.append('were 5 ' + token.text + token.whitespace_)
                            ran = True
                else:
                    chunks.append(token.text_with_ws)
        L = chunks
        L.pop(0)
        if L[0] == 'were ':
            L.pop(0)            
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' [how:]') 
        L = "".join(L)
        return L    

x4 = k6.apply(template13)

def func4(row):
    i = str(row)   
    i = re.sub(r'\bmy\b', 'yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bMy\b', 'Yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bI\b', 'youu', i)
    i = re.sub(r'\bmine\b', 'yourss', i)
    i = re.sub(r'\bme\b', 'youu', i)
    i = re.sub(r'\bams\b', 'are', i)
    
    i = re.sub(r'\bit like\b', '', i) 
    i = re.sub(r'\blikes me\b', 'likes you', i)
    i = re.sub(r'\blike as\b', 'is ANSWER as', i)
    i = re.sub(r'\bbe like as\b', 'as', i)
    i = re.sub(r'\bit be like\b', '', i)
    i = re.sub(r'\bit like as\b', 'as', i)
    i = re.sub(r'\blike in\b', 'in', i)
    i = re.sub(r'\blook like\b', '', i)
    i = re.sub(r'\bbe like\b', '', i) 
    i = i.split()

    # Correct the words
    i = [i.replace('yourr', 'your') for i in i] 
    i = [i.replace('myy', 'my') for i in i]
    i = [i.replace('II!az', 'I') for i in i]
    i = [i.replace('youu', 'you') for i in i]
    i = [i.replace('yourss', 'yours') for i in i]
    i = [i.replace('minee', 'mine') for i in i]
    
    # In case the word is now the first word, use capitals
    i = [i.replace('Yourr', 'Your') for i in i]
    i = [i.replace('Myy', 'My') for i in i]
    i = [i.replace('Ii!az', 'I') for i in i]
    i = [i.replace('Youu', 'You') for i in i]
    i = [i.replace('Yourss', 'Yours') for i in i]
    i = [i.replace('Minee', 'Mine') for i in i]
    i = " ".join(i)

    if 'is ANSWER as' in i:
        i = i.split()
        if i[-1] == 'is': # Present tense
            i.pop(-1) # Remove 'is' as last word
            i = " ".join(i) + "." # Add full stop
        if i[-1] == 'was': # Past tense
            i.pop(-1)
            i = " ".join(i) + "."
            i = re.sub(r'\bis ANSWER\b', 'was ANSWER', i)
    
    return i

df['qwords13_template'] = x4.apply(func4)
#print(df['qwords13_template'])

print('done')


  
############################################
# TRANSFORM QUESTION TO ANSWER TEMPLATE 1+2
############################################
# There are still small mistakes due to spaCy not correctly recognising verbs

#s = "What should be done to get rid of dandruff?"
#s = "What should toddlers eat for breakfast?"
#s = "What should I do if I am afraid of failure?"
#s = "What should I gift my husband on our first wedding anniversary?"
#df = pd.DataFrame({'sentence':[s]})
#k7 = df['sentence']

def template14(row):
    L = row
    if L == '':
        return L
    doc = nlp(L)
    chunks = []
    pos = []
    vblist = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    if 'What should' in doc.text:
        ran = False
        for token in doc:
            pos.append(token.tag_)
            if token.tag_ in vblist and not ran:
                if token.i == 2: # If third word is verb, pass with no change
                    chunks.append(token.text + token.whitespace_)
                    ran = True
                else:
                    chunks.append('should ' + token.text + token.whitespace_)
                    ran = True                          
            else:
                chunks.append(token.text_with_ws)
        L = chunks
        L = " ".join(L)
        L = L.split()
        
        if L[1] == 'should' and L[3] == 'should':
            L.pop(1)

        if L[1] == 'someone ':
            L.pop(1)
            L.insert(1, 'one ')
        L = [L.replace('?', '') for L in L]
        L.insert(len(L), ' is [XYZ:]')
        L = [L[0][0].capitalize() + L[0][1:]] + L[1:]
        L = " ".join(L)
        return L
    else:
        return""        

x7 = k7.apply(template14)
#print(x)

def func7(row):
    i = str(row)
    i = re.sub(r'\bmy\b', 'yourr', i) # To avoid words being converted back by the next line
    i = re.sub(r'\bI\b', 'youu', i)
    i = re.sub(r'\bmine\b', 'yourss', i)
    i = re.sub(r'\bdos\b', 'does', i)
    i = re.sub(r'\bme\b', 'youuu', i)
    i = re.sub(r'\bam\b', 'are', i)
    i = re.sub(r'\bour\b', 'yourr', i)
    
    i = re.sub(r'\bit like\b', '', i) 
    i = re.sub(r'\blikes me\b', 'likes you', i)
    i = re.sub(r'\blike as\b', 'is ANSWER as', i)
    i = re.sub(r'\bbe like as\b', 'as', i)
    i = re.sub(r'\bit be like\b', '', i)
    i = re.sub(r'\bit like as\b', 'as', i)
    i = re.sub(r'\blike in\b', 'in', i)
    i = re.sub(r'\blook like\b', '', i)
    i = re.sub(r'\bbe like\b', '', i) 
    i = i.split()

    # Correct the words
    i = [i.replace('yourr', 'your') for i in i] 
    i = [i.replace('myy', 'my') for i in i]
    i = [i.replace('II!az', 'I') for i in i]
    i = [i.replace('youu', 'you') for i in i]
    i = [i.replace('yourss', 'yours') for i in i]
    i = [i.replace('minee', 'mine') for i in i]
    i = [i.replace('youuu', 'you') for i in i]
    i = [i.replace('oouur', 'our') for i in i]

    # In case the word is now the first word, use capitals
    i = [i.replace('Yourr', 'Your') for i in i]
    i = [i.replace('Myy', 'My') for i in i]
    i = [i.replace('Ii!az', 'I') for i in i]
    i = [i.replace('Youu', 'You') for i in i]
    i = [i.replace('Yourss', 'Yours') for i in i]
    i = [i.replace('Minee', 'Mine') for i in i]
    i = [i.replace('Meeer', 'Me') for i in i]    
    i = " ".join(i)
    print(i)

    if 'is ANSWER as' in i:
        i = i.split()
        if i[-1] == 'is': # Present tense
            i.pop(-1) # Remove 'is' as last word
            i = " ".join(i) + "." # Add full stop
        if i[-1] == 'was': # Past tense
            i.pop(-1)
            i = " ".join(i) + "."
            i = re.sub(r'\bis ANSWER\b', 'was ANSWER', i)
    return i
    
df['qwords14_template'] = x7.apply(func7)
#print(df['qwords8_template'])
print('done')


  
df = df.drop(["sentence", "qwords1", "qwords2", "qwords3", "qwords3", "qwords4", "qwords5", "qwords5x","qwords6", "qwords7", "qwords8", "qwords9", "qwords10", "qwords11", "qwords12", "qwords13", "qwords14"], axis = 1)
df.at[0, df.loc[0].astype(bool).idxmax()]


  
s = df.T[0]
sentence = s[s != ""]
print(sentence)


