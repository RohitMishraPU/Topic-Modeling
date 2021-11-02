import logging
import gensim
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora,models,similarities
def match(data):
    
    documents = ["Human machine interface for lab abc computer applications",
                 "A survey of user opinion of computer system response time",
                 "The EPS user interface management system",
                  "System and human system engineering testing of EPS",
                  "Relation of user perceived response time to error measurement",
                  "The generation of random binary unordered trees",
                  "The intersection graph of paths in trees",
                  "Graph minors IV Widths of trees and well quasi ordering",
                  "Graph minors A survey"]
    stoplist = set('for a of the and to in'.split())
    docs = [[word for word in document.lower().split() if word not in stoplist]
             for document in documents]
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in docs:
            for token in text:
                frequency[token] += 1

    docs = [[token for token in text if frequency[token] > 1]
             for text in docs]

    dictionary = corpora.Dictionary(docs)
    print(dictionary.token2id)
    corpus=[dictionary.doc2bow(text)for text in docs]
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    print(data)
    new_doc = data
    print(new_doc)
    new_vec = dictionary.doc2bow(new_doc.lower().split())
    print(new_vec)
    vec_lsi=lsi[new_vec]
    index = similarities.MatrixSimilarity(lsi[corpus])
    sims=index[vec_lsi]
    print(sims)
    return(sims)
    






