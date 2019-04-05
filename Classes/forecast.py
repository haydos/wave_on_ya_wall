import calendar
import requests
from datetime import datetime, timedelta



class forecast():

    api_url = 'http://magicseaweed.com/api/5142c266149ab8ebd6ac4cba3283da6b/forecast'
    spotID = ''
    settingsPath = ''
    units = 'uk'

    # JSON DATA
    gifPeriod = ''
    gifPressure = ''
    gifSwell = ''
    gifWind = ''

    pressure = ''
    pressureUnits = ''
    temperature = ''
    temperatureUnits = ''
    weather = ''

    ratingSolidStars = ''
    ratingFadedStars = ''

    localTimeStampUNIX = '' #NEW
    localTimeStamp = '' #NEW

    primDirection = ''
    primCompass = ''
    primHeight = ''
    primPeriod = ''

    secondDirection = ''
    secondCompass = ''
    secondHeight = ''
    secondPeriod = ''

    tertiartyDirection = ''
    tertiartyCompass = ''
    tertiartyHeight = ''
    tertiartyPeriod = ''

    swellProbability = ''
    swellUnits = ''


    windChill = ''
    windCompass = ''
    windDirection = ''
    windGusts = ''
    windSpeed = ''
    windUnits = ''



    # Class Initialiser - calls getForecast if arguments passed to it
    def __init__(self, spot_id, units='eu', local_datetime = None):
        if local_datetime is not None:
            try:
                response = requests.get('{0}?spot_id={1}&units={2}'.format(self.api_url, spot_id, units))
            except:
                raise TypeError('local_datetime must be of type datetime.datetime')
            return
        return

    # Returns an UNIX timestamp as str given a datetime instance.
    @staticmethod
    def timestamp_from_datetime(dt):
        return calendar.timegm(dt.timetuple())

    # Returns a DateTime instance from a UNIX timestamp
    @staticmethod
    def datetime_from_timestamp(ts):
        return datetime.utcfromtimestamp(int(ts))

    # Returns the next available forecast timeframe as datetime.
    """ Magicseaweed provides 8 forecasts for a given day, as follows:
           1  00:00:00
           2  03:00:00
           3  06:00:00
           4  09:00:00
           5  12:00:00
           6  15:00:00
           7  18:00:00
           8  21:00:00

           Example:
           If datetime.datetime(2014, 10, 30, 10, 0, 0) is passed as argument,
           this function returns datetime.datetime(2014, 10, 30, 12, 0, 0).

           """
    @staticmethod
    def round_timeframe(dt):
        while dt.hour % 3 != 0:
            dt = dt + timedelta(hours=1)
        return datetime(dt.year, dt.month, dt.day, dt.hour, 0, 0)

    # Makes requests to Magicseaweed's forecast API. The default unit is European.
    @classmethod
    def get_forecast(self, spot_id, units='eu', local_datetime=None):
        response = requests.get('{0}?spot_id={1}&units={2}'.format(self.api_url, spot_id, units))
        if local_datetime is not None:
            try:
                local_datetime = self.round_timeframe(local_datetime)
            except:
                raise TypeError('local_datetime must be of type datetime.datetime')
            local_timestamp = self.timestamp_from_datetime(local_datetime)
            for forecast in response.json():
                if forecast['localTimestamp'] == local_timestamp:
                    json = forecast

                    self.gifPeriod = json['charts']['period']
                    self.gifPressure = json['charts']['pressure']
                    self.gifSwell = json['charts']['swell']
                    self.gifWind = json['charts']['wind']

                    self.pressure = json['condition']['pressure']
                    self.temperature = json['condition']['temperature']
                    self.temperatureUnits = json['condition']['unit']
                    self.pressure = json['condition']['pressure']
                    self.pressureUnits = json['condition']['unitPressure']
                    self.weather = json['condition']['weather']

                    self.ratingSolidStars = json['solidRating']
                    self.ratingFadedStars = json['fadedRating']

                    self.localTimeStampUNIX = json['localTimestamp']
                    self.localTimeStamp = self.datetime_from_timestamp(self.localTimeStampUNIX)

                    self.primCompass = json['swell']['components']['primary']['compassDirection']
                    self.primDirection = json['swell']['components']['primary']['direction']
                    self.primHeight = json['swell']['components']['primary']['height']
                    self.primPeriod = json['swell']['components']['primary']['period']

                    try:
                        self.secondCompass = json['swell']['components']['secondary']['compassDirection']
                        self.secondDirection = json['swell']['components']['secondary']['direction']
                        self.secondHeight = json['swell']['components']['secondary']['height']
                        self.secondPeriod = json['swell']['components']['secondary']['period']
                    except:
                        pass

                    try:
                        self.tertiartyCompass = json['swell']['components']['tertiary']['compassDirection']
                        self.tertiartyDirection = json['swell']['components']['tertiary']['direction']
                        self.tertiartyHeight = json['swell']['components']['tertiary']['height']
                        self.tertiartyPeriod = json['swell']['components']['tertiary']['period']
                    except:
                        pass

                    self.windChill = json['wind']['chill']
                    self.windCompass = json['wind']['compassDirection']
                    self.windDirection = json['wind']['direction']
                    self.windGusts = json['wind']['gusts']
                    self.windSpeed = json['wind']['speed']
                    self.windUnits = json['wind']['unit']

                    return forecast
            return None
        return json