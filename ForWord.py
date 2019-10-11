'''
遍历症状成分词，并且分类组成字库
'''
# import  json
# with open("data/症状成分词.txt","r",encoding="utf8") as f:
#     list_word2type_s=f.readlines()
#     dict={}
#     for data in list_word2type_s:
#         list_word2type=data.strip().split(" ")
#         if list_word2type[1] not in dict:
#             dict[list_word2type[1]]=[list_word2type[0]]
#         else:
#             if list_word2type[0] not in dict[list_word2type[1]]:
#                 dict[list_word2type[1]].append(list_word2type[0])
#     print(len(dict.keys()))
#     print(dict.keys())
# f2=open("Data/json/WordRepository.json","w",encoding='Utf8')
# json.dump(dict,f2,ensure_ascii=False)

'''
遍历语料文件，收集已经标注的词，打入词库，方便辅助分词。收集的词按照分类放到字典中，并且存放到json。
'''

import json
dict_words={}
def collectwords(path,dict):
    with open(path,"r",encoding="utf8") as f:
        list_line=f.readlines()
    for ori in list_line:
        if ori.startswith(u'\ufeff'):
            ori = ori.encode('utf8')[3:].decode('utf8')
        dic_line=json.loads(ori.strip())
        list_char=list(dic_line["originalText"])
        for entity in dic_line["entities"]:
            if entity["label_type"] in dict.keys():
                dict[entity["label_type"]].append("".join(list_char[entity["start_pos"]:entity["end_pos"]]))
            else:
                dict[entity["label_type"]]=[]
                dict[entity["label_type"]].append("".join(list_char[entity["start_pos"]:entity["end_pos"]]))
collectwords("Data/subtask1_training_part1.txt",dict_words)
collectwords("Data/subtask1_training_part2.txt",dict_words)
for k,v in dict_words.items():
    v=list(set(v))
    dict_words[k]=v
f=open("Data/json/WordsRepository_AllEntities.json","w",encoding="utf8")
json.dump(dict_words,f,ensure_ascii=False)
f.close()
