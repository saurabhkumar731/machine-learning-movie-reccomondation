# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:43:04 2025

@author: Saurabh
"""

import pandas as pd
import difflib
import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity


loaded_model=pickle.load(open('C:/Users/Saurabh/Desktop/Deploying movie/similarity.pkl','rb'))
movies_data=pd.read_csv('C:/Users/Saurabh/Downloads/movies (1).csv')

def main():
    
    st.title('Movie Reccomondation')
    
    movie_name=st.text_input('enter movie name')
    
    if movie_name:
        
    
    
        list_of_all_titles=movies_data['title'].tolist()
    
        find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
    
        close_match= find_close_match[0]
    
        index_of_the_movie =movies_data[movies_data.title==close_match]['index'].values[0]
    
        similarity_score=list(enumerate(loaded_model[index_of_the_movie]))
    
    
        sorted_similar_movies =sorted(similarity_score,key=lambda x:x[1],reverse=True)
    
        i=1
    
        for movie in sorted_similar_movies:
          index = movie[0]
          title_from_index =movies_data[movies_data.index==index]['title'].values[0]
          if(i<30):
            st.write(i,".",title_from_index)
            i+=1
            
    else:
        st.text("no movier name")                
    
if __name__=='__main__':
    main()    