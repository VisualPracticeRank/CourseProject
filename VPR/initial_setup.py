import metapy
import os
import sys
import uuid
import shutil
import faulthandler; faulthandler.enable()

def make_folder(name):
    try:
        os.makedirs(name)
        os.makedirs(name+"/dataset")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
def setup_folder(data, folder):
    shutil.copy("template/stopwords.txt", folder)
    shutil.copy(data, folder + "/dataset/dataset.dat")

    f = open(folder + "/dataset/line.toml", "w")
    f.write("type = \"line-corpus\"")
    f.close()

    f = open(folder + "/config.toml", "w")
    #f.write("prefix = \"./" + folder + "\"")
    f.write("prefix = \".\"")
    f.write("\nstop-words = \"stopwords.txt\"")
    f.write("\n\ndataset = \"dataset\"")
    f.write("\ncorpus = \"line.toml\"")
    f.write("\nindex = \"idx-" + folder + "\"")
    
    f.write("\n\n[[analyzers]]")
    f.write("\nmethod = \"ngram-word\"")
    f.write("\nngram = 1")
    f.write("\nfilter = \"default-unigram-chain\"")

    f.close()

def setup_idx(folder_path, folder_name):
    cur_dir = os.getcwd()
    os.chdir(folder_path)
    metapy.index.make_inverted_index("config.toml")
    os.chdir(cur_dir)
    #ishutil.copytree("./idx-" + folder_name, folder_path + "/idx-" + folder_name)
    #shutil.rmtree("./idx-" + folder_name, ignore_errors = False)

def run_setup(data):
    folder_name = uuid.uuid4().hex # generate unique folder name
    folder_path = './datasets/' + folder_name
    make_folder(folder_path)

    #data = sys.argv[1]
    setup_folder(data, folder_path)
    setup_idx(folder_path, folder_name)
    
    #print(folder_path)
    return folder_path
