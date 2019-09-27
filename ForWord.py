"""
遍历症状成分词，并且分类组成字库
"""
import  json
with open("data/症状成分词.txt","r",encoding="utf8") as f:
    list_word2type_s=f.readlines()
    dict={}
    for data in list_word2type_s:
        list_word2type=data.strip().split(" ")
        if list_word2type[1] not in dict:
            dict[list_word2type[1]]=[list_word2type[0]]
        else:
            if list_word2type[0] not in dict[list_word2type[1]]:
                dict[list_word2type[1]].append(list_word2type[0])
    print(len(dict.keys()))
    print(dict.keys())
f2=open("Data/json/WordRepository.json","w",encoding='Utf8')
json.dump(dict,f2,ensure_ascii=False)