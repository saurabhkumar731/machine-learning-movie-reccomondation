# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:21:39 2025

@author: Saurabh
"""

import numpy as np
import pandas as pd
import difflib
import pickle
from sklearn.metrics.pairwise import cosine_similarity

loaded_model=pickle.load(open('C:/Users/Saurabh/Desktop/Deploying movie/similarity.pkl','rb'))

movie_name=input('Enter your favourite movie name :')

movies_data=pd.read_csv('C:/Users/Saurabh/Downloads/movies (1).csv')
list_of_all_titles=movies_data['title'].tolist()

find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)

close_match= find_close_match[0]

index_of_the_movie =movies_data[movies_data.title==close_match]['index'].values[0]

similarity_score=list(enumerate(loaded_model[index_of_the_movie]))


sorted_similar_movies =sorted(similarity_score,key=lambda x:x[1],reverse=True)

print('Movies suggested for you:\n')

i=1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index =movies_data[movies_data.index==index]['title'].values[0]
  if(i<30):
    print(i,'.',title_from_index)
    i+=1