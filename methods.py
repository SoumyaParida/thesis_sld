import csv
import codecs
import itertools
from collections import defaultdict
import itertools
import subprocess
from netaddr import *
import datetime
#---------------------------------------------------------------------------------------
#Final
import subprocess
def resultPrefix(prefixes):
    newlist=list()
    for ip in prefixes:
        if ip:
            ip=ip.split('/')
            newlist.append((ip[0],ip[1]))
    sorted_by_second = sorted(newlist, key=lambda tup: tup[1],reverse=False)
    #print sorted_by_second
    test1=list()
    test2=list()
    for value in sorted_by_second:
        test1.append((value[0]+'/'+value[1]))
    for item in sorted_by_second:
        test2.append((item[0]+'/'+item[1]))
    #print "test1",test1
    #print "test2",test2
    result=set()
    count=0
    alreadyDone=set()
    for value1 in test1:
        #test3.remove(value1)
        if value1 not in alreadyDone:
            alreadyDone.add(value1)
            prefix1=IPSet([value1])
            for item in test2:
                prefix2=IPSet([item])
                if prefix1!=prefix2:
                    if prefix1.issuperset(prefix2):
                        result.add(value1)
                        alreadyDone.add(item)
                    else:
                        result.add(value1)
    return result

#=============================
#collecting RIS
#============================
# f=open("/home/soumya/Documents/wholeSLD/ripeRIS.txt",'r')

# addressSet=set()
# asndict=defaultdict(set)
# for value in f:
#     value=value.replace(' ','').replace('\n','').replace('(','').replace(')','').replace("'",'').split(',')
#     addressSet.add(value[0])
# print "add",len(addressSet)

# finaloutput=codecs.open("/home/soumya/Documents/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# ipset=set()
# for line in finaloutputre:
#     ipset.add(line[8])
#     asndict[line[8]].add(line[9])

# print "len ipset",len(ipset)

# notcompletd=ipset-addressSet
# print "notcomple",len(notcompletd)

# f1=open("/home/soumya/Documents/wholeSLD/ripeRISNotComplted.txt",'w')
# f11=open("/home/soumya/Documents/wholeSLD/ripeRISNotCompltedASN.txt",'w')
# count=0
# for ip in notcompletd:
#     count=count+1
#     print "count",count
#     try :
#         ls_lines = subprocess.check_output(['whois', '-h','riswhois.ripe.net',ip]).splitlines()
#         for index,item in enumerate(ls_lines):
#             if 'route:' in item:
#                 asn=ls_lines[index+1].split(':')[1].strip()               
#                 prefix=ls_lines[index].split(':')[1].strip()
#                 f1.write(str((ip,prefix)))
#                 f1.write('\n')
#                 f11.write(str((ip,prefix,asn)))
#                 f11.write('\n')
#     except:
#         print "error in",ip  
# print "count",count

#=======================================================================
#Creating prefix file
#========================================================================
# finaloutput=codecs.open("/home/soumya/Documents/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# sldToIpdict=defaultdict(set)
# for line in finaloutputre:
#     sldToIpdict[line[7]].add(line[8])

# f=open('/home/soumya/Documents/wholeSLD/ripeRIS.txt','r')
# h=open('/home/soumya/Documents/wholeSLD/prefix.txt','w')

# k=open('/home/soumya/Documents/wholeSLD/linksCount.txt','r')

# prefixset=defaultdict(set)
# for item in f:
#     item=item.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     prefixset[item[0]].add(item[1])

# for value in k:
#     value=value.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     ipset=set()
#     if sldToIpdict.get(value[0]):
#         ipset=sldToIpdict.get(value[0])
#     prefix=set()
#     for ip in ipset:
#         if prefixset.get(ip):
#             prefix=prefix | prefixset.get(ip)
#     h.write(str((value[0],prefix)))
#     h.write('\n')


#=======================================================================
#Method1 :AggreagatePrefix
#========================================================================
# f=open('/home/soumya/Documents/wholeSLD/prefix.txt','r')
# h=open('/home/soumya/Documents/wholeSLD/prefixAggregate.txt','w')
# hostlist=list()
# d = defaultdict(list)
# result=list()
# count=0
# for item in f:
#     item=item.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     host=item[0]
#     hostlist.append(host)
#     item.pop(0)
#     prefixes=list()
#     for x in item:
#         prefixes.append(x)
#     d[host].append(prefixes)
# for value in hostlist:
#     prefixTest=list(itertools.chain.from_iterable(d.get(value)))
#     if len(prefixTest) >1 :
#         check=list(resultPrefix(prefixTest))
#     else:
#         check=list(prefixTest)
#     h.write(str((value,check)))
#     h.write('\n')

# def jaccard_similarity(x,y):
#     intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
#     #union_cardinality = len(set.union(*[set(x), set(y)]))
#     sum_cardinality = len(set(y))
#     return intersection_cardinality/float(sum_cardinality)

# h=open('/home/sakib/soumya/wholeSLD/prefixAggregate.txt','r')
# k=open('/home/sakib/soumya/wholeSLD/SldAggregate.txt','w')
# d=defaultdict(list)
# hostlist=list()
# for line in h:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     host=item[0]
#     hostlist.append(host)
#     item.pop(0)
#     prefixes=list()
#     for x in item:
#         prefixes.append(x)
#     d[host].append(prefixes)
# donelist=set()
# i=0
# count=0

