import math
import sys
import time
import metapy
import pytoml
import os
import base64
import initial_setup
import build_ranker

class CustomRanker(metapy.index.RankingFunction):
    def __init__(self, rtn):
        self.rtn = rtn
        super(CustomRanker, self).__init__()

    def score_one(self, sd):
        # Security - Good for testing, but should become more secure.
        return eval(self.rtn
            .replace("{{avg_dl}}", str(sd.avg_dl))
            .replace("{{num_docs}}", str(sd.num_docs))
            .replace("{{total_terms}}", str(sd.total_terms))
            .replace("{{query_length}}", str(sd.query_length))
            .replace("{{t_id}}", str(sd.t_id))
            .replace("{{query_term_weight}}", str(sd.query_term_weight))
            .replace("{{doc_count}}", str(sd.doc_count))
            .replace("{{corpus_term_count}}", str(sd.corpus_term_count))
            .replace("{{d_id}}", str(sd.d_id))
            .replace("{{doc_term_count}}", str(sd.doc_term_count))
            .replace("{{doc_size}}", str(sd.doc_size))
            .replace("{{doc_unique_terms}}", str(sd.doc_unique_terms))
            )

def load_ranker(cfg_file):
    return metapy.index.OkapiBM25()

def return_score_data(idx, query):
    avg_dl = idx.avg_dog_length()
    num_docs = idx.num_docs()
    total_terms = idx.total_corpus_terms()
    query_length = len(query)
    t_id = 0
    query_term_weight = 0
    doc_count = idx.doc_freq(t_id)
    corpus_term_count = idx.total_num_occurences(t_id)
    # Document
    d_id = 0
    doc_term_count = 0
    doc_size = 0
    doc_unique_terms = 0

def ranker_func(model):
    if model == 'OkapiBM25':
        #print("BM25")
        return metapy.index.OkapiBM25()
    elif model == "PivotedLength":
        #print("PivotedLength")
        return metapy.index.PivotedLength()
    elif model == "AbsoluteDiscount":
        #print("AbsoluteDiscount")
        return metapy.index.AbsoluteDiscount()
    elif model == "JelinekMercer":
        #print("JelinekMercer")
        return metapy.index.JelinekMercer()
    elif model == "DirichletPrior":
        #print("DirichletPrior")
        return metapy.index.DirichletPrior()
    else:
        return CustomRanker(base64.b64decode(model).decode())

def run_query(folder, model, q):
    filepath = "./datasets/" + folder
    os.chdir(filepath)
    cfg = "../../config.toml"
    idx = metapy.index.make_inverted_index(cfg)
    ranker = ranker_func(model)
    top_k = 10
    query = metapy.index.Document()
    query.content(q.strip())
    r = ranker.score(idx, query, top_k)
    print(r)
    return r


run_query(sys.argv[1], sys.argv[2], sys.argv[3])
