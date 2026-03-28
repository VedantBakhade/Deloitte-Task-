import json
from datetime import datetime

def convertFromFormat1(jsonObject):
    loc = jsonObject['location'].split('/')
    return {
        'deviceID': jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        'location': {
            'country': loc[0], 'city': loc[1], 'area': loc[2], 
            'factory': loc[3], 'section': loc[4]
        },
        'data': {
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp']
        }
    }

def convertFromFormat2(jsonObject):
    # This handles the ISO timestamp conversion to milliseconds
    dt_str = jsonObject['timestamp'].replace('Z', '+00:00')
    dt = datetime.fromisoformat(dt_str)
    ts_ms = int(dt.timestamp() * 1000)
    return {
        'deviceID': jsonObject['device']['id'],
        'deviceType': jsonObject['device']['type'],
        'timestamp': ts_ms,
        'location': {
            'country': jsonObject['country'], 'city': jsonObject['city'], 
            'area': jsonObject['area'], 'factory': jsonObject['factory'], 
            'section': jsonObject['section']
        },
        'data': jsonObject['data']
    }

def main(jsonObject):
    if jsonObject.get('device') is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)
      
