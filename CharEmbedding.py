from gensim.models import Word2Vec
import json


class originalFile():
    def __init__(self):
        with open("Data/Jian_DATA.json","r",encoding="utf8") as f:
            self.dict_ori=json.load(f)

    def __iter__(self):
        for dict_data in self.dict_ori:
            yield list(dict_data["originalText"])

sentence=originalFile()
model=Word2Vec(sentence,size=200,workers=16)
model.save("Data/models/word2voc.model")