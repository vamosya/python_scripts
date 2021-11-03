# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:11:57 2021

@author: cperaltap (vamosya github)

use: GarminActivitiesToCsvFile.py user pass

"""

# Librerias necesarias
from garminconnect import Garmin
from getpass import getpass
import logging
import pandas as pd
import reverse_geocoder as rg
import warnings
import sys

if len(sys.argv) != 3:
    print ("ERROR: You need to pass 2 arguments. Use: GarminActivitiesToCsvFile.py user pass")
    exit()

def get_connection(user, paswd, max_activities = 2000):
    client = Garmin(user, paswd)
    print("{} {}".format(user, paswd))
    client.login()
    print("Hola {}.conexión creada".format(client.get_full_name()))
    return client 
   
def get_df(user, paswd, max_activities):
    connection = get_connection(user, paswd, max_activities)
    df = connection.get_activities(0, max_activities) 
    # save as pandas df
    activities = pd.DataFrame(df)
    return activities
    
def create_csv(user, paswd, max_activities):
    activities = get_df(user, paswd, max_activities)
    activities.to_csv('activities.csv')
    
create_csv(sys.argv[1], sys.argv[2], 1500)