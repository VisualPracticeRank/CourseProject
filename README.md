# Visual Practice Rank
## Goal
The goal of this project is to create a visual representation of a supplied ranking function in a form that is comparable to mdoern search engines withe the display of additional data that would be only in the background

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
You can upload your dataset by selecting `Dataset` in the homepage and fill up and upload the appropriate files needed:
1. Name
2. Description
3. Data
4. Qrels
5. Queries

and select Upload

### Model
In addition to the default models available ('OkapiBM25','PivotedLength','AbsoluteDiscount','JelinekMercer','DirichletPrior'), you can upload your own custom models.

# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.
