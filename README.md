# Visual Practice Rank
## Goal
The goal of this project is to create a visual representation of a supplied ranking function in a form that is comparable to modern search engines with the display of additional data that would be only in the background

## Project Presentation
https://mediaspace.illinois.edu/media/t/1_3s2zdgys

## Getting Started
### Installation
1. Create a virtual environment using conda:

   `conda create -n [your-env-name] python=3.6`

   e.g. `conda create -n vpr python=3.6 anaconda`


2. Activate the virtual environment

   `conda activate [your-env-name]`

   e.g. `conda activate vpr`

3. Download the repository
   
   `git clone https://github.com/VisualPracticeRank/CourseProject.git`

3. Install the packages in requirements.txt

   `cd CourseProject`
   
   `pip install -r requirements.txt`

### Running the Django server
While in the CourseProject folder, cd into VPR, list of the files and folders and you will see a file called manage.py. Run the following command:
   
   `python3 manage.py makemigrations`
   
   `python3 manage.py migrate --run-snycdb`
   
   `python3 manage.py runserver`

A browser with the application will pop-up, or you can head to `127.0.0.1:8000`

If you are running this on a VM, instead of `python3 manage.py runserver`, you can run the following command:
   `python3 manage.py runserver 0.0.0.0:8000`

Then, head over to `[your ip]:8000`, e.g. `18.219.133.210:8000`

### Shutting down the Django server
If you want to shutdown the Django server, you can do `ctrl+c` in the terminal to shut down the server. You can also deactivate the virtual environment with this command: 

   `conda deactivate`

## Features
### Dataset
You can upload your dataset by selecting `Dataset` on the homepage and fill in and upload the appropriate files needed:
1. Name
2. Description
3. Data
4. Qrels
5. Queries

and select Upload.

### Model
In addition to the default models available ('OkapiBM25', 'PivotedLength', 'AbsoluteDiscount', 'JelinekMercer', 'DirichletPrior'), you can upload your own custom models.

You can upload your own model (ranker) by selecting `Model` on the homepage and fill in the textboxes:
1. Name
2. Description
3. Model

and select Add.

### Query
After selecting the dataset and model that you want to use, you can specify a query in the textbox and select Search. You will get the top 10 documents with the highest score in your model, displayed in descending order.

### Step Through
This functionality allows you to step through the queries.txt file you specified when uploading the dataset and observe the changes in the ndcg score and other various stats.

After selecting the dataset and model that you want to use, you can select Step Through. You can use the '<<' and '>>' buttons to step through and step out.

## How It Works
### Overview
This program is implemented using Django (Python, HTML, SQLite3) as the frontend and metapy (and Python) as the backend. 

### Frontend
The dataset details are stored in the webui_dataset. The dataset, qrels, and queries files are stored in a folder, with a unique name generated by the system, under the `dataset` folder. The webui_dataset has the following fields: id (primary key), name, description, data, qrels, queries.

When a dataset is being uploaded, the documents in the dataset is loaded into `webui_document` with the following fields: id (primary key), document_id, body, dataset_id (foreign key to webui_dataset.id).

When a model is being uploaded, the model is loaded into `webui_model` with the following fields: id (primary key), description, model, name. Before storing the actual model, it will be encoded to base64.

After you can select a dataset, model, and query, you click on Search. Then frontend (in `view.py`) will call the backend (`search_eval.py`) and pass the following variables: `folder` (folder where the dataset is stored), `model`, `query`.

For the iteration feature, the frontend will send these information to the backend: `folder` (path to dataset), `model`. After receiving the response from the backend, the frontend will display the following information: `query` (as specified in the queries.txt), `NDCG`, a table of the following information: the score of the document, size of the document, unique terms in the document, and snippit of the body.

### Backend
The backend (`search_eval.py`) will these variables from the frontend: `folder`, `model`, `query`. It will first change its directory to `[folder_to_dataset]/datasets` and build an inverted index.

Then, it will determine if the `model` is one of the defaults ('OkapiBM25', 'PivotedLength', 'AbsoluteDiscount', 'JelinekMercer', 'DirichletPrior'). If it's not, then it will decode the string (using base64) and build the ranker.

Finally, it will run the ranker with the inverted index, query for the top 10 documents and return the top 10 documents, and their score.

For the iteration feature, the backend will utilize the qrels.txt and queries.txt that were uploaded when uploading the dataset. It will return a list of list:
   1. results[0] = list of top k articles
   2. results[1] = list of ndcg
   3. results[2] = list of running avg ndcg
   4. results[3] = list of queries


## Reference
1. Chase Geiglem, 2017. [2-search-and-ir-eval.ipynb] (https://github.com/meta-toolkit/metapy/blob/master/tutorials/2-search-and-ir-eval.ipynb).
