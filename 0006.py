from collections import Counter,defaultdict
import os,re
def word_counter(path,num=1):
    for file in os.listdir(path):
        with open(path+os.sep+file,'rt') as f:
            fulltext=f.read()
            words_list=re.findall(r'[A-Za-z]+',fulltext)
            word_counts=Counter(words_list)
            top_tree=word_counts.most_common(num)
            print(top_tree)
if __name__=="__main__":
    path=r"C:\Users\chauncey\Desktop\aa"
    word_counter(path,1)
