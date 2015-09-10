'''

this is the module for weatching the particular folder

'''



import time
from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler
import pudb

class Cswift(FileSystemEventHandler):

#    def on_any_event(self,event):
#        pu.db
#        print "hey event got occured..",event
     
    def on_created(self,event):
       pu.db
       if(event.is_directory == True):
           print "Directory got created",event
       else:
           print 'file got created',event

    def on_modified(self,event):
 #      pu.db
       print "file got modified",event

    def on_deleted(self,event):
  #     pu.db
       print "file got deleted",event


if __name__=="__main__":
    cswift_handler = Cswift()
    observer = Observer()
    observer.schedule(cswift_handler,path='/home/cool', recursive=True)
    observer.start()


    try:
        while True:
            time.sleep(1)
    except KeyboardInterrrupt:
        observer.stop()


    observer.join() 


