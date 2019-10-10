from QueryTree import BuildQueryTree
import json
class LabelByHand():
    def __init__(self):
        pass

    def PassRepeat(self,i):
        '''
        去掉文件中的重复对象。
        :param i: 处理到几个文件
        :return:
        '''
        paths=["Data/collectSentence/"+str(num)+".txt" for num in range(1,i+1)]
        for path in paths:
            with open(path,"r+",encoding="utf8") as f:
                list_words=f.readlines()
                f.seek(0)
                f.truncate()
                list_words=list(set(list_words))
                for data in list_words:
                    print(data,file=f,end="")
                f.close()
        print("去重完成!   ",[data for data in paths])

    def Label(self,i):
        BQT = BuildQueryTree(StartType=2)
        paths=["Data/collectSentence/"+str(num)+".txt" for num in range(1,i+1)]
        with open(paths[i-1],"r+",encoding="utf8") as f:
            list_sentence=f.readlines()
            f.seek(0)
            f.truncate()
            for words in list_sentence:
                words=json.loads(words.strip())
                for i in range(len(words)):
                    label=BQT.SearchQueryTreeWithWord(words[i].split("***")[0],1)
                    words[i]=words[i].split("***")[0]+"==="+label
                print(json.dumps(words,ensure_ascii=False),file=f,end="\n")

if __name__=="__main__":
    LBH=LabelByHand()

    # 去掉重复的词
    # LBH.PassRepeat(5)
    for i in range(1,6):
        LBH.Label(i)