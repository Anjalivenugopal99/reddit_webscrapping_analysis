import praw
import re
import schedule
import csv
import datetime
import pickle
from . import reddit_constants
class RedditHelper():
    
    def __init__(self):
        self.temp ={}
        self.start_time = datetime.datetime.now()
        self.end_time= self.start_time + datetime.timedelta(minutes=reddit_constants.time_frame)
        
    def getRedditInstance(self):
        """Method to get the reddit instance from the user details"""
        reddit = praw.Reddit(client_id = reddit_constants.my_client_id,
                             client_secret = reddit_constants.my_client_secret,
                             user_agent = reddit_constants.my_user_agent,
                             username = reddit_constants.my_username)
        return reddit
    def find_word_count(self,word_list):
        """find the TICKER count in a list and return a new dictionary with
            word and word count"""
        d ={}
        for key in word_list: 
            if 3<len(key)<=5:
                d[key] = d.get(key, 0) + 1
        sorted(d.items(), key = lambda x: x[1], reverse = True)
        return d
    def get_time(self,comment):
        """get time from each comment and convert to datetime format"""
        time = datetime.datetime.fromtimestamp(comment.created_utc)
        return time
    def process_data(self,data_dict):
        """ process the incoming dictionary data  if the  date is between
        the given time and end time which is 1 hr after the start time and the 
        set start time again as endtime"""
        delete = []
        for key,value in data_dict.items():
            if self.start_time<key<self.end_time:
                for words,count in value.items():
                   # print("Words:: ",words)
                    if words in self.temp:
                        self.temp[words] += count
                    else:
                        self.temp[words] = count
                delete.append(key)
                #print("input map:",self.temp)
            if key>self.end_time:
                self.write_to_file()
                self.temp = {}
                self.start_time = self.end_time 
                self.end_time= self.start_time + datetime.timedelta(minutes=reddit_constants.time_frame)
        for i in delete:
            del data_dict[i]
            
    
    def write_to_file(self):
        """
        This method write a dictionary to a pickle file.
        """
        st  =  self.start_time.strftime(reddit_constants.datetime_format)
        et = self.end_time.strftime(reddit_constants.datetime_format)
        print("map in write to file : ",self.temp)   
        pickling_on = open("../pickle_files/tempdata_"+st+"_"+et+".pickle",'wb')
        pickle.dump(self.temp, pickling_on)
        pickling_on.close()
            
        