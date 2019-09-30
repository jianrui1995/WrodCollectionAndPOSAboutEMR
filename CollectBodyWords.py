"""
收集Jian_DATA.json 下面的身体部位词。并处理
"""
import json
class CollectBodyWords():
    def __int__(self):
        pass

    def ReadFile(self):
        '''
        读取文件，将部位词总结。
        :return:
        '''
        f = open("Data/Jian_DATA.json", "r", encoding="utf8")
        self.list_sentence = json.load(f)
        f.close()
        self.list_words=[]
        for i in self.list_sentence:
            list_entity=i["entities"]
            for data in list_entity:
                if data["label_type"]=="解剖部位":
                    self.list_words.append(data["entity"])
            print("|",end="")
        f2=open("Data/json/WordsRepository_Body.json","w",encoding="utf8")
        self.list_words=list(set(self.list_words))
        print("\n")
        print(len(self.list_words))
        json.dump(self.list_words,f2,ensure_ascii=False)
        f2.close()

    def ReturnOneWord(self):
        '''
        返回只有一个字的部位词
        :return:
        '''
        list_words=[]
        for word in self.list_words:
            if len(list(word))==1:
                list_words.append(word)
        for word in list_words:
            if word in list_words:
                self.list_words.remove(word)
        f2 = open("Data/json/WordsRepository_Body.json", "w", encoding="utf8")
        json.dump(self.list_words,f2,ensure_ascii=False)
        f2.close()
        return  list_words

if __name__=="__main__":
    CBW=CollectBodyWords()
    CBW.ReadFile()
    print(CBW.ReturnOneWord())
