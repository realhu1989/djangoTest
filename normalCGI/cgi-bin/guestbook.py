#!/usr/bin/env python
#coding: utf-8

import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """Save the comment data
    """

    #open the shelve moduel database File

    database = shelve.open(DATA_FILE)

    if 'greeting_list' not in database:
        greeting_list=[]
    else:
        #get the greeting_list from databass
        greeting_list=database['greeting_list']

    greeting_list.insert(0, {
        'name':name,
        'comment':comment,
        'create_at':create_at,
    })

    #update the database
    database['greeting_list']=greeting_list

    #close the database file
    database.close()

def load_data():
    """Return the comment data saved before
    """

    #open the shelve module database file
    database = shelve.open(DATA_FILE)

    #get the greeting_list if not , just return empty list.
    greeting_list = database.get('greeting_list', [])

    database.close()

    return greeting_list

