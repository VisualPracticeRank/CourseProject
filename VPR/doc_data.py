import metapy
import os
import sys

def return_doc_data(folder):
    filepath = "./datasets/" + folder
    os.chdir(filepath)
    cfg = "../../config.toml"
    idx = metapy.index.make_inverted_index(cfg)
    num_docs = idx.num_docs()
    doc_data = []
    for x in range(num_docs):
        doc_data.append({'doc_size': idx.doc_size(x), 'unique_terms': idx.unique_terms(x)})
    corpus_data = {'unique_terms': idx.unique_terms(), 'avg_dl': idx.avg_doc_length(), 'num_docs': idx.num_docs(), 'total_terms': idx.total_corpus_terms()}
    print({'doc_data': doc_data, 'corpus_data': corpus_data})

return_doc_data(sys.argv[1])