# for i in range(i,len(hostlist)):
#     print "host going on",hostlist[i]
#     print "donelist",len(donelist)
#     print "current time",datetime.datetime.now().time()
#     print "count",count
#     if hostlist[i] not in donelist:
#         j=i+1
#         valuePrefix=list(itertools.chain.from_iterable(d.get(hostlist[i])))
#         for j in range(j,len(hostlist)):
#             if hostlist[j] not in donelist:
#                 valuePrefix1=list(itertools.chain.from_iterable(d.get(hostlist[j])))

#                 for value1 in valuePrefix:
#                     if value1 !='':
#                         for index, item1 in enumerate(valuePrefix1):
#                             if value1.split('.')[0] == item1.split('.')[0]:
#                                 prefix1=IPSet([value1])
#                                 prefix2=IPSet([item1])
#                                 if prefix1.issuperset(prefix2):
#                                     valuePrefix1[index] = value1

#                 for value2 in valuePrefix1:
#                     if value2 !='':
#                         for index, item2 in enumerate(valuePrefix):
#                             if value2.split('.')[0] == item2.split('.')[0]:
#                                 prefix1=IPSet([value2])
#                                 prefix2=IPSet([item2])
#                                 if prefix1.issuperset(prefix2):
#                                     valuePrefix[index] = value2
#                 if ((len(valuePrefix) >0) and (len(valuePrefix1) >0)):
#                     similarity=jaccard_similarity(valuePrefix, valuePrefix1)
#                     if similarity >0.7 :
#                         k.write(str((hostlist[i],hostlist[j])))
#                         k.write('\n')
#                         donelist.add(hostlist[j])
#     count=count+1

#=============================================
#clubbed slds
#=============================================

# f=open('/home/sakib/soumya/wholeSLD/SldAggregate.txt','r')

# f1=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','w')

# d=defaultdict(set)
# for line in f:
#   mainSLD=line.replace(' ','').replace('\n','').replace('(','').replace(')','').replace("'",'').split(',')
#   d[mainSLD[0]].add(mainSLD[1])

# result=list()
# for k,v in d.items():
#   result.append((k,v,len(v)))

# sorted_by_second = sorted(result, key=lambda tup: tup[2],reverse=True)

# for value in sorted_by_second:
#   f1.write(str(value))
#   f1.write('\n')

#=============================================
#Sorting clubbed slds
#=============================================

# f=open('/home/sakib/soumya/wholeSLD/clubbedSLDSorted.txt','w')

# f1=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')

# result=list()
# for line in f1:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     result.append(str((item[0],int(item[-1]))))
# sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
# for item in sorted_by_second:
#     f.write(str(item))
#     f.write('\n')

#=============================================
#clubbed links
#=============================================

# f1=open('/home/sakib/soumya/wholeSLD/linksCount.txt','r')
# sldTOLinksdict=dict()
# result=list()
# for line in f1:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sldTOLinksdict[item[0]]=item[1]

# f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')
# g=open('/home/sakib/soumya/wholeSLD/clubbedSLDLinks.txt','w')
# result=list()
# for value in f:
#     data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     mainSld=data[0]
#     childSld=data[-1]
#     del data[-1]
#     links=0
#     for item in data:
#         if sldTOLinksdict.get(item):
#             links=links + int(sldTOLinksdict.get(item))
#     result.append(str((mainSld,int(childSld),links)))
# sorted_by_second = sorted(result, key=lambda tup: len(tup[2]),reverse=True)
# for item in sorted_by_second:
#     g.write(str(item))
#     g.write('\n')

# =============================================
# Not completed websites
# =============================================
# k=open('/home/sakib/soumya/wholeSLD/linksCount.txt','r')
# sldTOLinksdict=dict()
# result=list()
# for line in k:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sldTOLinksdict[item[0]]=item[1]

# f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')
# h=open('/home/sakib/soumya/wholeSLD/linksCount.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/clubbedLinksASN_forNotCompleted.txt','w')
# d=defaultdict(set)
# completedSLD=set()
# for line in f:
#   mainSLD=line.replace(' ','').replace('\n','').replace('(','').replace(')','').replace("'",'').split(',')
#   del mainSLD[-1]
#   for item in mainSLD:
#       completedSLD.add(item)
# print "completed",len(completedSLD)

# hostlist=set()
# for line in h:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     host=item[0]
#     hostlist.add(host)
# print "hostlist",len(hostlist)
# notcompletedSLD=set(hostlist)-set(completedSLD)
# print "notcompletedSLD",len(notcompletedSLD)
# result=list()
# for item in notcompletedSLD:
#   linklist=set()
#   if sldTOLinksdict.get(item):
#     links=int(sldTOLinksdict.get(item))
#   result.append(str((item,0,links)))
# #sorted_by_second = sorted(result, key=lambda tup: len(tup[1]),reverse=True)
# for item in result:
#     f1.write(str(item))
#     f1.write('\n')



#=============================================
#IP addresses Count
#=============================================

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# f=open('/home/sakib/soumya/wholeSLD/ipAddressCount.txt','w')
# sldTOASNDict=defaultdict(set)
# for line in finaloutputre:  
#     if line[7] != '-' :
#         sldTOASNDict[line[7]].add(line[8])

