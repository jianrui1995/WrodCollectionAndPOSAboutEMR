import json

class BuildQueryTree():
    def __init__(self,StartType=1):
        '''

        :param type:1： 从Data/json/WordRepository.json文件中读取词库构建查询树; 2:从已有的查询树中，读取查询树。如果需要打入新的词，那
        么可以调用类其他方法

        :return:
        '''
        if StartType==1:
            with open("Data/json/WordRepository.json","r",encoding="utf8") as f:
                self.dict=json.load(f)
            self.dict_PosQueryTree=self.CreatNode(label="Start")
            self.dict_NegQueryTrss=self.CreatNode(label="Start")
            for data in self.dict.items():
                self.InsertQueryTree(self.dict_PosQueryTree,self.dict_NegQueryTrss,data[0],data[1])
            print("字典构造完成！！！放入json")

        if StartType==2:
            fpos=open("Data/json/PosQueryTree.json","r",encoding="utf8")
            fneg=open("Data/json/NegQueryTree.json","r",encoding="utf8")
            self.dict_PosQueryTree=json.load(fpos)
            self.dict_NegQueryTrss=json.load(fneg)


    def CreatNode(self,value=None,label="NotEnd"):
        '''
        返回一个查询树的节点。大bug：当把label标签改为列表的时候，就会发现，修改一个字典，另一个字典也会被修改？ 永远不懂大bug。
        :return:
        '''
        dictA={}
        dictA["label"]=label
        dictA["next"]={}
        dictA["value"]=value
        return dictA

    def InsertQueryTree(self,dict_PosQueryTree,dict_NegQueryTree,label,list_words):
        '''
        多数，词列表插入
        :param dict_PosQueryTree:
        :param dict_NegQueryTree:
        :param label:词的分类标记
        :param list_words:词列表
        :return:
        '''
        for word in list_words:
            list_char=list(word)
            dict_PosQueryTree=self.InsertQueryTreeWithOneWord(dict_PosQueryTree,label,list_char)
            list_char.reverse()
            dict_NegQueryTree=self.InsertQueryTreeWithOneWord(dict_NegQueryTree,label,list_char)
        f2 = open("Data/json/PosQueryTree.json", "w", encoding="utf8")
        json.dump(self.dict_PosQueryTree, f2, ensure_ascii=False)
        f3 = open("Data/json/NegQueryTree.json", "w", encoding="utf8")
        json.dump(self.dict_NegQueryTrss, f3, ensure_ascii=False)
        f2.close()
        f3.close()

    def InsertQueryTreeWithOneWord(self,QueryTree,label,list_char):
        '''
        单树，单词插入
        :param QueryTree:需要被查询树
        :param word: 需要插入的单词
        :return:
        '''
        temp=QueryTree
        for i in range(0,len(list_char)):
            if list_char[i] in temp["next"]:
                temp=temp["next"][list_char[i]]
            else:
                temp["next"][list_char[i]]= self.CreatNode(value=list_char[i])
                temp=temp["next"][list_char[i]]
        temp["label"]=label
        return QueryTree

    def InsertQueryTreeWithWords(self,label,words):
        self.InsertQueryTree(self.dict_PosQueryTree, self.dict_NegQueryTrss, label, words)
        fwords=open("Data/WordRepository.json","r",encoding="utf8")
        wordrepositpry=json.load(fwords)
        for word in words:
            if word  not in wordrepositpry[label]:
                wordrepositpry[label].append(word)
        fwords.close()
        fwords=open("Data/WordRepository.json","w",encoding="utf8")
        json.dump(wordrepositpry,fwords,ensure_ascii=False)
        print("完成词入库！！！")
if __name__=="__main__":
    BQT=BuildQueryTree(StartType=1)