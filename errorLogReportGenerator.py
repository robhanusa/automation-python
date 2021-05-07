#!/usr/bin/env python3

import operator
import re

#error type, sorted from most to least common
#key is error description, value is count
error_messages = {}

#user entries (INFO or ERROR) sorted by frequency per user
#key is user and value is another dict w/ keys INFO and ERROR
user_entries = {}

#make pattern based on log files
pattern = r"(INFO|ERROR) ([\w \']*) .*\((.+)\)"
pattern1 = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"

#populate the dictionaries above
with open("syslog.log", 'r') as f:
    for line in f:
        result = re.search(pattern,line)
        error = result.groups()[0]
        message = result.groups()[1]
        user = result.groups()[2]
        #populate error_messages dict
        if error == "ERROR":
            if message not in error_messages:
                error_messages[message] = 1
            else:
                error_messages[message] +=1
        #populate user_entries dict
        if user not in user_entries:
            user_entries[user] = {"ERROR": 0, "INFO": 0}
        user_entries[user][error] += 1
             
#the below return sorted strings of tuples        
sorted_error_messages = sorted(error_messages.items(), key = operator.itemgetter(1), reverse = True)
sorted_user_entries = sorted(user_entries.items())
#print(sorted_user_entries)

error_messages_columns = ['Error','Count']
error_messages_title = 'Error Message'

#sort dictionaries based on count.
with open('error_messages.csv', 'w') as f:
    f.write(f'{error_messages_columns[0]}, {error_messages_columns[1]}\n')
    for row in range(len(sorted_error_messages)):
        f.write(f'{sorted_error_messages[row][0]}, {sorted_error_messages[row][1]}\n')

user_entries_columns = ['Username', 'INFO', 'ERROR']
with open('user_statistics.csv', 'w') as f:
    f.write(f'{user_entries_columns[0]}, {user_entries_columns[1]}, {user_entries_columns[2]}\n')
    for row in range(len(sorted_user_entries)):
        f.write(f'{sorted_user_entries[row][0]}, {sorted_user_entries[row][1]["INFO"]}, {sorted_user_entries[row][1]["ERROR"]}\n')
    