# for k,v in sldTOASNDict.items():
#     if sldTOASNDict.get(k):
#         f.write(str((k,len(sldTOASNDict.get(k)))))
#         f.write('\n')


# =============================================
# clubbed ips
# =============================================

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/clubbedSLDIPs','w')
# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:  
#     if line[7] != '-' :
#         sldTOASNDict[line[7]].append(line[8])

# print "1st step done"

# result=list()
# for value in f:
#     data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     mainSld=data[0]
#     childSld=data[-1]
#     del data[-1]
#     asnlist=set()
#     for item in data:
#         if sldTOASNDict.get(item):
#             asnlist=asnlist | set(sldTOASNDict.get(item))
#     result.append(str((mainSld,len(asnlist))))
# sorted_by_second = sorted(result, key=lambda tup: len(tup[1]),reverse=True)
# for item in sorted_by_second:
#     f1.write(str(item))
#     f1.write('\n')

# =============================================
# clubbed asns
# =============================================

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/clubbedSLDASNs.txt','w')
# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:  
#     if line[7] != '-' and line[9] !='-':
#         sldTOASNDict[line[7]].append(line[9])

# print "1st step done"

# result=list()
# for value in f:
#     data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     mainSld=data[0]
#     childSld=data[-1]
#     del data[-1]
#     asnlist=set()
#     for item in data:
#         if sldTOASNDict.get(item):
#             asnlist=asnlist | set(sldTOASNDict.get(item))
#     result.append(str((mainSld,len(asnlist))))
# sorted_by_second = sorted(result, key=lambda tup: len(tup[1]),reverse=True)
# for item in sorted_by_second:
#     f1.write(str(item))
#     f1.write('\n')


# =============================================
# Not completed websites
# =============================================

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)


# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:  
#     if line[7] != '-' :
#         sldTOASNDict[line[7]].append(line[8])

# f=open('/home/sakib/soumya/wholeSLD/clubbedLinksASN_forNotCompleted.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/NotCompletedIps.txt','w')
# d=defaultdict(set)
# completedSLD=set()
# for line in f:
#   mainSLD=line.replace(' ','').replace('\n','').replace('(','').replace(')','').replace("'",'').split(',')
#   sld=mainSLD[0]
#   if sldTOASNDict.get(sld):
#     f1.write(str((sld,len(set(sldTOASNDict.get(sld))))))
#     f1.write('\n')


# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:  
#     if line[7] != '-' and line[9] !='-':
#         sldTOASNDict[line[7]].append(line[9])

# f=open('/home/sakib/soumya/wholeSLD/clubbedLinksASN_forNotCompleted.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/NotCompletedASNs.txt','w')
# d=defaultdict(set)
# completedSLD=set()
# for line in f:
#   mainSLD=line.replace(' ','').replace('\n','').replace('(','').replace(')','').replace("'",'').split(',')
#   sld=mainSLD[0]
#   if sldTOASNDict.get(sld):
#     f1.write(str((sld,len(set(sldTOASNDict.get(sld))))))
#     f1.write('\n')

#==========================================
#combibe all features
#==========================================
# f=open('/home/sakib/soumya/wholeSLD/clubbedSLDIPs.txt','r')
# sldTOIPsdict=dict()
# for line in f:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sldTOIPsdict[item[0]]=item[1]
# g=open('/home/sakib/soumya/wholeSLD/clubbedSLDASNs.txt','r')
# sldTOASNsdict=dict()
# for line in g:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sldTOASNsdict[item[0]]=item[1]
# h=open('/home/sakib/soumya/wholeSLD/clubbedSLDLinks.txt','r')
# final=open('/home/sakib/soumya/wholeSLD/finalClubbedFile.txt','w')
# for line in h:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sld=item[0]
#     childsld=int(item[1])
#     links=int(item[2])
#     if sldTOIPsdict.get(sld):
#         ips=int(sldTOIPsdict.get(sld))
#     else:
#         ips=0
#     if sldTOASNsdict.get(sld):
#         asns=int(sldTOASNsdict.get(sld))
#     else:
#         asns=0
#     final.write(str((sld,childsld,links,ips,asns)))
#     final.write('\n')

#==========================================
#Sorting
#==========================================
# h=open('/home/sakib/soumya/wholeSLD/finalClubbedFile.txt','r')
# final=open('/home/sakib/soumya/wholeSLD/finalClubbedFileSorted.txt','w')
# result=list()
# for line in h:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sld=item[0]
#     childsld=int(item[1])
#     links=int(item[2])
#     ips=int(item[3])
#     asns=int(item[4])
#     result.append((sld,childsld,links,ips,asns))

# sorted_by_second = sorted(result, key=lambda tup: tup[2],reverse=True)
# for item in sorted_by_second:
#     final.write(str(item))
#     final.write('\n')


#==========================================
#zipf's law
#==========================================

# sumoflinks=0
# f=open('/home/sakib/soumya/wholeSLD/finalClubbedFileSorted.txt','r')
# count=1
# for line in f:
#     data=line.replace('(','').replace(')','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     sumoflinks= sumoflinks+int(data[2])
# print sumoflinks   #Answer is 12575566

