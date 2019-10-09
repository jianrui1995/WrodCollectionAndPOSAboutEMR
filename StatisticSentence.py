'''
统计句子中的句子长度分布
'''
import json
import re
import pkuseg

def StatisticSentence(path):
    dict_num={}
    f1=open("Data/originalText.txt","a",encoding="utf8")
    with open(path,"r",encoding="utf8") as f:
        list_dict=f.readlines()
        path=[]
        for i in range(1,11):
            path.append("Data/collectSentence/"+str(i)+".txt")
        for str_data in list_dict:
            if str_data.startswith(u'\ufeff'):
                str_data= str_data.encode('utf8')[3:].decode('utf8')
            dict_data1=json.loads(str_data.strip())
            origText=dict_data1["originalText"]
            print(origText)
            print(origText,file=f1,end="\n")
    f1.close()
            # 切分，单词。
            # list_sentence=re.split(r"[。，]",origText)

            # # 将从1到10个字的描述摘抄出来。做成一个txt
            # for sentence in list_sentence:
            #     if len(sentence)>0 and len(sentence)<11:
            #         f1=open("Data/collectSentence/"+str(len(sentence))+".txt","a",encoding="utf8")
            #         print(sentence,file=f1,end="\n")
            #         f1.close()

            #统计每个句子的字数量数量
    #         for sentence in list_sentence:
    #             if len(sentence) not in dict_num:
    #                 dict_num[len(sentence)]=1
    #             else:
    #                 dict_num[len(sentence)]=dict_num[len(sentence)]+1
    # return dict_num

# 调用方法
# dict_num1=StatisticSentence("Data/subtask1_training_part1.txt")
# dict_num2=StatisticSentence("Data/subtask1_training_part2.txt")

# 计算各个数量中，句子的占比。
# for k,v in dict_num2.items():
#     if k not in dict_num1:
#         dict_num1[k]=v
#     else:
#         dict_num1[k]=dict_num1[k]+v
# total=0
# for k,v in dict_num1.items():
#     total=total+v
# for i in range(95):
#     print(i," ",dict_num1[i]," ",dict_num1[i]/total)

# 文本级别的分词。
# if __name__=="__main__":
#     pkuseg.test('Data/originalText.txt', 'Data/originalText_seg.txt', nthread=10)

def collectWords():
    path = []
    for i in range(1, 11):
        path.append("Data/collectSentence/" + str(i) + ".txt")
    f1=open("Data/originalText_seg.txt","r",encoding="utf8")
    list_sentence=f1.readlines()
    for sentence in list_sentence:
        list_words=re.split(r"[。，]",sentence.strip())
        for words in list_words:
            list_words_B=words.split(" ")
            for i in range(len(list_words_B)-1,-1,-1):
                if list_words_B[i]=="":
                    list_words_B.pop(i)
            if len(list_words_B)<6 and len(list_words_B)>0 :
                json_list_words=json.dumps(list_words_B,ensure_ascii=False)
                f2=open(path[len(list_words_B)-1],"a",encoding="utf8")
                print(json_list_words,file=f2,end="\n")
                f2.close()

collectWords()