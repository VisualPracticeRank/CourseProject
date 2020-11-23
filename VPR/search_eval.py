import math
import sys
import time
import metapy
import pytoml
import os

def load_ranker(cfg_file):
    return metapy.index.OkapiBM25()

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