#80 % of 12575566 which is 10060453
# sumoflinks=0
# f=open('/home/sakib/soumya/wholeSLD/finalClubbedFileSorted.txt','r')
# count=1
# for line in f:
#     data=line.replace('(','').replace(')','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     if sumoflinks <10060453 :
#         sumoflinks=sumoflinks+int(data[2])
#         count=count+1
#     else:
#         break
# print sumoflinks #837
# print count #3205

#================================
#sorting based on number of child sld
#================================
# h=open('/home/sakib/soumya/wholeSLD/finalClubbedFile.txt','r')
# final=open('/home/sakib/soumya/wholeSLD/finalClubbedBasedOnChildSorted.txt','w')
# result=list()
# for line in h:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sld=item[0]
#     childsld=int(item[1])
#     links=int(item[2])
#     ips=int(item[3])
#     asns=int(item[4])
#     result.append((sld,childsld,links,ips,asns))

# sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
# for item in sorted_by_second:
#     final.write(str(item))
#     final.write('\n')

# f=open('/home/sakib/soumya/wholeSLD/finalClubbedBasedOnChildSorted.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/infrasturesHavingZeroSLD.txt','w')
# result=list()
# a=list()
# b=list()
# count=1
# childSLDWithLessSLD=1
# for line in f:
#   data=line.replace('(','').replace(')','').replace("'",'').replace('\n','').replace(' ','').split(',')
#   sld=data[0]
#   childSld=data[1]
#   if ((int(childSld)==0) or (int(childSld)==1)) :
#     f1.write(str(line))
#     childSLDWithLessSLD=childSLDWithLessSLD+1
# print childSLDWithLessSLD
# print float(childSLDWithLessSLD*100)/53852
  # a.append(count)
  # b.append(int(childSld))
  # count=count+1

#===========================
#sorting based on links
#===========================
# h=open('/home/sakib/soumya/wholeSLD/infrasturesHavingZeroSLD.txt','r')
# final=open('/home/sakib/soumya/wholeSLD/infrasturesHavingZeroSLDSorted.txt','w')
# result=list()
# for line in h:
#     item=line.replace('(','').replace(')','').replace('\n','').replace(' ','').replace("'",'').replace('set','').replace('[','').replace(']','').split(',')
#     sld=item[0]
#     childsld=int(item[1])
#     links=int(item[2])
#     ips=int(item[3])
#     asns=int(item[4])
#     result.append((sld,childsld,links,ips,asns))

# sorted_by_second = sorted(result, key=lambda tup: tup[2],reverse=True)
# for item in sorted_by_second:
#     final.write(str(item))
#     final.write('\n')
#=================================================
# f=open('/home/sakib/soumya/wholeSLD/finalClubbedFileSorted.txt','r')

# result=list()
# a=list()
# b=list()
# count=0
# linksCount=0
# parent=0
# sldCount=0
# for line in f:
#   data=line.replace('(','').replace(')','').replace("'",'').replace('\n','').replace(' ','').split(',')
#   sld=data[0]
#   childSld=int(data[1])
#   if count<3205:
#     sldCount=sldCount+childSld
#     count=count+1
# print float(sldCount*100)/189181

#   links=int(data[2])
#   linksCount=linksCount+links
#   sldCount=sldCount+childSld
# print linksCount
# print sldCount



#   if parent <3205:
#     linksCount=linksCount+int(links)
#     parent=parent+1
# print linksCount
# print parent
# print float(linksCount*100)/2103163
  # a.append(count)
  # b.append(int(links))
  # count=count+1
#   if ((int(childSld)==0) or (int(childSld)==1)) :
#     f1.write(str(line))
#     childSLDWithLessSLD=childSLDWithLessSLD+1
# print childSLDWithLessSLD
# print float(childSLDWithLessSLD*100)/53852
  # a.append(count)
  # b.append(int(childSld))
  # count=count+1


# print a[:20]
# print b[:20]

# import numpy
# from matplotlib import pyplot as plt
# import matplotlib
# import math
# from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
# from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# fig, ax = plt.subplots(figsize=[5,4])

# plt.loglog(a,b,'ro')

# plt.xlabel("Log (Rank of SLD Cluster infrastructure)")
# plt.ylabel("Log (Number of links on cluster infrastructure)")

# # y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
# # ax.yaxis.set_major_formatter(y_formatter)

# # x_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
# # ax.xaxis.set_major_formatter(x_formatter)
# plt.draw()
# plt.show()

#=====================================
#Clubbed Prefixes
#==================================

# g=open('/home/sakib/soumya/wholeSLD/prefix.txt','r')
# sldTOPrefixDict=defaultdict(list)
# for line in g:
#   sldPrefix=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#   sld=sldPrefix[0]
#   sldPrefix.pop(0)
#   sldTOPrefixDict[sld].append(sldPrefix)

# print "1st step done"
# f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')
# f1=open('/home/sakib/soumya/wholeSLD/clubbedPrefixes.txt','w')

