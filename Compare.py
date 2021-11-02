import logging
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import simple_preprocess
from collections import defaultdict
import re
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def tokenDoc(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

def checkFreq(texts):
    frequency = defaultdict(int)
    for token in texts:
        frequency[token] += 1

    texts =[token for token in texts if frequency[token] > 1]
    return texts

def CompareDoc(data1,data2):
    data1=re.sub('\.!?@','',data1)
    data2=re.sub('\.!?@','',data2)
    doc1=tokenDoc(data1)
    doc1=checkFreq(doc1)
    dict1=corpora.Dictionary([doc1])
    corpus=[dict1.doc2bow(doc1)]
    lsi = models.LsiModel(corpus, id2word=dict1, num_topics=2)
    index = similarities.MatrixSimilarity(lsi[corpus])
    doc2_bow=dict1.doc2bow(data2.lower().split())
    print(doc2_bow)
    doc2_lsi=lsi[doc2_bow]
    print(doc2_lsi)
    sims=index[doc2_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print(sims)
    if sims[0][1]>0:
        return True
    else:
        return False
