import requests

from bs4 import BeautifulSoup as BS

import facebook

import requests
import facebook
from bs4 import BeautifulSoup as BS

with open ('fbkey', 'r') as f:
    key = f.readlines()

graph = facebook.GraphAPI(access_token = key) 

river_url = 'http://water.weather.gov/ahps2/river.php?wfo=SHV&wfoid=18715&riverid=203413&pt%5B%5D=all&allpoints=143204%2C147710%2C141425%2C144668%2C141750%2C141658%2C141942%2C143491%2C144810%2C143165%2C145368&data%5B%5D=xml'

headers = {"user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
r= requests.get(river_url, headers=headers)
soup = BS(r.text, 'lxml')

#process the data returned from waterdata.usgs.gov

stations = soup.find_all('h1', attrs={'class': 'data_name'})
stages = soup.find_all('div', attrs={'class': 'stage_stage_flow'})
flood_lvl = soup.find_all('div', attrs={'class': 'flood_stage_flow'})
warns = soup.find_all('div', attrs={'class': 'current_warns_statmnts_ads'})
alerts = soup.find_all('td', attrs={'scope': 'col'})

num_river = len(stations)
#strip the html formatting and build our lists
stx_list = []
stage_list = []
flood_list = []
warns_list = []

for i in range(num_river):
    stx_list.append((stations[i].text.strip()))
    stage_list.append((stages[i].text.strip()))
    flood_list.append((flood_lvl[i].text.strip()))
    warns_list.append((warns[i].text.strip()))

#setup the alert system with appropriate values and corresponding warning stage for each river station.
alert_list = []
alert_values = []
for i in range(len(alerts)):
    alert_list.append((alerts[i].text.strip())) 

a_values = alert_list[1::2]
alert_list.clear()

#get current river level (stage)
stages = []
levels = []
for i in range(num_river):
    s = stage_list[i].split()
    stages.append(s)
for i in range(num_river):
    s = stages[i][2]
    levels.append(s) 

stages.clear()

#build current warning list
warns = []
for i in range(len(warns_list)):
    w = warns_list[0].strip('Current Warnings/Statements/Advisories:')
    warns.append(w)

#build Major, Moderate, Flood, Action values lists
major_lvl = a_values[::5]
moderate_lvl = a_values[1::5]
flood_lvl = a_values[2::5]
action_lvl = a_values[3::5]

num_stx = len(stx_list)
class River():
   def __init__(self, station, stage, major, moderate, flood, action, warn):
       self.station = station
       self.stage = stage
       self.major = major
       self.moderate = moderate
       self.flood = flood
       self.action = action
       self.warn = warn

       if self.major == 0:
            self.major = self.action
       if self.moderate == 0:
            self.moderate = self.action
       if self.flood == 0:
            self.flood = self.action

   def alerts(self):          
        if float(self.stage) < float(self.action):
            pass
        elif float(self.stage) >= float(self.major):
            graph.put_object(parent_object='me', connection_name='feed', message=('The %s has reached [Major Flood Stage: (%sFt)] @ %sFt.\n\n***Warnings***\n%s\n\nPlease click the Link below for more information.' % (self.station, self.major, self.stage, self.warn)), link = river_url)
        elif float(self.stage) >= float(self.moderate):
            maj_diff = round(float(self.stage) - float(self.moderate), 2)
            graph.put_object(parent_object='me', connection_name='feed', message=('The %s has reached [Moderate Flood Stage: (%sFt)] @ %sFt.\n\nNext stage is [Major Flood Stage] in %sFt.\n\n***Warnings***\n%s\n\nPlease click the Link below for more information.' % (self.station, self.moderate, self.stage, maj,diff, self.warn)), link = river_url)
        elif float(self.stage) >= float(self.flood):
            mod_diff = round(float(self.stage) - float(self.flood), 2)
            warn = graph.put_object(parent_object='me', connection_name='feed', message=('The %s has reached [Flood Stage: (%sFt)] @ %sFt.\n\nNext stage is [Moderate Flood Stage] in %sFt.\n\n***Warnings***\n%s\n\nPlease click the Link below for more information.' % (self.station, self.flood, self.stage, mod_diff, self.warn)), link = river_url)
        elif float(self.stage) >= float(self.action):
            flood_diff = round(float(self.stage) - float(self.action), 2)
            warn = graph.put_object(parent_object='me', connection_name='feed', message=('The %s has reached [Action Flood Stage: (%sFt)] @ %sFt.\n\nNext stage is [Flood Stage] in %sFt.\n\n***Warnings***\n%s\n\nPlease click the Link below for more information.' % (self.station, self.action, self.stage, flood_diff, self.warn)), link = river_url)


def riverlist():
    river_list = []
    for n in range(len(stx_list)):
        station = River(stx_list[n], levels[n], major_lvl[n], moderate_lvl[n], flood_lvl[n], action_lvl[n], warns[n])
        river_list.append(station)
    return river_list

if __name__ == '__main__':
    for river in riverlist():
        print(river.alerts())
