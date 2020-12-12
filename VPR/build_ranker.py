import sys
import metapy

def setup_idx(cfg):
    return metapy.index.make_inverted_index(cfg)

def ranker_func(idx, type):
    if type == "OkapiBM25":
        print("OkapiBM25")
        return metapy.index.OkapiBM25()
    elif type == "PivotedLength":
        print("PivotedLength")
        return metapy.index.PivotedLength()
    elif type == "AbsoluteDiscount":
        print("AbsoluteDiscount")
        return metapy.index.AbsoluteDiscount()
    elif type == "JelinekMercer":
        print("JelinekMercer")
        return metapy.index.JelinekMercer()
    elif type == "DirichletPrior":
        print("DirichletPrior")
        return metapy.index.DirichletPrior()

def initialize(type):
    #idx = metapy.index.make_inverted_index(cfg)

    if type == "OkapiBM25":
        print("OkapiBM25")
        return metapy.index.OkapiBM25()
    elif type == "PivotedLength":
        print("PivotedLength")
        return metapy.index.PivotedLength()
    elif type == "AbsoluteDiscount":
        print("AbsoluteDiscount")
        return metapy.index.AbsoluteDiscount()
    elif type == "JelinekMercer":
        print("JelinekMercer")
        return metapy.index.JelinekMercer()
    elif type == "DirichletPrior":
        print("DirichletPrior")
        return metapy.index.DirichletPrior()

    #query = metapy.index.Document()
    #query.content(sys.argv[3])

    #print(ranker.score(idx, query, num_results=5))
#idx.unique_terms()

#print("idx.num_docs()")
#print(idx.num_docs())

#print("idx.unique_terms()")
#print(idx.unique_terms())

#print("idx.avg_doc_length()")
#print(idx.avg_doc_length())

#print("idx.total_corpus_terms()")
#print(idx.total_corpus_terms())
