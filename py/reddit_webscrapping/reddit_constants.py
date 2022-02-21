# -*- coding: utf-8 -*-
my_client_id = "aU5CZ-LIiXtUZg"
my_client_secret = "xJCnDlCcJ-n0fQbwCEsoJqY0wHVWYw"
my_user_agent = "Reddit Webscrapping"
my_username = "EntertainmentShot784"

sub_reddit_name = "wallstreetbets"
regex = r"(\b\w(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+){1}\w\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+){1}\w\b)*)"
datetime_format = "%m%d%Y%H%M"
database = r"data_sqlite_original.db"
directory = '.\pickle_files'
update_query = """ UPDATE TICKER_DATA SET TIKR_COUNT = TIKR_COUNT + ?,DATE_TO = ?,DATE_FROM = ? where TIKR = ?;""" 
create_query = """INSERT INTO TICKER_DATA (TIKR ,TIKR_COUNT ,DATE_TO,DATE_FROM) VALUES (?,?,?,?);"""
time_frame = 30