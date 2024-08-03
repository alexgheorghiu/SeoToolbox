"""Based on https://www.youtube.com/watch?v=GQ6OT2HyfPs"""
import argparse

import pandas as pd
import numpy as np

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

from list_utils import read_file, write_lines

import nltk
nltk.download('stopwords')


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster

stemmer = PorterStemmer()  # ex: stemmer.stem('roofing')

sw = stopwords.words('romanian')  #Values can be 'english', 'romanian'


# ex: sw

def tokenizer(keyword):
    """ex: tokenizer('When to buy houses on desks')"""
    return [stemmer.stem(w) for w in keyword.split(' ')]


# ex: tfid = TfidfVectorizer(use_idf=False, norm=None)
# ex: pd.DataFrame(tfid.fit_transform(keywords).toarray(), index=keywords, columns=tfid.get_feature_names_out())
def group(keywords, stop_words):
    tfidf = TfidfVectorizer(tokenizer=tokenizer, stop_words=stop_words)
    X = pd.DataFrame(tfidf.fit_transform(keywords).toarray(),
                     index=keywords, columns=tfidf.get_feature_names_out())
    c = cluster.AffinityPropagation()
    X['pred'] = c.fit_predict(X)
    return dict(zip(X.index, X.pred))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Groups a list of keywords')
    parser.add_argument('--input', default='keyword_grouping_input.txt')
    parser.add_argument('--output', default='keyword_grouping_output.txt')
    args = parser.parse_args()

    file_path = args.input
    keywords = list(read_file(file_path))

    dict_df = group(keywords, sw)
    # print(dict_df)

    sorted_x = sorted(dict_df.items(), key=lambda kv: kv[1])
    # print(sorted_x)

    a_map = map(lambda x: f'{x[0]}, {x[1]}', sorted_x)
    # print("\n".join(lst))
    # print(len(lst))
    write_lines(list(a_map), args.output)
    # print("\n".join(lst))
