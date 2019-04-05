import Classes.forecast as forecast
from datetime import datetime, timedelta
import pprint

model = forecast.forecast(1004)

spot_id = 1004
forecastHourIntervals = []
numDays = 2
numHours = 24*numDays
for xhours in range(0,numHours,3):
    forecastHourIntervals.append(datetime.now() + timedelta(hours=xhours))


images = []
for tempDateTime in forecastHourIntervals:
    tempForecast = model.get_forecast(spot_id , model.units, tempDateTime)
    imgSwellURL = tempForecast['charts']['swell']

pprint.pprint(tempForecast)