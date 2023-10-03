import json
json_data = '''
{
  "message": "success",
  "iss_position": {
    "latitude": "41.8157",
    "longitude": "-138.3051"
  },
  "timestamp": 1652700632
}
'''
data = json.loads(json_data)
print(data['iss_position']['longitude'])