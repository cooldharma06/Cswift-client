'''

program to get the input from user and to make the configuration file


'''


__author__ = 'cooldharma06@gmail.com'


import ConfigParser


cfgfile = open("config.ini",'w')

config = ConfigParser.ConfigParser()

# set a number of parameters
config.add_section("Swift-config")

tenant_name = input('Enter the tenant name..')
config.set("Swift-config", "tenant_name", tenant_name)
user = input('Enter the user name...')
config.set("Swift-config", "user", user)
config.set("Swift-config","key",input('Enter the key value..'))
#config.set("Swift-config","authurl",input('Enter the swift authurl *ex="http://ip:port/* ...'))
config.set("Swift-config","key",'http://10.0.2.15:35357/v2.0')
config.set("Swift-config","auth_version",input('Enter the auth version.. [default = 2.0] ...'))


#config.add_section("ematter")
#config.set("ematter", "pages", 250)

# write to screen
config.write(cfgfile)

cfgfile.close()


