'''

this is the client script which will do all operations for the user


'''


import ConfigParser
import swiftclient
from keystoneclient.v2_0 import client
import pudb
import os
import subprocess

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


swift_config=[]



class SwiftClient(FileSystemEventHandler):
    
#    _username = None
#    _password = None
#    _tenantname = None
#    _auth_url = None
#    _timeout = None 

    def __init__(self, u_name, p_word, t_name, a_url, a_version, timeout,):
        self._username = u_name
        self._password = p_word
        self._tenantname = t_name
        self._auth_url = a_url
        self._auth_version = a_version
        self.timeout = timeout



    def config_read():
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        # print config.sections()
        for section in config.sections():
            for key in config.options(section):
                #rint config.get(section,key)
                swift_config.append(config.get(section,key))
                print swift_config


# set timeout to 30s or less than that one

    def keystone_authenticate(self):
        try:
            keystone = client.Client(username=self._username, password=self._password, tenantname=self._tenantname, auth_url=self._auth_url, timeout=self.timeout)
 
#           self.authtoken = keystone.auth_token
            print '--------- Authenticated'
            return 1;
        except Exception as e:
            print 'Contact your administrator with the following message',e
            return 0;


# set retries to 4
    def swift_connection(self):
        try:
#            pu.db
            self.connect = swiftclient.Connection(user=self._username, key=self._password, tenant_name=self._tenantname, authurl=self._auth_url, auth_version=self._auth_version,retries=4)
            print 'Connection success'
            #return self.connect
        except Exception as e:
            print 'Swift connection failed. Please check your connection or creadentials',e



# method to list the containers in the swift

    def init_container(self):
        # pu.db      
        flag = False
        command = 'swift post cswift'
        print 'init container is getting called'
        try:
#            connect = swiftclient.Connection(user=self._username, key=self._password, authurl=self._auth_url, auth_version=self._auth_version,retries=4)   

            for cont in self.connect.get_account()[1]:
            #    print cont
                if (cont['name']=='cswift'):
                    print 'default Container present'
                    flag = True
                          
        except Exception as e:
            print 'Connection failed. Please contact your administrator',e

        if (flag == False):
            subprocess.call(command,shell=True)
            print 'Container got created'


            
# upload object
#  default upload size '""" 1G """"'
#  defualt syncing container is '' cswift '' 
#
    def upload_object(self,file_name):
#        pu.db
        container_name = 'cswift'
        file1 = file_name
        try:
           command = 'swift upload '+container_name+' -S 1073741824'+' '+file1
           print command 
           subprocess.call(command,shell=True)
           print 'Object -- ',file1,' ... is uploaded'
        except Exception as e:
            print 'Some know error, call administrator...',e


    def on_any_event(self,event):
        print 'Event got..',event
          



   

if __name__ == '__main__':
    #conig_read() 
    obj = SwiftClient('cool1','cool1','coolswift','http://10.0.2.15:5000/v2.0',2.0,20)
    auth_token = obj.keystone_authenticate()
    if(auth_token != None):
        obj.swift_connection()
    else:
        print 'Connection failed'
    obj.init_container()
    #_file_name = '/home/cool'
  
    observer = Observer()
    observer.schedule(obj,path='/home/cool')  # ,recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrrupt:
        observer.stop()


    observer.join()



#  
#  if anything happened in the directory call upload option
#
# 
#    obj.upload_object(_file_name) 
