import pygal

#==========================
#COUNTRY
#==========================
# line_chart = pygal.Bar(show_x_labels=True,x_label_rotation=20,print_values_position='top',print_values=True,print_labels=True,truncate_legend=-1,legend_at_bottom=True,y_title='percentage of IP addresses-->',x_title='country codes-->')

# h=open('/home/sakib/soumya/wholeSLD/geo/countries_Count.txt','r')
# countriesCount=0
# for line in h:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     countriesCount=countriesCount+int(value[1])

# f=open('/home/sakib/soumya/wholeSLD/geo/countries_Count.txt','r')
# count=0
# for line in f:
# 	if count<10:
# 		value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
# 		line_chart.add(value[0], round(float(int(value[1])*100)/countriesCount,2))
# 		count=count+1
# 	else:
# 		break
# line_chart.render_to_png('/home/sakib/soumya/wholeSLD/geo/countries_all.png')
# from pygal.style import Style
# custom_style = Style(background='transparent',plot_background='transparent')
# worldmap_chart = pygal.maps.world.World()
# f=open('/home/sakib/soumya/wholeSLD/geo/countries_Count.txt','r')
# worldlist=list()
# worldlist20=list()
# worldlist10=list()
# worldlist3=list()
# worldlist0=list()
# for line in f:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     per=int(value[1])*100/countriesCount
#     if per > 50 :
#     	worldlist.append(value[0].lower())
#     elif per >20 and per < 50 :
#     	worldlist20.append(value[0].lower())
#     elif per >3 and per < 10 :
#     	worldlist10.append(value[0].lower())
#     elif per >1 and per < 3 :
#     	worldlist3.append(value[0].lower())
#     elif per < 1 :
#     	worldlist0.append(value[0].lower())
# print "worldlist",worldlist
# print "worldlist20",worldlist20
# print "worldlist10",worldlist10
# worldmap_chart.add('More than 50%',worldlist)
# worldmap_chart.add('Within 20-50%',worldlist20)
# worldmap_chart.add('Within 3-10%',worldlist10)
# worldmap_chart.add('Within 1-3%',worldlist3)
# worldmap_chart.add('Within 1%',worldlist0)
# worldmap_chart.render_to_png('/home/sakib/soumya/wholeSLD/geo/world_countries_all.png')
#worldmap_chart.render_to_file('/home/sakib/soumya/wholeSLD/geo/world_countries_all.svg')

#==========================
#cONTINENT
#==========================
#line_chart = pygal.Bar(show_x_labels=True,x_label_rotation=20,print_values_position='top',print_values=True,print_labels=True,truncate_legend=-1,legend_at_bottom=True,y_title='percentage of IP addresses-->',x_title='continents-->')

# h=open('/home/sakib/soumya/wholeSLD/geo/continent_count.txt','r')
# countriesCount=0
# for line in h:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     countriesCount=countriesCount+int(value[1])
# f=open('/home/sakib/soumya/wholeSLD/geo/continent_count.txt','r')
# count=0
# for line in f:
# 	value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
# 	print (value[0],round(float(int(value[1])*100)/countriesCount,2))


# line_chart.add('North America', 57.16)
# line_chart.add('Asia', 27.93)
# line_chart.add('Europe',14.84)
# line_chart.add('Oceania', 0.07)
# line_chart.add('South America', 0.01)
# line_chart.add('Africa', 0.001)
# line_chart.render_to_png('/home/sakib/soumya/wholeSLD/geo/continent_all.png')
# from pygal.style import Style
# custom_style = Style(background='transparent',plot_background='transparent')
# worldmap_chart = pygal.maps.world.World()
# f=open('/home/sakib/soumya/wholeSLD/geo/countries_Count.txt','r')
# worldlist=list()
# worldlist20=list()
# worldlist10=list()
# worldlist3=list()
# worldlist0=list()
# for line in f:
#     value=line.replace('(','').replace(')','').replace('[','').replace(']','').replace('set','').replace("'",'').replace('\n','').replace(' ','').split(',')
#     per=int(value[1])*100/countriesCount
#     if per > 50 :
#     	worldlist.append(value[0].lower())
#     elif per >20 and per < 50 :
#     	worldlist20.append(value[0].lower())
#     elif per >3 and per < 10 :
#     	worldlist10.append(value[0].lower())
#     elif per >1 and per < 3 :
#     	worldlist3.append(value[0].lower())
#     elif per < 1 :
#     	worldlist0.append(value[0].lower())
# print "worldlist",worldlist
# print "worldlist20",worldlist20
# print "worldlist10",worldlist10
# worldmap_chart.add('More than 50%',worldlist)
# worldmap_chart.add('Within 20-50%',worldlist20)
# worldmap_chart.add('Within 3-10%',worldlist10)
# worldmap_chart.add('Within 1-3%',worldlist3)
# worldmap_chart.add('Within 1%',worldlist0)
# worldmap_chart.render_to_png('/home/sakib/soumya/wholeSLD/geo/world_countries_all.png')
#worldmap_chart.render_to_file('/home/sakib/soumya/wholeSLD/geo/world_countries_all.svg')


