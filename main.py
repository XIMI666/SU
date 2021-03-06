# -*- coding:utf-8 -*-
import time
from tkinter import *

import gensim  # 语料包
import jieba  # 汉语言处理包


def run1():
    global text1, text2
    t1 = time.time()
    try:
        punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，！【】（）、。：； ’‘……￥·"""
        dicts = {i: '' for i in punctuation}
        punc_table = str.maketrans(dicts)  # 去除标点符号

        a1 = inp1.get() + ".txt"
        f = open(a1, encoding="utf-8")
        data1 = f.read()
        new_data1 = data1.translate(punc_table)
        text1 = jieba.lcut(new_data1)  # 被测试文本
        f.close()

        f = open("orig.txt", encoding="utf-8")
        data2 = f.read()
        new_data2 = data2.translate(punc_table)
        text2 = jieba.lcut(new_data2)  # 测试文本
        f.close()

    except FileNotFoundError:
        txt.insert(END, "找不到文件，请重新输入")

    def calc_similarity(x, y):
        texts = [x, y]
        dictionary = gensim.corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        similarity_ = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
        test_corpus_1 = dictionary.doc2bow(x)
        cosine_sim = similarity_[test_corpus_1][1]
        return cosine_sim

    if __name__ == '__main__':
        similarity = calc_similarity(text1, text2)
        t2 = time.time()
        txt.insert(END, "\n文章相似度： %.2f%%" % (similarity * 100))  # 追加显示运算结果
        txt.insert(END, "\n运行结束，查询总时间为： %.2f" % (t2 - t1) + "s")
        file = open('result.txt', 'w') # 将结果写入文件
        txt.insert(END, "\n结果被存入pythonProject1/result.txt" )
        file.write("\n文章相似度： %.2f%%" % (similarity * 100))

        inp1.delete(0, END)  # 清空输入

root = Tk()
root.geometry('480x240')
root.title('查重系统')

lb1 = Label(root, text='请输入需要查询的文件名')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)

btn1 = Button(root, text='开始运行', command=run1)
btn1.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

txt = Text(root)
txt.place(rely=0.6, relheight=0.4)

root.mainloop()  # UI界面设计

