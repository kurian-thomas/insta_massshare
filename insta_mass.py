from InstagramAPI import InstagramAPI
from urllib.parse import quote_plus
import time

username = ''   #add your username
pwd = ''		#add your password
API = InstagramAPI(username,pwd)
API.login()
time.sleep(2)
API.getProfileData()
my_id = API.LastJson['user']['pk']


API.getUsernameInfo(my_id)   #check if authentication was right 
print("username: "+str(API.LastJson['user']['username']))
print("following count: "+str(API.LastJson['user']['following_count']))
print("follower count: "+str(API.LastJson['user']['follower_count']))


API.getTotalSelfFollowers()
followers_details=API.LastJson

API.getTotalSelfFollowings()
followings_details=API.LastJson

url=''						#url of media to be shared via instagram web
message=""					#custom message added to the media	

m_id=API.get_media_id(url)

for i in range(len(followers_details['users'])):			#for all followers
	API.direct_share(m_id,followers_details['users'][i]['pk'],message)

print("ok")
