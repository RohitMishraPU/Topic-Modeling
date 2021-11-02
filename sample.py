# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:19:22 2017

@author: MISHRA
"""

import logging
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import simple_preprocess
from collections import defaultdict
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def readDoc1():
    with open('data3.txt','r') as myfile:
        data=myfile.read().replace('\n', '')
    return data
def readDoc2():
    with open('data.txt','r') as myfile:
        data=myfile.read().replace('\n', '')
    return data

def tokenDoc(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

def checkFreq(texts):
    frequency = defaultdict(int)
    for token in texts:
        frequency[token] += 1

    texts =[token for token in texts if frequency[token] > 1]
    return texts

doc1=readDoc1()
doc1=tokenDoc(doc1)
doc1=checkFreq(doc1)
dict1=corpora.Dictionary([doc1])
corpus=[dict1.doc2bow(doc1)]
lsi = models.LsiModel(corpus, id2word=dict1, num_topics=2)
index = similarities.MatrixSimilarity(lsi[corpus])
doc2=readDoc2()
doc2_bow=dict1.doc2bow(doc2.lower().split())
print(doc2_bow)
doc2_lsi=lsi[doc2_bow]
print(doc2_lsi)
sims=index[doc2_lsi]
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims)