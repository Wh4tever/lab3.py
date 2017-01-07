import requests
import json
from datetime import datetime, date, time
from time import time
op = open('index.html', 'w+', encoding='utf-8')
op.write('<!DOCTYPE html><html><head></head><body>')
timeBeg = time()
timeEnd = timeBeg + 604800
city = 'Los Angeles'

req = requests.get('https://api.meetup.com/2/open_events?and_text=False&country=us&offset=0&city=Los+Angeles&format=json&limited_events=False&state=ca&photo-host=public&page=20&radius=1&desc=False&status=upcoming&sig_id=216713652&sig=0b9e715a0020fc920ec915af58a530978e7613a8&key=1e247e3d3c54156541f171414741e1e').json()


for i in range(7):
    if i == 0: op.write('<h2>Monday</h2>')
    elif i == 1: op.write('<h2>Tuesday</h2>')
    elif i == 2: op.write('<h2>Wednesday</h2>')
    elif i == 3: op.write('<h2>Thursday</h2>')
    elif i == 4: op.write('<h2>Friday</h2>')
    elif i == 5: op.write('<h2>Saturday</h2>')
    elif i == 6: op.write('<h2>Sunday</h2>')
    for item in req['results']:
        d = datetime.fromtimestamp(int(item['time']) / 1000).weekday()
        if d == i:
            try:
                op.write('<style> .brd { border-bottom: 2px solid black; padding: 10px; }</style><div class="brd"><p><b>Time</b>: ' + str(datetime.fromtimestamp(int(item['time']) / 1000)) + '</p>')
            except KeyError:pass
            try:
                op.write('<p><b>Name</b>: ' + str(item['name'] + '</p>'))
            except KeyError:pass
            try:
                op.write('<p><b>Organizer</b>: ' + str((item['group'])['name'])+'</p>')
            except KeyError:pass
            try:
                op.write('<p><b>Description</b>: ' + str(item['description']) + '</p>')
            except KeyError:pass
            try:
                op.write("<p>Phone: " + str((item['venue'])['phone']) + '</p>')
            except KeyError:pass
            try:
                op.write("<p>Country: " + str((item['venue'])['localized_country_name']) + '</p>')
            except KeyError:pass
            try:
                op.write('<p>City: ' + str((item['venue'])['city']) + '</p>')
            except KeyError:pass
            try:
                op.write('<p>Address: ' + str((item['venue'])['address_1']) + '</p>')
            except KeyError:pass
          
          
            op.write('</div>')
op.write('</body></html>')
op.close()