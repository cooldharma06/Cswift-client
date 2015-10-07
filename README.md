Cswift-client


Hi this the swift client which is aimed to make easy interaction with swift - openstack
In future we will add more feature to this client


Requirements:
  * python
  * python-swiftclient  
  * time
  * watchdog
  * ** openstack with swift enabled


What it does.?

Initially its aimed to the swiftclient operation but after certain we developed to do it as automatic syncer.
After running the below command it will create one home sync directory under (/home/cool) it will synced to the cloud.
Whatever the file you are creating/copying/updating/deleting under this folder it will synced to the cloud.

For that you have to create the account in your Openstack cloud. And you have to specify your credentials in the Cswiftclient.py file. It have the seperate configuration file currently for POC i hardcoded inside the Cswiftclient.py

In the main() you can get the hardcoded configurations.


How to run.?

Just run -> python Cswiftclient.py

_ _ _ _ _ 

cool06 .. :)



