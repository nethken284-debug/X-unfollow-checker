import json
def following_follower(path):
    with open(path,encoding='utf-8') as f:
        text= f.read()
        parts=text.split('=',1)
        parts_json=parts[1]
        parts_of_json=json.loads(parts_json)
        return parts_of_json
following=following_follower('data/following.js')
followers=following_follower('data/follower.js')
who_followers=[]
for b in followers:
    who_followers.append(b['follower']['accountId'])

for i in following:
    if i['following'][str('accountId')]not in who_followers:
     print (i['following'][str('accountId')])
     print(i['following'][str('userLink')])
