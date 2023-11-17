import requests

#gets forecast
def get_forecast(office,gridX,gridY):
    # Construct the API URL for the given latitude and longitude
    url = f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast'

    # Send a GET request to the API URL
    response = requests.get(url)
    # If the response is successful, extract the forecast data
    if response.ok:
        forecast = str(response.json()['properties']['periods'][0]['temperature'])
        # had to move to a different like as part of the below if statement 
        forecast += "F" 
        # ran into a lot of issues with this part as sometimes it popped up as 'null' on the API
        if response.json()['properties']['periods'][0]['temperatureTrend'] != None: 
            forecast += " "+response.json()['properties']['periods'][0]['temperatureTrend']
        
        forecast += " - "+response.json()['properties']['periods'][0]['shortForecast']
        # returning forecast information
        return forecast

    # If the response is not successful, raise an exception
    else:
        raise Exception('Failed to fetch forecast.')

#gets lat and lon from user
def get_points():

    lat = str(input('Please enter latitude: '))
    lon = str(input('Please enter longitude: '))
    
    url2 = f'https://api.weather.gov/points/{lat},{lon}'

    response = requests.get(url2)

    if response.ok:
        office = str(response.json()['properties']['cwa']) # office id
        gridX = int(response.json()['properties']['gridX'])   # latuitude = grid x
        gridY = int(response.json()['properties']['gridY'])   #longitude = grid y
    #if not code successful, raise an exception
    else:
        raise Exception('Failed to fetch office and grid points.')

    return office, gridX, gridY


office, gridX, gridY = get_points()
print(office, gridX, gridY)
forecast = get_forecast(office, gridX, gridY)

print(forecast)
