#!/usr/bin/env python3

import pymongo
import getpass
import json


CUSTOM_ROLES = dict()

CUSTOM_ROLES["listDatabases"] = {
      "role": "listDatabases",
      "privileges": [
         { "resource": { "cluster" : True }, "actions": ["listDatabases"]}
      ],
      "roles": []
   }
CUSTOM_ROLES["insertonly_cachedb"] = {
      "role": "insertonly_cachedb",
      "privileges": [
         { "resource": { "db": "cache_db", "collection": "" }, 
                        "actions": ["createIndex","insert","killCursors",
                                    "listIndexes","listCollections"] }
      ],
      "roles": [{ "role": "listDatabases", "db": "admin" }]
   }



def default(choi, deflt):
   if choi and choi.strip() != "":
      return choi.strip()
   else:
      return deflt

def make_user(db ,username:str, passwd:str, roles:list):
   #client.testdb.add_user('newTestUser', 'Test123', roles=[{'role':'readWrite','db':'testdb'}])
   # db.add_user(username, passwd, roles=roles) # deprecated in mongo 4.0
   db.command("createUser", username, pwd=passwd, roles=roles)
   print("done: {} added".format(username))

def get_db(hosts='localhost:27017', dbname="admin", u=None, p=None, authsource=None):
   if u:
      URI = 'mongodb://{}:{}@{}/?authSource={}'.format(u,p,hosts,authsource)
   else:
      URI = 'mongodb://{}/?'.format(hosts,authsource)
   if getBooleanInput("is this a replicate set? "):
      n = default(input("replica set name [rs0]: ").strip(),"rs0")
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

def pickOne(msg ,opts:list):
   i = input("{} {}: ".format(msg, opts))
   while i not in opts:
      i = input("{} {}: ".format(msg, opts))
   return i

def gen_roles(username="user"):
   roles = list()
   while getBooleanInput("add new role to {}? ".format(username)):
      if getBooleanInput("assign role to specific db? "):
         r = dict()
         r["role"] = input("role: ")
         r["db"] = input("db: ")
      else:
         r = input("role: ")
      if getBooleanInput("Is this correct: {}? ".format(r)):
         roles.append(r)  
   return roles

def get_all_add():
   print("where to connect:")
   hosts = default(input("host:port (if multiple comma separated) [localhost:27017]: ").strip(),"localhost:27017")
   authdb = default(input("authdb [admin]: ").strip(),"admin")
   
   if getBooleanInput("is authentication for {} db required? ".format(authdb)):
      u, p = get_credentials("{} db credentials".format(authdb))
      db = get_db(hosts, authdb, u, p,authdb)
   else:
      db = get_db(hosts, authdb)

   while getBooleanInput("add new custom role to db (do only once per db)? "):
      print(json.dumps(CUSTOM_ROLES,indent=1))
      pik = pickOne("Pick one of the following",list(CUSTOM_ROLES.keys()))
      try:
         addCustomRole(db, CUSTOM_ROLES[pik])
      except pymongo.errors.OperationFailure:
         print("need to authenticate to make changes.")
         u, p = get_credentials("{} db credentials".format(authdb))
         db = get_db(hosts, authdb, u, p,authdb)
         addCustomRole(db, CUSTOM_ROLES[pik])

   user, passwd = get_credentials("Credentials for new user")
   roles = gen_roles(user)

   print("User {} will be added to the authdb {} with the following permissions {}".format(user,authdb,roles))
   if getBooleanInput("is this correct? "):
      try:
         make_user(db, user, passwd, roles)
      except pymongo.errors.OperationFailure:
         print("need to authenticate to make changes.")
         u, p = get_credentials("{} db credentials".format(authdb))
         db = get_db(hosts, authdb, u, p,authdb)
         make_user(db, user, passwd, roles)


# https://www.w3resource.com/mongodb/shell-methods/role-management/db-createRole.php
def addCustomRole(db, roleDoc):
   # db.createRole(roleDoc)
   db.command("createRole",
      roleDoc["role"],
      privileges=roleDoc["privileges"],
      roles=roleDoc["roles"])
   print("done: {} added to db.".format(roleDoc["role"]))



if __name__ == "__main__":
   get_all_add()