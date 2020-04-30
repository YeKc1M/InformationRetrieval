# lab 1
数据源 news_tensite_xml.smarty.dat
lab1的内容包括index.py（实现倒排索引），logical.py（实现简单的AND/OR/NOT/ANDNOT/ORNOT操作），实现ANDALL和ORALL操作的优化
# lab2
新增的数据源 new_data_xml.dat
lab2的内容包括：
1. 将term和posting分开存储（index.py），写入dictionary.txt和posting.txt
2. 实现dynamic indexing（将新数据并入原数据），写入到dynamicTerm.txt和dynamicPosting.txt
3. 对term实现1-gram index索引（1gramIndex.py）
4. 构建title的zone index（zoneIndex.py）
5. 实现文本查询（AND）和域查询（AND）