# WrodCollectionAndPOSAboutEMR
###py文件功能说明：  
* ForWord.py  
    从Data/症状分词.txt中读取字典，做成初步的标注词库。把结果放入到Data/json/wordrepository.json文件中
* BuildQueryTess.py  
    两种方法创建，一种是从wordrepository.json文件中创建，一种是直接注入词注入到查询树中，并且将词加入到wordrepository.json。
* CollectBodyWords.py  
    对Jian_DATA.json的文件进行总结