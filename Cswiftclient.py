'''

this is the client script which will do all operations for the user


'''


import ConfigParser
import swiftclient
from keystoneclient.v2_0 import client

import pudb

swift_config=[]



class SwiftClient:
    
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

    def list_container(self):
        # pu.db      
        try:
#            connect = swiftclient.Connection(user=self._username, key=self._password, authurl=self._auth_url, auth_version=self._auth_version,retries=4)

            for cont in self.connect.get_account()[1]:
                print cont
                print 'Present Containers are..',cont['name']

        except Exception as e:
            print 'Connection failed. Please contact your administrator',e

            
# upload object
    def upload_object(self):
        try:
          
    


if __name__ == '__main__':
    #conig_read() 
    obj = SwiftClient('cool1','cool1','coolswift','http://10.0.2.15:5000/v2.0',2.0,20)
    auth_token = obj.keystone_authenticate()
    if(auth_token != None):
        obj.swift_connection()
    else:
        print 'Connection failed'
    obj.list_container()
     
