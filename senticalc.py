

import  re
import pickle
import nltk
import csv
from datetime import datetime
import datetime
import unicodedata
import pandas as pd



def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString  

def sentiscore(s):
    f = open(s,'r' ,encoding='utf8', errors='ignore')
    line = f.read()
    tokens = nltk.word_tokenize(line)
    words = [word for word in tokens if word.isalpha()]
   # print(words)
    p=nltk.pos_tag(words)
    #print(p)
    Output = [item for item in p if  item[1] == 'NNS' or item[1]=='NNP' or item[1]=='NN' or item[1]=='NNPS' or item[1]=='JJ' or item[1]=='JJR' or item[1]=='JJS' or item[1]=='RB' or item[1]=='RBR' or item[1]=='RBS' or item[1]=='VB' or item[1]=='VBD' or item[1]=='VBN' or item[1]=='VBP' or item[1]=='VBG' or item[1]=='VBZ']
   # print(Output)
    x = open("senti.txt" )
    s1=x.read()
    s = replaceMultiple(s1,['#1','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13','#14','#15'] , '')       
    x.close()
    x=open("senti.txt","w")
    x.write(s)
    x.close()
    list1=[]
    p=open('senti.txt')
    line=p.readline()
    while line:
        tokens = nltk.word_tokenize(line)
        slice_object = slice(5)
        q=tokens[slice_object]
        list1.append(q)
        line = p.readline()
    #print("******************************************************************")
       
   # print(list1)
    p.close()
    d=[]
    for j in Output:
        p=list(j)
        if p[1] in ['NNP','NNS','NN','NNPS']:
            p[1]='n'
        if p[1] in ['JJ','JJR','JJS']:
            p[1]='a'
        if p[1] in ['RB','RBR','RBS']:
            p[1]='r'
        if p[1] in ['VB','VBD','VBN','VBP','VBG','VBZ']:
            p[1]='v'
        d.append(tuple(p))
    #print(d)
    l=len(d)
    l1=len(list1)
    pos=0
    neg=0
    for i in d:
        q=list(i)
        for j in range(l1):
            if q[0]==list1[j][4]:
                pos=pos+float(list1[j][2])
                neg=neg+float(list1[j][3])
    pos=pos/l
    neg=neg/l
    return pos,neg
                  
"""
                
# Main function
client = TwitterClient()

#socialawarness=['social distancing India','quarantine in India','isolation in India','community spread in India','lockdown in India','W.H.O India','guideline in India','awarness in India','covid-19 spread india','Sanitization in india','PPE N95 mask in India','confirmed case in india','prevent in india','stay safe from corona in india','hygiene in india','truma in india','child affected in india']
#,'corporate sector in india','shutdown economy in india','industry in india','jobless in india in corona time','companies in india','market in india','investment in india in corona time','economic growth in india','economic fallout in india','manufacturing sector in india','RBI in india','unemployment in corona time in india','farmer in india','capital investment in india in corona time'
#covideconomy=['economy effect in india','atmanirbhar bharat package','covid-19 economy in india','lockdown economy in india','industry in india','corporate sector effect in india','shutdown economy in india','economic growth in india','companies in india','market in india','jobless in india in corona time','economic fallout in india','manufacturing sector in india','rural agricultur economy','RBI in india','unemployment in corona time in india','farmer in india','capital investment in india in corona time']
count = 0
list1=[]
listid=[]
#q=['Impact of Coronavirus on Education in India','school college off','education in india','lockdown education in india','covid-19 eduction in india','school in india','college education in india','examination in india','exam postpone in india','university education in india','final year exam in india','education session in india','lockdown education in india','online education in india','online class in india','online child education in india']


"""

list1=[]

with open('June.csv', 'r') as file:
    reader = csv.reader(file)
    count=0
    for row in reader:
        print(row[2])
        list1.append(row[2])
        count=count+1
        if count>100:
            break

                
#print(list1)



for tweet in list1:
    
    tweet=tweet.lower()
    tweet=re.sub(r"that's","that is",tweet)
    tweet=re.sub(r"what's","what is",tweet)
    tweet=re.sub(r"where's","where is",tweet)
    tweet=re.sub(r"it's","it is",tweet)
    tweet=re.sub(r"i'm","i am",tweet)
    tweet=re.sub(r"she's","she is",tweet)
    tweet=re.sub(r"he's","he is",tweet)
    tweet=re.sub(r"they're ","they are",tweet)
    tweet=re.sub(r"who're","who are",tweet)
    tweet=re.sub(r"ain't","am not",tweet)
    tweet=re.sub(r"wouldn't","would not",tweet)
    tweet=re.sub(r"shouldn't","should not",tweet)
    tweet=re.sub(r"can't","can not",tweet)
    tweet=re.sub(r"couldn't","could not",tweet)
    tweet=re.sub(r"won't","will not",tweet)
    twwet=re.sub(r"\w","",tweet)
    twwet=re.sub(r"\d","",tweet)
    twwet=re.sub(r"s+[a-z]\s+","",tweet)
    twwet=re.sub(r"\s+[a-z]$","",tweet)
    twwet=re.sub(r"^[a-z]\s+","",tweet)
    twwet=re.sub(r"\s+","",tweet)

list2 = [x.replace('\n', '') for x in list1]   
list3 = [x.replace('https', '') for x in list1] 
s1='05-05-20' 
s2='.txt'
s=s1+s2 
f=open(s,'w',encoding='utf-8')
for i in list3:
    f.write(i + '\n')
f.close()         
print("Calculating sentiscore")  

pos,neg=sentiscore(s)
print(pos)
print(neg) 

"""
print(count)
a=[]
date=s1
a.append(date)
a.append(count)
a.append(pos)
a.append(neg)  
p=[]
p.append(a)
with open('education.csv', 'a',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(p)  

"""
    