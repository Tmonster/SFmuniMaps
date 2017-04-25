import time
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import json
import requests
import sys
sys.path.insert(0, 'graphicsdir/')
from graphics import *
# r = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=N")
f = open("paths.xml", "r")
routes = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni")
routesjson = json.loads(dumps(bf.data(fromstring(routes.content))))

xoffset = 12251901
ymax    = 3781993
yoffset = 3769931
divSize = 20
win = GraphWin("Main", float(16000)/float(divSize),float(16000)/float(divSize))
count = 0
for route in routesjson["body"]["route"]:
    routeinfo = requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r="+str(route["@tag"]))
    routeinfojson = json.loads(dumps(bf.data(fromstring(routeinfo.content))))
    print "Drawing " + str(route["@tag"])
    for path in routeinfojson["body"]["route"]["path"]:
        reset = True
        for point in path["point"]:
            x = (abs(float(point["@lon"])) * 100000)
            y = (abs(float(point["@lat"])) * 100000)
            x = (xoffset- x)/divSize
            y = (ymax - y)/divSize
            curpoint = Point(x, y)
            if reset:
                line = Line(curpoint, curpoint)
                reset = False
            else:
                line = Line(curpoint, prevpoint)
            line.draw(win)
            prevpoint = curpoint
    if count < -1 :
        break
    else:
        count += 1