# sldList=['google.com','yunjiasu-cdn.net','wpengine.com','eu-west-1.elb.amazonaws.com'
#         ,'us-east-1.elb.amazonaws.com','ourwebpic.com','edgecastcdn.net','cloudflare.com',
#         'incapdns.net','fastlylb.net','dynect.net','pbwstatic.com','netdna-cdn.com'
#         'cloudflare.net','akamaiedge.net','anycast.me','kxcdn.com','jiashule.com',
#         'alikunlun.com','d5nxst8fruw4z.cloudfront.net','ap-northeast-1.elb.amazonaws.com',
#         'd2t8dj4tr3q9od.cloudfront.net','cdntip.com','us-west-2.elb.amazonaws.com',
#         'ap-southeast-1.elb.amazonaws.com','windows.net']
# result=list()
# count=0
# for value in f:
#     data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     mainSld=data[0]
#     if mainSld in sldList: 
#         del data[-1]
#         asnlist=list()
#         for item in data:
#             if sldTOPrefixDict.get(item) > 0:
#                 asnlist=asnlist+list(itertools.chain.from_iterable(sldTOPrefixDict.get(item)))
#             prefixlist=list()
#             for prefix in asnlist:
#                 if '-' not in prefix:
#                     prefixlist.append(prefix)
#         if len(set(prefixlist)) >0:
#             result.append(str((mainSld,len(set(prefixlist)))))
#         else:
#             result.append(str((mainSld,0)))
# sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
# for item in sorted_by_second:
#     f1.write(str(item))
#     f1.write('\n')

#=======================================
#hypergiants
#=======================================
# k1=open('/home/sakib/soumya/wholeSLD/hyperginats.txt','r')
# import pygal
# xy_chart = pygal.XY(truncate_label=-1,stroke=False,y_title='number of prefixes-->',x_title='number of asns-->',print_labels=True,truncate_legend=-1,legend_at_bottom=True,y_label_rotation=-20,x_label_rotation=-20)
# #xy_chart.x_labels = ['akamaiedge.net','akamai.net','google','ourwebpic.com','cloudflare.com','incapdns.net','dynect.net','cloudflare.net','fastlylb.net','us-east-1.elb.amazonaws','netdna-cdn.com','facebook.com','twitter.com','googleusercontent.com','gandi.net','cdntip.com','eu-west-1.elb.amazonaws','rackspace.com','wp.com','yunjiasu-cdn.net']
# linkscount=0
# highlyDistributedCDN=list()
# highlyDistributedCDNValues=list()
# DistributedCDN=list()
# DistributedCDNValues=list()
# CloudPlatformCDN=list()
# CloudPlatformCDNValues=list()
# contentProviders=list()
# contentProvidersValues=list()
# contentConsumers=list()
# contentConsumersValues=list()

# rest=list()
# restValues=list()

# valueslist=list()

# restValueslist=list()
# for line in k1:
#     data=line.replace('(','').replace(')','').replace("'",'').replace('\n','').replace(' ','').split(',')

#     if int(data[5]) >190 and int(data[4]) >20:
#         highlyDistributedCDN.append((int(data[4]),int(data[5])))
#         highlyDistributedCDNValues.append(({'value':(int(data[4]),int(data[5])), 'label': data[0]}))
#     elif int(data[4]) >10 and int(data[4]) <30 and int(data[5]) <180:
#         DistributedCDN.append((int(data[4]),int(data[5])))
#         DistributedCDNValues.append({'value':(int(data[4]),int(data[5])), 'label': data[0]})
#     elif int(data[5]) >100 and int(data[4]) >0 and int(data[4]) <15:
#         CloudPlatformCDN.append((int(data[4]),int(data[5])))
#         CloudPlatformCDNValues.append({'value':(int(data[4]),int(data[5])), 'label': data[0]})
#     elif int(data[5]) >10 and int(data[4]) ==1:
#         contentProviders.append((int(data[4]),int(data[5])))
#         contentProvidersValues.append({'value':(int(data[4]),int(data[5])), 'label': data[0]})
#     else:
#         rest.append((int(data[4]),int(data[5])))
#         restValueslist.append(data[0])
#         restValues.append({'value':(int(data[4]),int(data[5])),'label': data[0]})

# #print "highlyDistributedCDNValues",highlyDistributedCDNValues
# #print "DistributedCDNValues",DistributedCDNValues
# #print "CloudPlatformCDNValues",CloudPlatformCDNValues
# #print "contentProvidersValues",contentProvidersValues


# #print restValueslist
# xy_chart.add('Highly Distributed CDNs',highlyDistributedCDNValues)
# xy_chart.add('Distributed CDNs',DistributedCDNValues)
# xy_chart.add('Cloud Platform CDN',CloudPlatformCDNValues)
# xy_chart.add('Content Producers',contentProvidersValues)
# xy_chart.add('DataCenters',restValues)
# xy_chart.render_to_png('/home/sakib/soumya/wholeSLD/finalhyper.png')

#==========================================
#hyperginat objects
#===========================================

# from collections import Counter

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:
#     if line[7] != '-':
#         sldTOASNDict[line[7]].append(line[3].split(';')[0])

# f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')


