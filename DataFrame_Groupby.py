#!/Users/kristof/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-
__author__ = 'L.I. sezeezezeztre'

import pandas as pd
import numpy as np

# Load Data
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_csv('dataSet/users.txt', engine='python',
                    sep='::', header=None, names=userHeader, dtype=np.dtype("O"))

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_csv('dataSet/movies.txt', engine='python',
                     sep='::', header=None, names=movieHeader, dtype=np.dtype("O"))

ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('dataSet/ratings.txt', engine='python',
                      sep='::', header=None, names=ratingHeader, dtype=np.dtype("O"))

# Merge data
mergeRatings = pd.merge(pd.merge(users, ratings), movies)

# Clone DataFrame


def cloneDF(df):
<<<<<<< HEAD
    return pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy()).apply(pd.to_numeric,errors='ignore')
=======
    return pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy()).apply(pd.to_numeric, errors="ignore")
#    pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy())
#    apply(pd.to_numeric, errors='ignore')
>>>>>>> aa81f8a14a454cf8950eff94fc70967b4778cd87


# Show Films with more votes. (groupby + sorted)
numberRatings = cloneDF(mergeRatings)
numberRatings = numberRatings.groupby(
    'title').size().sort_values(ascending=False)
print('Films with more votes: \n%s' % numberRatings[:10])
print('\n==================================================================\n')


# Show avg ratings movie (groupby + avg)
avgRatings = cloneDF(mergeRatings)
avgRatings = avgRatings.groupby(['movie_id', 'title']).mean()
print('Avg ratings: \n%s' % avgRatings['rating'][:10])
print('\n==================================================================\n')


# Show data ratings movies (groupby + several funtions)
dataRatings = cloneDF(mergeRatings)
dataRatings = dataRatings.groupby(['movie_id', 'title'])[
    'rating'].agg(['mean', 'sum', 'count', 'std'])
print('Films ratings info: \n%s' % dataRatings[:10])
print('\n==================================================================\n')


# Show data ratings movies, applying a function (groupby + lambda function)
myAvg = cloneDF(mergeRatings)
#myAvg = myAvg.groupby(['movie_id', 'title'])['rating'].agg(
#    {'SUM': np.sum, 'COUNT': np.size, 'AVG': np.mean, 'myAVG': lambda x: x.sum() / float(x.count())})
myAvg = myAvg.groupby(['movie_id', 'title'])['rating'].agg(
    {np.sum, np.size, np.mean, lambda x: x.sum() / float(x.count())},
    col_names = ('SUM', 'COUNT', 'AVG', 'myAVG')
)
print('My info ratings: \n%s' % myAvg[:10])
print('\n==================================================================\n')


# Sort data ratings by created field (groupby + lambda function + sorted)
sortRatingsField = cloneDF(mergeRatings)
#sortRatingsField = sortRatingsField.groupby(['movie_id', 'title'])['rating'].agg(
#    {'COUNT': np.size, 'myAVG': lambda x: x.sum() / float(x.count())}).sort('COUNT', ascending=False)
sortRatingsField = sortRatingsField.groupby(['movie_id', 'title'])['rating'].agg(
    {np.size, lambda x: x.sum() / float(x.count())}, col_names=('COUNT','myAVG')
).sort_values(ascending=False)
print('My info sorted: \n%s' % sortRatingsField[:15])
