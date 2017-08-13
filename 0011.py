def judge(path):
    fulltext=[]
    with open(path) as f:
        for line in f:
            fulltext.append(line.strip('\n'))
    return fulltext
if __name__=='__main__':
    path=r"C:\Users\chauncey\Desktop\filtered_words.txt"
    word=input("Input:")
    if word in judge(path):
        print("Freedom")
    else:
        print("Human Rights")
