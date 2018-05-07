"""Returns string "False" or string of good bathing hours for tomorrow from given wunderground api-key and geo-location."""
import requests
import json
import sys
import clipboard
import webbrowser

# call this iOS pythonista script from iOS Workflow with this url
# pythonista://[folder]/[script.py]?action=run&root=icloud&argv=api_key&argv=geolocation

def main():
    """Do the main function."""

    # Definition of good sittuation for bathing
    good_conditions = ['partlysunny', 'partlycloudy', 'mostlysunny', 'mostlycloudy', 'hazy', 'sunny', 'clear']
    good_temp = 20
    good_weekday_hour = [16, 17, 18]
    good_weekend_hour = [11, 12, 13, 14, 15, 16, 17, 18]
    weekend = ['Sunday', 'Saturday']
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Try to get wunderground.com API key from arg 1
    try:
        api_key = sys.argv[1]
        print(f'API-key: {api_key}')
    except (IndexError):
        print('No argument 1 given. (API key for wunderground.com')
    else:
        api_key = sys.argv[1]

    # Try to get geolocation from arg 1
    try:
        geo_loc = sys.argv[2]
        print(f'Geolocation: {geo_loc}')
    except (IndexError):
        print('No argument 2 given. (Geolocation coordinates)')

    # Get weather data
    api_url = f'http://api.wunderground.com/api/{api_key}/hourly10day/q/{geo_loc}.json'
    print(f'Fetching: {api_url}')
    try:
        response = requests.get(api_url)
        parsed_json = json.loads(response.content)
    except Exception as e:
        print(f'API error: {e}')

    # Define today and tomorrow
    thisDay = int(parsed_json['hourly_forecast'][0]['FCTTIME']['yday'])
    nextDay = thisDay + 1

    goodTimes = []
    for hour_forcast in parsed_json['hourly_forecast']:

        conditions = hour_forcast['icon']
        temp_c = int(hour_forcast['temp']['metric'])
        day = hour_forcast['FCTTIME']['weekday_name']
        hour = int(hour_forcast['FCTTIME']['hour'])
        yday = int(hour_forcast['FCTTIME']['yday'])

        if (conditions in good_conditions
            and yday == nextDay 
            and temp_c >= good_temp
            and (
                (day in weekday and hour in good_weekday_hour)
                or (day in weekend and hour in good_weekend_hour)
                )
            ):
            condition_text = f'kl {hour} {conditions} {temp_c}℃'
            goodTimes.append(condition_text)
            print(condition_text)
            
    if(len(goodTimes)):
        clipboard.set('\n'.join(goodTimes))
        print(f'Result: True')
    else:
        clipboard.set('False')
        print(f'Result: False')
    webbrowser.open('workflow://callback')


if __name__ == '__main__':
    main()
