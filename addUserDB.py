#!/usr/bin/env python3

import pymongo
import getpass
import json

def make_user(db ,username:str, passwd:str, roles:list):
   #client.testdb.add_user('newTestUser', 'Test123', roles=[{'role':'readWrite','db':'testdb'}])
   db.add_user(username, passwd, roles=roles)



def get_db(hosts='localhost:27017', dbname="admin", u=None, p=None, authsource=None):
   if u:
      URI = 'mongodb://{}:{}@{}/?authSource={}'.format(u,p,hosts,authsource)
   else:
      URI = 'mongodb://{}/?'.format(hosts,authsource)
   if getBooleanInput("is this a replicate set?"):
      n = input("replica set name: ")
      if u:
         URI = "{}&replicaSet={}".format(URI, n)
      else:
         URI = "{}replicaSet={}".format(URI, n)
   client = pymongo.MongoClient(URI)
   return client[dbname]

def get_credentials(msg=""):
   print(msg)
   user = input("Username: ")
   passwd = getpass.getpass()
   return user,passwd
def getBooleanInput(msg=""):
   i = input(msg).strip().lower()
   while True:
      if i == "y" or i == "yes" or i == "true" or i == "t":
         return True
      elif i == "n" or i == "no" or i == "false" or i == "f":
         return False
      i = input(msg).strip().lower()

def gen_roles(username="user"):
   roles = list()
   while getBooleanInput("add role to {}? ".format(username)):
      r = dict()
      r["role"] = input("role: ")
      r["db"] = input("db: ")
      if getBooleanInput("Is this correct: {}? ".format(r)):
         roles.append(r)  
   return roles

def get_all_add():
   print("where to connect:")
   hosts = input("host:port (if multiple comma separated): ")
   authdb = input("authdb: ")
   user, passwd = get_credentials("Credentials for new user")
   roles = gen_roles(user)

   print("User {} will be added to the authdb {} with the following permissions {}".format(user,authdb,roles))
   if getBooleanInput("is this correct? "):
      if getBooleanInput("is authentication for {} db required? ".format(authdb)):
         u, p = get_credentials("{} db credentials".format(authdb))
         db = get_db(hosts, authdb, u, p,authdb)
      else:
         db = get_db(hosts, authdb)
      make_user(db, user, passwd, roles)

if __name__ == "__main__":
   get_all_add()