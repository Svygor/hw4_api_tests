import requests
from jsonschema import validate
import jsonschema

# schema1 = {'type': 'array',
#            'items': {
#                'type': 'object',
#                'properties':
#                    {
#                        'name': {'type': 'string'},
#                        'age': {'type': 'integer'}
#                    }
#            }
#            }
#
# data1 = [{'name': 'Jhon', 'age': 25}]
# data2 = [{'name': 'Sarah', 'age': 'twenty three'}]
# data3 = [{'name': 'Jhon', 'age': 25}, {'name': 'Sarah', 'age': 'twenty three'}]
#
# print(validate(data3, schema1))

schema = {'type': 'array', 'items': {
                'type': 'object',
                'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'brewery_type': {'type': 'string'},
                        'street': {'type': 'string'},
                        'city': {'type': 'string'},
                        'state': {'type': 'string'},
                        'postal_code': {'type': 'string'},
                        'country': {'type': 'string'},
                        'longitude': {'type': 'string'},
                        'latitude': {'type': 'string'},
                        'phone': {'type': 'string'},
                        'website_url': {'type': 'string'},
                        'updated_at': {'type': 'string'},
                        'tag_list': {'type': 'array'}
                }}
          }

data = [{
    'id': "123",
    'name': "Almanac Beer Company",
    'brewery_type': "micro",
    'street': "651B W Tower Ave",
    'city': "Alameda",
    'state': "California",
    'postal_code': "94501-5047",
    'country': "United States",
    'longitude': "-122.306283180899",
    'latitude': "37.7834497667258",
    'phone': "4159326531",
    'website_url': "http://almanacbeer.com",
    'updated_at': "2018-08-23T23:24:11.758Z",
    'tag_list': []
}]

try:
    check = validate(data, schema)
except jsonschema.exceptions.ValidationError as e:
    print("-------------------------------------------------------------")
    print(e)