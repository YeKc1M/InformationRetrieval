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
新闻检索：采用Dynamic Indexing（新闻要求实时性，能够即时获得最新的消息）。存储采用Distributed Indexing? collections are too large to perfom index construction efficiently on a single machine.
# lab3
权值计算和文档得分
1. 编写结算tfidf基本算法
2. 计算查询文档得分
3. 编写计算权值的改进方法，即对tf进行归一化处理，wfidf
    1. wf=1+log(tf)
    2. wf=0.5+(0.5*tf/max(tf))
# lab4
向量模型
查询语句：1. 中国美国大豆市场 2. 高考成绩发布 3. 公安制止犯罪 4. 石油泄漏 5. 全球经济发展
# lab5
语言模型
1. 将向量模型中所有文档集的bag of words 作为`Mc`
2. 建立每篇文档的`Md`
3. 利用概率模型的三种计算方法，确定`Md`中每个term的先验概率值
    1. $ P(x_i | R)=0.5 $  $ P(x_i | \overline{R})=\frac{n_i}{N} $
    2. $ P(x_i | R)=\frac{V_i}{V} $  $ P(x_i | \overline{R})=\frac{n_i-V_i}{N-V}
    3. $ P(x_i | R)=\frac{V_i+0.5}{V+1} $  $ P(x_i | \overline{R})=\frac{n_i-V+0.5}{N-V+1}
4. 设计检索界面，测试5条查询需求，给出排序结果。$ P(w | d)=\lambda P(w|M_d)+(1-\lambda )P(w | M_c)