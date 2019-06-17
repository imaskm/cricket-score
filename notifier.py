# Python program to illustrate 
# desktop news notifier 
import feedparser 
import notify2 
import os 
import time 
def getScore(url): 
    f = feedparser.parse(url)
    #print(f)
    #ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('Live Scores') 
    for newsitem in f['items']: 
        #if("India" not in newsitem['title'] ):
            #continue
        n = notify2.Notification(newsitem['title'], 
								newsitem['summary']
								) 
        
        n.set_urgency(notify2.URGENCY_NORMAL) 
        n.show() 
        time.sleep(2)
        n.set_timeout(15000) 
    

getScore("http://static.cricinfo.com/rss/livescores.xml") 
