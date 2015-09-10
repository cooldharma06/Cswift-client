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
        self.command = 'cd /home/cool ; swift --os-auth-url '+a_url+' --os-username '+u_name+' --os-password '+p_word+' --os-tenant-name '+t_name
        print self.command

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
        command = self.command+' post cswift'
        print 'init container is getting called'
        try: 
#            pu.db
            for cont in self.connect.get_account()[1]:
            #    print cont
                if (cont['name']=='cswift'):
                    print 'default Container present'
                    flag = True
                          
        except Exception as e:
            print 'Connection failed. Please contact your administrator',e

        if (flag == False):
            subprocess.call(command, shell=True)
            print 'Container got created'


            
#  upload object
#  default upload size '""" 1G """"'
#  default syncing container is '' cswift '' 
#  defult file path here is /home/cool/
#
#
    def object_action(self, event, file_path):
#        pu.db
        container_name = 'cswift'
        rel_path = '/home/cool'
        filename  = os.path.relpath(file_path,rel_path)
        if (event.event_type == 'created' and event.is_directory==True):
            try:
                command = self.command+' upload '+container_name+' '+filename
		print command
                subprocess.call(command, shell=True)
                print 'Object --'
            except Exception as e:
                print 'some error occurred while uploading'

        elif (event.event_type == 'modified'):
            try:
                command = self.command+' upload '+container_name+' -S 1073741824'+' '+filename
                print command 
                subprocess.call(command, shell=True)
                print 'Object -- ',filename,' ... is uploaded'
            except Exception as e:
                print 'Some know error, call administrator...',e
        elif (event.event_type == 'deleted'):
            try:
                command = self.command+' delete '+container_name+' '+filename
                subprocess.call(command, shell=True)
                print filename,' is removed from your both system and cloud'
            except Exception as e:
                print 'Some known error, just call admin...',e
        else:
            print 'unknown event got occured :-)'


    def on_any_event(self, event):
        print 'Event got..',event
#        pu.db
        self.object_action(event, event.src_path)



   

if __name__ == '__main__':
    #conig_read() 
    obj = SwiftClient('cool1', 'cool1', 'coolswift', 'http://10.0.2.15:5000/v2.0', 2.0, 20)
    auth_token = obj.keystone_authenticate()
    if(auth_token != None):
        obj.swift_connection()
    else:
        print 'Connection failed'
    obj.init_container()
    #_file_name = '/home/cool'
  
    observer = Observer()
    observer.schedule(obj, path='/home/cool', recursive=True)
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
