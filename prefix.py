import requests

post_data = {'token': '4602c02f21e4b8243cc1d04e08be7161'}
'''POST TOKEN AND RECIEVE CHALLENGE DATA'''
request = requests.post("http://challenge.code2040.org/api/prefix",data=post_data)
prefix_data = request.json()
prefix = prefix_data['prefix']
array = prefix_data['array']

'''LIST COMPREHENSION CHECKS IF PREFIX IS AT THE BEGINING OF EACH STRING IN ARRAY
   RETURNS ARRAY WITH ONLY STRINGS WITHOUT PREFIX'''
result_array = [string for string in array if string[0:len(prefix)] != prefix]

'''POST DATA TO SERVER'''
result_data = {'token': '4602c02f21e4b8243cc1d04e08be7161',
                'array': result_array}
result = requests.post("http://challenge.code2040.org/api/prefix/validate",
                        json=result_data)
print(result.text)
