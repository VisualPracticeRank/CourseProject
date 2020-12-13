# Visual Practice Rank
## Goal
The goal of this project is to create a visual representation of a supplied ranking function in a form that is comparable to modern search engines with the display of additional data that would be only in the background

## Getting Started
### Installation
1. Create a virtual environment using conda:

   `conda create -n [your-env-name] python=3.6 anaconda`

   e.g. `conda create -n vpr python=3.6 anaconda`


2. Activate the virtual environment

   `conda activate [your-env-name]`

   e.g. `conda activate vpr`


3. Install the packages in requirements.txt

   `conda install --file requirements.txt`

### Running the Django server
Running the Django server
While in the CourseProject folder, cd into VPR, list of the files and folders and you will see a file called manage.py. Run the following command:

   `python3 manage.py runserver`

A browser with the application will pop-up.

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
