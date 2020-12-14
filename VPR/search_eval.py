import math
import sys
import time
import metapy
import pytoml
import os
import base64
import initial_setup
#import build_ranker

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

#def load_ranker(cfg_file):
#    return metapy.index.OkapiBM25()

def return_score_data(idx, query):
    avg_dl = idx.avg_doc_length()
    num_docs = idx.num_docs()
    total_terms = idx.total_corpus_terms()
    query_length = len(query)
    #t_id = idx.unique_terms()

    #query_term_weight = 0
    #doc_count = idx.doc_freq(t_id)
    #corpus_term_count = idx.total_num_occurences(t_id)
    # Document
    #d_id = 0
 #   doc_term_count = idx.doc_term_count()
 #   doc_size = idx.doc_size()
 #   doc_unique_terms = idx.unique_terms()

    corpus_unique_term = idx.unique_terms()
    #term_count = []
    #for i in range(corpus_unique_terms):
    #    term_count.append((idx.term_text(i), idx.term_text(i)))
    
    doc_size = []
    for i in range(num_docs):
        doc_size.append((i, idx.doc_size(i)))

    doc_term_count = []
    for i in range(corpus_unique_term):
        doc_term_count.append((idx.term_text(i), idx.doc_freq(i)))
    
    corpus_term_count = []
    for i in range(corpus_unique_term):
        corpus_term_count.append((idx.term_text(i), idx.total_num_occurences(i)))
    
    l_l = []
    l_l.append(avg_dl)
    l_l.append(num_docs)
    l_l.append(total_terms)
    l_l.append(query_length)

    l_l.append(doc_size)
    l_l.append(doc_term_count)

    l_l.append(corpus_term_count)
    l_l.append(corpus_unique_term)
    
#    l_l.append(doc_size)
#    l_l.append(doc_unique_terms)
#    l_l.append(doc_term_count)

#    print(doc_size)
#    print(doc_unique_terms)
#    print(doc_term_count)

    return l_l

def ranker_func(model):
    if model == 'OkapiBM25':
        return metapy.index.OkapiBM25()
    elif model == "PivotedLength":
        return metapy.index.PivotedLength()
    elif model == "AbsoluteDiscount":
        return metapy.index.AbsoluteDiscount()
    elif model == "JelinekMercer":
        return metapy.index.JelinekMercer()
    elif model == "DirichletPrior":
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

    if q == "-1":
        ev = metapy.index.IREval(cfg)
        #print("\n\nhere\n\n\n")
        with open(cfg, 'r') as fin:
            cfg_d = pytoml.load(fin)

        query_cfg = cfg_d['query-runner']
        if query_cfg is None:
            sys.exit(1)

        query_path = query_cfg.get('query-path', 'queries.txt')
        query_start = query_cfg.get('query-id-start', 0)

        ndcg = 0.0
        num_queries = 0

        #print('Running queries')
        r_l = []
        n_l = []
        with open(query_path) as query_file:
            for query_num, line in enumerate(query_file):
                query.content(line.strip())
                results = ranker.score(idx, query, top_k)
                r_l.append(results)
                curr_ndcg = ev.ndcg(results, query_start + query_num, top_k)
                ndcg += curr_ndcg
                n_l.append(curr_ndcg)
                num_queries += 1
        ndcg = ndcg / num_queries
       
        l = []
        l.append(r_l)
        #l.append(return_score_data(idx, q.strip()))
        l.append(n_l)
        l.append(ndcg)
        print(l)
        return l
    else:
        query.content(q.strip())
        r = ranker.score(idx, query, top_k)

        l = [[r]]
        print(l)
        return l


run_query(sys.argv[1], sys.argv[2], sys.argv[3])
