import json

class BuildQueryTree():
    def __init__(self,StartType=1):
        '''
        :param StartType:1： 从Data/json/WordRepository.json文件中读取词库构建查询树; 2:从已有的查询树中，读取查询树。如果需要打入新的词，那
        么可以调用类其他方法
        :return:
        '''
        self.StartType=StartType
        if self.StartType==1:
            with open("Data/json/WordRepository.json","r",encoding="utf8") as f:
                self.dict=json.load(f)
            self.dict_PosQueryTree=self.CreatNode(label="Start")
            self.dict_NegQueryTrss=self.CreatNode(label="Start")
            for data in self.dict.items():
                self.InsertQueryTree(self.dict_PosQueryTree,self.dict_NegQueryTrss,data[0],data[1])
            print("字典构造完成！！！放入json")

        if self.StartType==2:
            fpos=open("Data/json/PosQueryTree.json","r",encoding="utf8")
            fneg=open("Data/json/NegQueryTree.json","r",encoding="utf8")
            fwords = open("Data/json/WordRepository.json", "r", encoding="utf8")
            self.dict_PosQueryTree=json.load(fpos)
            self.dict_NegQueryTrss=json.load(fneg)
            self.wordrepositpry = json.load(fwords)
            fpos.close()
            fneg.close()
            fwords.close()


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
        IsInsert=False
        for word in list_words:
            list_char=list(word)
            dict_PosQueryTree,IsInsert=self.InsertQueryTreeWithOneWord(dict_PosQueryTree,label,list_char)
            list_char.reverse()
            dict_NegQueryTree,IsInsert=self.InsertQueryTreeWithOneWord(dict_NegQueryTree,label,list_char)
            if self.StartType==2 and IsInsert :
                self.wordrepositpry[label].append(word)
        f2 = open("Data/json/PosQueryTree.json", "w", encoding="utf8")
        json.dump(self.dict_PosQueryTree, f2, ensure_ascii=False)
        f2.close()
        f3 = open("Data/json/NegQueryTree.json", "w", encoding="utf8")
        json.dump(self.dict_NegQueryTrss, f3, ensure_ascii=False)
        f3.close()

    def InsertQueryTreeWithOneWord(self,QueryTree,label,list_char):
        '''
        单树，单词插入
        :param QueryTree:需要被查询树
        :param label: 需要插入的词的标签
        :param list_char:需要插入词的汉字序列
        :return:完成插入的查询树
        '''
        IsInsert=False
        temp=QueryTree
        labeled="NotEnd"
        for i in range(0,len(list_char)):
            if list_char[i] in temp["next"]:
                temp=temp["next"][list_char[i]]
                labeled=temp["label"]
            else:
                temp["next"][list_char[i]]= self.CreatNode(value=list_char[i])
                temp=temp["next"][list_char[i]]
                IsInsert=True
        temp["label"]=label
        if not IsInsert:
            if labeled !=label:
                f=open("Data/collectSentence/DisputWord.txt","a",encoding="utf8")
                print("".join(list_char),"  old: ",labeled,"  new: ",label,file=f,end="\n")
                f.close()
        return QueryTree,IsInsert

    def InsertQueryTreeWithWords(self,label,words):
        '''
        当需要单独插入词典的时候，调用的函数
        :param label: 词列表的标签
        :param words: 需要插入的词列表
        :return:
        '''
        self.InsertQueryTree(self.dict_PosQueryTree, self.dict_NegQueryTrss, label, words)
        fwords=open("Data/json/WordRepository.json","w",encoding="utf8")
        json.dump(self.wordrepositpry,fwords,ensure_ascii=False)
        print("完成词入库！！！")

    def SearchQueryTess(self,sentence,dire=1):
        '''
        查询句子返回句子的序列标注。
        注意：这里方向，此列表没有反向。
        :param sentence: 句子
        :param dire: 使用的查询树的字典是正向还是负向的字典。dire=1是正向的，dire是负向的。
        :return:
        '''
        list_char=list(sentence)
        i=0
        list_labeled =[]
        while i < len(list_char):
            if dire==1:
                temp=self.dict_PosQueryTree
            if dire==2:
                temp=self.dict_NegQueryTrss
            list_found_maybe =[]
            list_found =[]
            label_maybe ='NotEnd'
            label ='NotEnd'
            for j in range(i,len(list_char)):
                if list_char[j] in temp["next"]:
                    temp=temp["next"][list_char[j]]
                    label_maybe=temp["label"]
                    list_found_maybe.append(temp["value"])
                    if label_maybe!="NotEnd":
                        label=label_maybe
                        list_found=list_found_maybe
                else:
                    break
            if label!="NotEnd":
                list_labeled.append(label+"_B")
                for k in range(1,len(list_found)):
                    list_labeled.append(label+"_I")
                i=i+len(list_found)
            else:
                list_labeled.append("O")
                i=i+1

    def SearchQueryTreeWithWord(self,word,dire=1):
        '''
        输入要查询的词，直接返回label。
        :param word:要查询的词
        :param dire: 查询的方向，1 为正向，2 为负向。
        :return:
        '''
        list_char=list(word)
        label="NotEnd"
        if dire==1:
            temp=self.dict_PosQueryTree
        if dire==2:
            list_char=list_char.reverse()
            temp=self.dict_NegQueryTrss
        for char in list_char:
            if char in temp["next"]:
                temp=temp["next"][char]
                label=temp["label"]
            else:
                label="NotEnd"
                break
        return label
if __name__=="__main__":
    BQT=BuildQueryTree(StartType=2)
    BQT.SearchQueryTreeWithWord("头",1)