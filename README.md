# WrodCollectionAndPOSAboutEMR
###py文件功能说明：  
* ForWord.py  
    从Data/症状分词.txt中读取字典，做成初步的标注词库。把结果放入到Data/json/wordrepository.json文件中  
    遍历语料文件，收集已经标注的词，打入词库，方便辅助分词。收集的词按照分类放到字典中，并且存放到json。
* QueryTess.py  
    两种方法创建，一种是从wordrepository.json文件中创建，一种是直接注入词注入到查询树中，并且将词加入到wordrepository.json。
* CollectBodyWords.py  
    对Jian_DATA.json的文件进行总结   
* StatisticSentence.py  
    分词，然后按照句号，逗号切分，然后统计出借个切分的句子，分词之后的长度。按照长度放入不同的文件中，文件位置Data/collectionSentence/。  
* CharEmbedding.py  
    对字粒度进行word2vec训练。  
* LabelByHand.py  
    文件的手动标注过程。
