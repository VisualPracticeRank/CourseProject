import math
import sys
import time
import metapy
import pytoml
import os

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

def create_inverted_index(file):
    #Generate tmp config file

    #Make Inverted Index


    #Compress Inverted index

    #Pass Path to Compressed Index
    return 1

def load_inverted_index(index_as_string):
    return 1

def run_query(q):
    cfg = "config.toml"
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker(cfg)
    ev = metapy.index.IREval(cfg)

    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query_cfg = cfg_d['query-runner']
    if query_cfg is None:
        sys.exit(1)

    top_k = 10

    query = metapy.index.Document()
    query.content(q.strip())
    r = ranker.score(idx, query, top_k)
    print(r)
    return r

run_query(sys.argv[1])
