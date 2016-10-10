sldList=['fastlylb.net']
# ,'yunjiasu-cdn.net','wpengine.com',
#'eu-west-1.elb.amazonaws.com'
#         ,'us-east-1.elb.amazonaws.com','ourwebpic.com','edgecastcdn.net','cloudflare.com',
#         'incapdns.net','fastlylb.net','dynect.net','pbwstatic.com','netdna-cdn.com'
#         'cloudflare.net','akamaiedge.net','anycast.me','kxcdn.com','jiashule.com',
#         'alikunlun.com','d5nxst8fruw4z.cloudfront.net','ap-northeast-1.elb.amazonaws.com',
#         'd2t8dj4tr3q9od.cloudfront.net','cdntip.com','us-west-2.elb.amazonaws.com',
#         'ap-southeast-1.elb.amazonaws.com','windows.net'
result=list()
count=0
for value in f:
    data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
    mainSld=data[0]
    del data[-1]
    if mainSld in sldList:
        result=result + data

print result[:20]
print len(result)


objectlist=list()
for item in result:
    if sldTOASNDict.get(item):
        objectlist=objectlist + list(sldTOASNDict.get(item))
print objectlist[:20]
f1=open('/home/sakib/soumya/wholeSLD/objectsfastlylb.txt','w')
# for value in objectlist:
#     f1.write(str(value))
#     f1.write('\n')
cnt = Counter()
for word in objectlist:
    cnt[word] += 1
print cnt.most_common(50)
for k,v in cnt.iteritems():
    f1.write(str((k,v)))
    f1.write('\n')