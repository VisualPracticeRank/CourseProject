import metapy
import os
import sys
import uuid
import shutil
import faulthandler; faulthandler.enable()

def make_folder(name):
    try:
        os.makedirs(folder_name)
        os.makedirs(folder_name+"/data")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
def setup_folder(data, folder_name):
    shutil.copy("template/stopwords.txt", folder_name)
    shutil.copy(data, folder_name + "/data/data.dat")

    f = open(folder_name + "/data/line.toml", "w")
    f.write("type = \"line-corpus\"")
    f.close()

    f = open(folder_name + "/config.toml", "w")
    f.write("prefix = \"./" + folder_name + "\"")
    f.write("\nstop-words = \"stopwords.txt\"")
    f.write("\n\ndataset = \"data\"")
    f.write("\ncorpus = \"line.toml\"")
    f.write("\nindex = \"idx-" + folder_name + "\"")
    
    f.write("\n\n[[analyzers]]")
    f.write("\nmethod = \"ngram-word\"")
    f.write("\nngram = 1")
    f.write("\nfilter = \"default-unigram-chain\"")

    f.close()

def setup_idx(folder_name):
    metapy.index.make_inverted_index(folder_name + "/config.toml")
    shutil.copytree("idx-" + folder_name, folder_name + "/idx-" + folder_name)
    shutil.rmtree("idx-" + folder_name, ignore_errors = False)

def return_name(name):
    print(name)
    return name


folder_name = uuid.uuid4().hex # generate unique folder name
make_folder(folder_name)

data = sys.argv[1]
setup_folder(data, folder_name)
setup_idx(folder_name)

return_name(folder_name)
