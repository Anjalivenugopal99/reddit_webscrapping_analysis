# -*- coding: utf-8 -*-
from. import reddit_constants
from.reddit_helper import RedditHelper 
import re
import sqlite3
from sqlite3 import Error
import os
import datetime
# method streaming the comments 
output_dict = {}
time_count = {}
global start_time

def stream_comments():
    rh = RedditHelper()
    reddit = rh.getRedditInstance()
    for comment in reddit.subreddit(reddit_constants.sub_reddit_name).stream.comments():
        time = rh.get_time(comment)
        matches = re.findall(reddit_constants.regex,comment.body)
        output_dict = rh.find_word_count(matches)
        time_count[time] = output_dict
        rh.process_data(time_count)
        
def write_to_sqltable():
    conn = create_connection(reddit_constants.database)
    if conn is not None:
        df= pd.DataFrame()
        with os.scandir(reddit_constants.directory) as it:
            for entry in it:
                if entry.is_file and entry.name.endswith(".pickle"):
                    name = entry.name.split("_")
                    date1 =  datetime.datetime.strptime(name[1], '%m%d%Y%H%M')
                    date2 = datetime.datetime.strptime(name[2].strip(".pickle"), '%m%d%Y%H%M')
                    df=df.append(pickle_to_df(entry,date1,date2))
#                     os.remove(directory+"/"+entry.name)
            write_to_table(conn,df)
            
    else:
        print("connection error")
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
def write_to_table(conn,df):
    cursor = conn.cursor()
    for index,row in df.iterrows():
        cursor.execute("""select * from TICKER_DATA where TIKR = ?""",(row.TIKR,))
        print(cursor.fetchall())
        if (cursor.fetchall()!=0):
            cursor.execute(reddit_constants.update_query,(row.TIKR_COUNT,str(row.DATE_TO),str(row.DATE_FROM),row.TIKR))
        else:
            cursor.execute(reddit_constants.create_query,(row.TIKR,row.TIKR_COUNT,str(row.DATE_TO),str(row.DATE_FROM)))
    conn.commit()
    conn.close()
