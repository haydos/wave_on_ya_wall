# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:47:16 2018

@author: Shannon
"""
import calendar
import requests
from datetime import datetime, timedelta, date, time
import imageio
from forecast import forecast



model = forecast(1004)

spot_id = 1004
#    d = date(2018, 1, 22)
#    t = time(12, 00)
#    dt = datetime.combine(d,t)
#    
#    forecast = msw.get_forecast(spot_id,"eu",dt)
#    print forecast

forecastDateTimes = []
numDays = 2
numHours = 24 * numDays
for xhours in range(0, numHours, 3):
    forecastDateTimes.append(datetime.now() + timedelta(hours=xhours))


images = []
for forecastDateTime in forecastDateTimes:
    forecastTemp = model.get_forecast(spot_id,model.units,forecastDateTime)
    imgSwellURL = forecastTemp['charts']['swell']
    print (imgSwellURL)
    imgSwellData = requests.get(imgSwellURL).content
    images.append(imageio.imread(imgSwellData,'gif'))
    
imageio.mimsave('movie2.gif', images, duration=.5)
        
        