# sldList=['pbwstatic.com']
# # ,'yunjiasu-cdn.net','wpengine.com',
# #'eu-west-1.elb.amazonaws.com'
# #         ,'us-east-1.elb.amazonaws.com','ourwebpic.com','edgecastcdn.net','cloudflare.com',
# #         'incapdns.net','fastlylb.net','dynect.net','pbwstatic.com','netdna-cdn.com'
# #         'cloudflare.net','akamaiedge.net','anycast.me','kxcdn.com','jiashule.com',
# #         'alikunlun.com','d5nxst8fruw4z.cloudfront.net','ap-northeast-1.elb.amazonaws.com',
# #         'd2t8dj4tr3q9od.cloudfront.net','cdntip.com','us-west-2.elb.amazonaws.com',
# #         'ap-southeast-1.elb.amazonaws.com','windows.net'
# result=list()
# count=0
# for value in f:
#     data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     mainSld=data[0]
#     del data[-1]
#     if mainSld in sldList:
#         result=result + data

# print result[:20]
# print len(result)


# objectlist=list()
# for item in result:
#     if sldTOASNDict.get(item):
#         objectlist=objectlist + list(sldTOASNDict.get(item))
# print objectlist[:20]
# f1=open('/home/sakib/soumya/wholeSLD/objectpbwstatic.txt','w')
# # for value in objectlist:
# #     f1.write(str(value))
# #     f1.write('\n')
# cnt = Counter()
# for word in objectlist:
#     cnt[word] += 1
# print cnt.most_common(50)
# for k,v in cnt.iteritems():
#     f1.write(str((k,v)))
#     f1.write('\n')

# objectDict=defaultdict(list)

# for word in objectlist:

# import glob

# read_files = glob.glob("/home/sakib/soumya/wholeSLD/objectCount/*.txt")

# with open("/home/sakib/soumya/wholeSLD/objectCount/result.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())


#==================
#object
#==================
# import pygal
# line_chart = pygal.HorizontalBar(truncate_legend=-1,legend_at_bottom=True,x_title='percentage of objects-->')

# g=open('/home/sakib/soumya/wholeSLD/objectCount/hypergiantresult.txt','r')
# count=0
# objectCount=defaultdict(list)
# for line in g:
#   value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#   # objectCount[value[0]].append(value[-1])
#   count=count+int(value[1])
# print count
# f=open('/home/sakib/soumya/wholeSLD/objectCount/hypergiantresult.txt','w')
# result=list()
# for k,v in objectCount.items():
#     if objectCount.get(k):
#         value=objectCount.get(k)
#         print value
#         count=0
#         for item in value:
#             count=count+int(item)
#     result.append((k,count))
# # f.write(str((k,count)))
# # f.write

# sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
# for item in sorted_by_second:
#     f.write(str(item))
#     f.write('\n')


# import pygal
# line_chart = pygal.HorizontalBar(truncate_legend=-1,legend_at_bottom=True,x_title='percentage of objects-->')


# h=open('/home/sakib/soumya/wholeSLD/objectCount/hypergiantresult.txt','r')
# newcount=0
# for line in h:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     ob=int(value[1])
#     if newcount<11:
#         line_chart.add(value[0], float(ob*100)/count)
#     else:
#         break
#     newcount=newcount+1

# line_chart.render_to_png('/home/sakib/soumya/wholeSLD/objectCount/hypergiant.png')

#==================
#objects via hypergiant
#==================
# g=open('/home/sakib/soumya/wholeSLD/objectCount/objectd5nxst8fruw4.txt','r')
# count=0
# objectCounttext=0
# objectCountImage=0
# objectCountApplication=0
# for line in g:
#   value=line.replace('(','').replace(')','').split(',')
#   count=count+int(value[-1])
#   if 'text' in value[0].lower():
#     objectCounttext=objectCounttext+int(value[-1])
#   if 'image' in value[0].lower():
#     objectCountImage=objectCountImage+int(value[-1])
#   if 'application' in value[0].lower():
#     objectCountApplication=objectCountApplication+int(value[-1])

# print ('text',float(objectCounttext*100)/count)
# print ('image',float(objectCountImage*100)/count)
# print ('application',float(objectCountApplication*100)/count)

# if 'application' in value[0]:
#     objectCount=objectCount+int(value[1])
  #count=count+int(value[-1])
#print count
#print float(6063814*100)/count


# import pygal
# line_chart = pygal.HorizontalBar(truncate_legend=-1,legend_at_bottom=True,x_title='percentage of objects-->')


# h=open('/home/sakib/soumya/wholeSLD/objectCount/objectalikunluncom.txt','r')
# newcount=0
# for line in h:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     # ob=int(value[-1])
#     # print (value[0],float(ob*100)/8881814)
#     if 'application' in value[0]
#         #sline_chart.add(value[0], float(ob*100)/count)
#         newcount=newcount+1
#     else:
#         break
    

# line_chart.render_to_png('/home/sakib/soumya/wholeSLD/objectCom/hypergiantNew.png')

#IP to geolocation
# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# index=set()
# for line in finaloutputre:
#     index.add(line[0])
# print len(index)

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:
#     if line[7] != '-':
#         sldTOASNDict[line[7]].append(line[8].split(';')[0])

# def test(sld,sldTOASNDict):
#     f=open('/home/sakib/soumya/wholeSLD/clubbedSLD.txt','r')
#     #sldList=['eu-west-1.elb.amazonaws.com']
#     result=list()
#     count=0
#     for value in f:
#         data=value.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#         mainSld=data[0]
#         del data[-1]
#         if mainSld == sld:
#             result=result + data

