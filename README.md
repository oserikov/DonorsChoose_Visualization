> **@oserikov: ** in this fork I naively removed the necessity to use Mongo. As the dataset is not that big actually, pandas serves fine, yet even pandas can be dropped, as we only read the whole csv into a list of dicts. The data itself is part of a larger project, and turns out to be hosted on [Kaggle](https://www.kaggle.com/c/kdd-cup-2014-predicting-excitement-at-donors-choose) novadays. Notice that you have to merge two csv's to get the desired one: `projects.csv` and `donations.csv`. Find the merged lightweight file here in this repo.


# DonorsChoose_Visualization
* Source Code for my blog post: [Interactive Data Visualization with D3.js, DC.js, Python, and MongoDB](http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/)

#Visit my Blog : http://adilmoujahid.com

## Getting started

The dependencies for the project can be installed using

    $ pip install -r requirements.txt

You can use ``Vagrant`` to start a machine with a MongoDB instance running

    $ vagrant up

To initialize the database you need to download the data

    $ wget https://s3.amazonaws.com/open_data/csv/opendata_projects.zip && unzip opendata_projects.zip

and import it

    $ mongoimport -d donorschoose -c projects --type csv --file /vagrant/opendata_projects.csv -headerline
