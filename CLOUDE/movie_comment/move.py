import sqlite3 #python3自带的
import pandas as pd
import jieba #jieba 主要是把一名话里面的词语提炼出来

#https://movie.douban.com/subject/1292052/
FILTER_WORDS=['知道']


def get_movie_id_list(min_comment_count):   
    movie_list=comment_data['MOVIEID'].value_counts()
    movie_list=movie_list[movie_list.values>min_comment_count]
    return movie_list.index

def get_comment_keywords_counts(movie_id,count):
    commmet_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
    comment_str_all=''
    for comment in comment_list:
        comment_str_all+=comment+'\n'
    #获取分词后的列表
    seg_list=list(jieba.cut(comment_str_all))
    #转换成pandas的series类型数据
    Keywords_counts=pd.Series(seg_list)
    Keywords_counts=keywords_counts[Keywords_counts.str.len()>1] #关键词长度大于1
    Keywords_counts=Keywords_counts[~Keywords_counts.str.contains('|'.join(FILTER_WORDS))] #包含关键词
    Keywords_counts=Keywords_counts.values_count()[:count]
    return Keywords_counts

def generate_word_cloud(word_list,path_name):   
    movie_id='1292052'
    keyword_count= get_comment_keywords_counts(movie_id,30)
    wordcloud = pec.WordCloud(width=120,height=720)
    wordcloud.render()

conn=sqlite3.connect('data/douban_comment_data.db')
comment_data=pd.read_sql_query('select * from comment;',conn)
    
def get_movie_name_and_score(movie_id):
    movie_link='http://movie.douban.com/subject/{}'.format(movie_id)
    search_result = movie_data[movie_data['链接']==movie_link].iloc[0]
    movie_name = search_result['电影名']
    movie_score = search_result['评分']
    return(movie_name,movie_score)
    
movie_name,movie_score = get_movie_name_and_score(movie_id)

path_name='wordcloud/{}_{}.html'.format(movie_name,movie_score)

generate_word_cloud(keywords_count,path_name)

    
    