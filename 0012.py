# -*- coding: utf-8 -*-
def read_file(path):
    with open(path) as f:
        fulltext=f.read().split('\n')
    return fulltext
def judge(filtered,sentence):
    index_len=[]
    for word in filtered:
        index=sentence.find(word)
        if index!=-1:
            index_len.append(word)
    return index_len
if __name__=='__main__':
    path=r'C:\Users\chauncey\Desktop\filtered_words.txt'
    fulltext=read_file(path)
    sentence=input('>')
    for w in judge(fulltext,sentence):
        sentence=sentence.replace(w,len(w)*'*')
    print(sentence)