#     print result[:20]
#     print len(result)

#     objectlist=list()
#     for item in result:
#         if sldTOASNDict.get(item):
#             objectlist=objectlist + list(sldTOASNDict.get(item))
#     print objectlist[:20]

#     f1=open('/home/sakib/soumya/wholeSLD/geo/countries/countries_'+sld+'.txt','w')
#     f2=open('/home/sakib/soumya/wholeSLD/geo/countinent/continent_'+sld+'.txt','w')
#     from geoip import geolite2
#     for ip in set(objectlist):
#         match = geolite2.lookup(ip)
#         if match is not None :
#             f1.write(str((match.country,ip)))
#             f1.write('\n')
#             f2.write(str((match.continent,ip)))
#             f2.write('\n')
#     return


# sldList=['us-east-1.elb.amazonaws.com','ourwebpic.com','edgecastcdn.net','cloudflare.com',
#         'incapdns.net','fastlylb.net','dynect.net','pbwstatic.com','netdna-cdn.com',
#         'cloudflare.net','akamaiedge.net','anycast.me','kxcdn.com','jiashule.com',
#         'alikunlun.com','d5nxst8fruw4z.cloudfront.net','ap-northeast-1.elb.amazonaws.com',
#         'd2t8dj4tr3q9od.cloudfront.net','cdntip.com','us-west-2.elb.amazonaws.com',
#         'ap-southeast-1.elb.amazonaws.com','windows.net']

# finaloutput=codecs.open("/home/sakib/soumya/wholeSLD/finaloutput.csv",'rU')
# finaloutputre = csv.reader(finaloutput,skipinitialspace=True,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# sldTOASNDict=defaultdict(list)
# for line in finaloutputre:
#     if line[7] != '-':
#         sldTOASNDict[line[7]].append(line[8].split(';')[0])

# for sld in sldList:
#     test(sld,sldTOASNDict)
#==================================================
#CountryList
#==================================================

# import glob

# read_files = glob.glob("/home/sakib/soumya/wholeSLD/geo/countries/*.txt")

# with open("/home/sakib/soumya/wholeSLD/geo/countries/countries_result.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())


# g = open("/home/sakib/soumya/wholeSLD/geo/countries/countries_result.txt",'r')
# f = open("/home/sakib/soumya/wholeSLD/geo/countriesnew/countries_Count.txt",'w')
# countrylist=defaultdict(list)
# for line in g:
#   value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#   countrylist[value[0]].append(value[1])

# result=list()
# for k,v in countrylist.items():
#     result.append((k,len(v)))
# sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
# for item in sorted_by_second:
#     f.write(str(item))
#     f.write('\n')

#==================================================
#continent
#==================================================

# import glob

# read_files = glob.glob("/home/sakib/soumya/wholeSLD/geo/countinent/*.txt")

# with open("/home/sakib/soumya/wholeSLD/geo/countinent/continent_result.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())


# g = open("/home/sakib/soumya/wholeSLD/geo/countinent/continent_result.txt",'r')
# f = open("/home/sakib/soumya/wholeSLD/geo/countinent/continent_count.txt",'w')
# countrylist=defaultdict(list)
# for line in g:
#   value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#   countrylist[value[0]].append(value[1])

# result=list()
# for k,v in countrylist.items():
#     result.append((k,len(v)))
# sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
# for item in sorted_by_second:
#     f.write(str(item))
#     f.write('\n')

#======================================
#hyperginat specific countries
#======================================
# import os
# import glob
# for filename in glob.glob('/home/sakib/soumya/wholeSLD/geo/countries/*.txt'):
#     g = open(filename,'r')
#     #filefirstName=filename.split('.')
#     f = open(filename+'_countriesNew.txt','w')
#     countrylist=defaultdict(list)
#     for line in g:
#       value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#       countrylist[value[0]].append(value[1])

#     result=list()
#     for k,v in countrylist.items():
#         result.append((k,len(v)))
#     sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
#     for item in sorted_by_second:
#         f.write(str(item))
#         f.write('\n')

#======================================
#hyperginat specific countries
#======================================
# import os
# import glob
# for filename in glob.glob('/home/sakib/soumya/wholeSLD/geo/countinent/*.txt'):
#     g = open(filename,'r')
#     filefirstName=filename.split('.')
#     f = open(filefirstName[0]+'_countinent','w')
#     countrylist=defaultdict(list)
#     for line in g:
#       value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#       countrylist[value[0]].append(value[1])

#     result=list()
#     for k,v in countrylist.items():
#         result.append((k,len(v)))
#     sorted_by_second = sorted(result, key=lambda tup: tup[1],reverse=True)
#     for item in sorted_by_second:
#         f.write(str(item))
#         f.write('\n')

#======================================
#hyperginat Infrastructure Identification
#======================================

# import os
# import glob



# def test(country,f):
#     countryCount=0
#     for filename in glob.glob('/home/sakib/soumya/wholeSLD/geo/countriesnew/*.txt'):
#         #filefirstName=filename.split('.')
#         g = open(filename,'r')
#         for line in g:
#           value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#           countryCount=countryCount+int(value[1])

#         #print "filename",filefirstName
#         print "countryCount",countryCount

