import sys
import metapy

def setup_idx(folder_name):
    return metapy.index.make_inverted_index(folder_name + "/config.toml")

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

idx = setup_idx(sys.argv[1])

ranker = ranker_func(idx, sys.argv[2])

query = metapy.index.Document()
query.content(sys.argv[3])

print(ranker.score(idx, query, num_results=5))
#idx.unique_terms()

#print("idx.num_docs()")
#print(idx.num_docs())

#print("idx.unique_terms()")
#print(idx.unique_terms())

#print("idx.avg_doc_length()")
#print(idx.avg_doc_length())

#print("idx.total_corpus_terms()")
#print(idx.total_corpus_terms())
