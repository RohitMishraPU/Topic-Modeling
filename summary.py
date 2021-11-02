import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization import summarize
import gensim
def summarizeText(data):
    print(gensim.summarization.keywords(data))
    return summarize(data)
