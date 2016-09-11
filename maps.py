#By Storm Shadow http://techbliss.org
import ico
import json
import os
import PyQt4
from PyQt4 import QtCore,  QtGui
import PyQt4.QtWebKit
import PyQt4.QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView
import pygeoip
import string


gi = pygeoip.GeoIP('GeoIPCity.dat')
ipadr = raw_input("Enter Ip Adress\n")
j = gi.record_by_addr(ipadr)
latte = str(j[u'latitude'])
Lotte = str(j[u'longitude'])
foo = (latte +","+ Lotte)


YOURAPIKEY = "" #enter your Google Maps JavaScript API
java = '''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {
        var myLatLng = {lat: Pizza1, lng: Pizza2};

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: myLatLng
        });

        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: 'There they are'
        });
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=APIKEY&callback=initMap">
    </script>
  </body>
</html>
'''

new_str1 = string.replace(java, 'Pizza1', str(j[u'latitude']))
new_str2 = string.replace(new_str1, 'Pizza2', str(j[u'longitude']))
new_str3 = string.replace(new_str2, 'APIKEY', YOURAPIKEY)
maphtml = new_str3


class LookUp(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])
        self.window = QWidget()
        self.window.setWindowTitle("IP Geolocator")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/mind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.setWindowFlags(PyQt4.QtCore.Qt.WindowStaysOnTopHint)
        self.window.setWindowIcon(icon)

        self.web = QWebView(self.window)
        self.web.setMinimumSize(1024,800)
        self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)
        self.web.setHtml(maphtml)
        self.layout = QVBoxLayout(self.window)
        self.layout.addWidget(self.web)


        self.window.show()
        self.exec_()


LookUp()