#         h = open(filename,'r')
#         for line in h:
#           value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#           if value[0]==country:
#             per=round(float(int(value[1])*100)/countryCount,2)
#             f.write(str((filename,value[0],per)))
#             f.write('\n')
#     return

# k=open('/home/sakib/soumya/wholeSLD/geo/countriesnew/count/countries_Count.txt','r')
# countries=set()
# for line in k:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     countries.add(value[0])

# print "countries",countries
# f=open('/home/sakib/soumya/wholeSLD/geo/countriesnew/count/infra.txt','w')
# for country in countries:
#     test(country,f)



f=open('/home/sakib/soumya/wholeSLD/geo/countriesnew/count/infra.txt','r')
dicttest=defaultdict(list)
for line in f:
    value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
    sldName=(value[0].split("countries_"))[1].split('.')[0]
    sldName_Countries=sldName+'_'+value[1]
    dicttest[sldName_Countries].append(value[2])

#f=open('/home/sakib/soumya/wholeSLD/geo/countriesnew/count/infrafinal.txt','w')
for k,v in dicttest.items():
    country=k.split('_')[1]
    if country=='US':
        print (k,v)

# import pygal
# line_chart = pygal.StackedBar()

# line_chart.add('US', [12.05, 11.44, 1.06, 0.2,47.88,7.82,0.02,0.89,64.05,1.92,0.09,3.37,0.04,9.59,2.02,1.46,6.21,99.94,0.01,1.44,0.07,1.71,None,None,None,None])
# line_chart.add('CN',  [None, None, None, None,None,None,8.32,None,None,None,1.83, None, None, None,None,13.74,None,None,4.36,None,None,None,2.47,None,None,None])
# line_chart.add('IE', [None, 0.02, None, None,0.01,None,None,None,None,None,None, 5.89, 0.02, 0.03,None,None,None,None,None,None,None,0.08,None,None,None,None])
# line_chart.add('JP', [25.94, None, 0.01, None,None,None,None,None,None,None,None, None, None, 0.75,None,None,None,None,None,None,None,0.0,None,None,None,None])
# line_chart.add('FR', [None, 0.02, None, None,None,None,None,None,None,None,None, 0.0, 3.5, None,None,None,None,None,None,None,None,None,None,1.16,None,None])
# line_chart.add('SG', [0.04, None, 0.04, None,0.0,None,None,None,None,None,None, None, None, None,None,0.02,9.94,0.06,None,None,None,0.0,None,None,None,None])
# line_chart.add('DE', [None, 0.01, 2.0, None,0.0,None,None,None,0.32,None,None, 0.0, 0.15, None,None,None,None,None,0.03,None,None,None,None,1.28,None,None])
# line_chart.add('GB', [None, None, 0.02, None,None,0.0,None,0.02,None,None,None, 0.01, 0.19, 1.93,None,None,None,None,None,None,None,None,None,None,None,None])
# line_chart.add('ES', [None, None, None, None,0.0,None,None,None,None,None,None, 0.0, 0.44, None,None,None,None,None,None,None,None,None,None,0.0,None,None])
# line_chart.add('PL', [None, None, None, None,None,None,None,None,None,None,None, None, 0.37, None,None,None,None,None,None,None,None,None,None,0.37,None,None])
# line_chart.add('CA', [None, None, None, None,0.0,None,None,None,None,None,None, None, 0.15, None,None,None,None,None,0.4,None,None,None,None,None,None,None])
# line_chart.add('HK', [None, None, None, None,None,None,0.27,None,None,None,None, None, None, 0.06,None,0.03,None,None,None,None,None,0.0,None,None,None,None])
# line_chart.add('NL', [None, None, None, None,None,None,None,None,0.3,None,None, None, 0.05, None,None,None,None,None,0.04,None,None,0.07,None,0.01,None,None])
#line_chart.add('IT', [None1, None2, 0.09, None4,None5,None6,None7,None8,None9,None10,None11, None12, 0.14, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,0.14,None25,None26])
# line_chart.add('AU', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, None12, None13, 0.1,None15,None16,None17,None18,None19,None20,None21,0.01,None23,None24,None25,None26])
# line_chart.add('CZ', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, None12, 0.04, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('BE', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, 0.03, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('FI', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, 0.03, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('LT', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, None12, 0.03, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('CH', [None1, None2, None3, None4,None5,0.0,None7,None8,None9,None10,None11, None12, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,0.02,None25,None26])
# line_chart.add('PT', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, None12, 0.03, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('RO', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, None12, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,0.02,None25,None26])
# line_chart.add('SE', [None1, 0.01, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('BR', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, None12, None13, None14,None15,None16,None17,None18,None19,None20,None21,0.01,None23,None24,None25,None26])
# line_chart.add('RU', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('TR', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('ZA', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('AR', [None1, None2, None3, None4,0.0,None6,None7,None8,None9,None10,None11, None12, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('KR', [None1, None2, None3, None4,0.0,None6,None7,None8,None9,None10,None11, None12, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
# line_chart.add('IL', [None1, None2, None3, None4,None5,None6,None7,None8,None9,None10,None11, 0.0, None13, None14,None15,None16,None17,None18,None19,None20,None21,None22,None23,None24,None25,None26])
#line_chart.render_to_png("/home/sakib/soumya/wholeSLD/geo/hyper.png")