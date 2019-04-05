import calendar
import requests
from datetime import datetime, timedelata, date, time
import imageio


class forecast():

    api_url = 'http://magicseaweed.com/api/5142c266149ab8ebd6ac4cba3283da6b/forecast'
    spotID = ''
    settingsPath = ''
    units = 'eu'
    windDirection = ''
    windMagnitude = ''
    swellMinHeight = ''
    swellMaxHeight = ''
    swellProbability = ''
    temperature = ''
    pressure = ''
    gifSwell = ''
    gifPeriod = ''
    gifWind = ''
    gifPressure = ''
    windCompass = ''
    swellCompass = ''
    ratingSolidStars = ''
    ratingFadedStars = ''

    def __init__(self, spot_id, units='eu', local_datetime = None):

        if local_datetime is not None:
            try:
                response = requests.get('{0}?spot_id={1}&units={2}'.format(self.api_url, spot_id, units))
