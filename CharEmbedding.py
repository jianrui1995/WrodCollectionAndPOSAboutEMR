from gensim.models import Word2Vec
import json


class originalFile():
    def __init__(self):
        self.f_ori=open("Data/originalText.txt","r",encoding="utf8")
        self.f_seg=open("Data/originalText_seg.txt","r",encoding="utf8")
        self.ori=[list(data) for data in self.f_ori.readlines()]
        self.seg=[data.strip().split(" ") for data in self.f_seg.readlines()]
    def iter_ori(self):
        yield list(self.f_ori.readline().strip())

    def iter_seg(self):
        yield self.f_seg.readline().split(" ")



sentence=originalFile()
<<<<<<< HEAD
model=Word2Vec(sentence,size=200,workers=16,iter=500)
model.save("Data/models/word2voc.model")
=======
for i in range(60,141,40):
    for j in range(200,301,50):
        model=Word2Vec(sentence.ori,size=j,workers=32,iter=i,min_count=3)
        model.save("Data/models/word2voc_char_size"+str(j)+"_iter"+str(i)+".model")
for i in range(60,141,40):
    for j in range(200,301,50):
        model=Word2Vec(sentence.ori,size=j,workers=32,iter=i)
        model.save("Data/models/word2voc_word_size"+str(j)+"_iter"+str(i)+".model")

>>>>>>> f6c96f2cc199b47a4fdf1cb544ec0adeed313acd
