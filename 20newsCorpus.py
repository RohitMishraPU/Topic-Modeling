import logging
import os
import sys
import re
import tarfile
import itertools

import nltk
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

import gensim
from gensim import corpora
from gensim.parsing.preprocessing import STOPWORDS

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

def process_message(message):
    message = gensim.utils.to_unicode(message, 'latin1').strip()
    blocks = message.split(u'\n\n')
    # skip email headers (first block) and footer (last block)
    content = u'\n\n'.join(blocks[1:])
    return content

def iter_20newsgroups(fname, log_every=None):
    """
    Yield plain text of each 20 newsgroups message, as a unicode string.

    The messages are read from raw tar.gz file `fname` on disk (e.g. `./data/20news-bydate.tar.gz`)

    """
    extracted = 0
    with tarfile.open(fname, 'r:gz') as tf:
        for file_number, file_info in enumerate(tf):
            if file_info.isfile():
                if log_every and extracted % log_every == 0:
                    logging.info("extracting 20newsgroups file #%i: %s" % (extracted, file_info.name))
                content = tf.extractfile(file_info).read()
                yield process_message(content)
                extracted += 1



class Corpus20News(object):
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        
        for message in iter_20newsgroups(self.fname):
            yield self.tokenize(message)

    def split_words(self, text, stopwords=STOPWORDS):
        """
        Break text into a list of single words. Ignore any token that falls into
        the `stopwords` set.

        """
        return [word
                for word in gensim.utils.tokenize(text, lower=True)
                if word not in STOPWORDS and len(word) > 3]


    def tokenize(self, message):
        
        text = u' '.join(self.split_words(message))
        return text.split()


tokenized_corpus = Corpus20News('./20news-18828.tar.gz')
#print(list(itertools.islice(tokenized_corpus, 2)))
dictionary=corpora.Dictionary(tokenized_corpus)
dictionary.save('./dict/newsdictionary.dict')
corpus=[dictionary.doc2bow(text)for text in tokenized_corpus]
corpora.MmCorpus.serialize('./dict/newsCorpus.mm',corpus)
print(dictionary)
