from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import api_config 
import json
class AuthStream():
    def get_tweets(self):
        Listener=GetDetails()
        auth=OAuthHandler(api_config.CONSUMER_KEY,api_config.CONSUMER_SECRET)
        auth.set_access_token(api_config.ACCESS_TOKEN,api_config.ACCESS_TOKEN_SECRET)
        stream =Stream(auth,Listener)
        #stream.filter(track=hash_tags)
        stream.filter(track=['ipl2020','Kohli','crypto','win','happy','bitcoin','analytics','python','smart','science','data','apple','iphone','tesla','coronavirus','bigboss','motivation','day','month'])
class GetDetails(StreamListener):
    def on_data(self,data):
        try:
            with open("outfile_v1.json",'a') as outfile:
                json.dump(data,outfile)
            with open("tweetsdata_v1.txt",'a') as tweetsdata:
                tweetsdata.write(data)
                tweetsdata.write('\n')
            outfile.close()
            tweetsdata.close()
        except BaseException as e:
           print('problem getting the data',string(e)) 
        return True
    def on_error(self,status):
        print(status)

if __name__ =="__main__":
    print("start")
    #hash_tags=["corona","ipl","applecard","transform","bigdata","worldwar","science","food","music","frustration","iphone"]
    obj = AuthStream()
    obj.get_tweets()
