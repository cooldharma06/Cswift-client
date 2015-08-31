'''

this is the client script which will do all operations for the user


'''


import ConfigParser
import swiftclient
import pudb

swift_config=[]

def config_read():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    # print config.sections()
    for section in config.sections():
        for key in config.options(section):
            #rint config.get(section,key)
            swift_config.append(config.get(section,key))
            print swift_config



def swift_connection():
    try:
#        pu.db
        connect = swiftclient.Connection(tenant_name=swift_config[0],user=swift_config[1],key=swift_config[2],authurl=swift_config[3],auth_version=swift_config[4])
        print 'Connection success'
    except Exception as e:
        print 'Swift connection failed. Please check your connection or creadentials',e


config_read()
swift_connection()

