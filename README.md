# SFmuniMaps
Create maps of SF muni using the nextbus webservices API

To download

```git clone https://github.com/Tmonster/SFmuniMaps```

In order for the graphics to work copy and paste the code in the file below into a subdirectory called graphicsdir

http://mcsp.wartburg.edu/zelle/python/graphics.py

To draw the map invoke a python shell and run ```import drawMap```

OR just execute ```python drawMap.py``` But this command will erase the map once it's been drawn. Therefore importing the map in the shell is a better idea.

The map should look like this. 
![SFMUNI MAP](https://github.com/Tmonster/SFmuniMaps/blob/master/SFMap.jpg "SFMUNI MAP")

If you want to change what is drawn, refer to the instructions on how to access the nextbus xml data located here.
http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf
