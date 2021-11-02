import logging
from gensim import corpora,models
from gensim.parsing.preprocessing import STOPWORDS
import pyLDAvis.gensim

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

dictionary = corpora.Dictionary.load('./dict/newsdictionary.dict')
corpus=corpora.MmCorpus('./dict/newsCorpus.mm')

lda = models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=50, update_every=0, passes=10)
p=pyLDAvis.gensim.prepare(lda,corpus,dictionary)
pyLDAvis.save_html(p,"visual.html")
