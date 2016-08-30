import requests
import datetime


post_data = {'token': '4602c02f21e4b8243cc1d04e08be7161'}

'''POST TOKEN AND RECIEVE CHALLENGE DATA'''
request = requests.post("http://challenge.code2040.org/api/dating",data=post_data)
iso_data = request.json()
iso_string = iso_data['datestamp']
interval = iso_data['interval']

'''PARSE DATE'''
current_date = datetime.datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%SZ')

'''ADD INTERVAL TO PARSED DATE'''
new_date = current_date + datetime.timedelta(seconds=int(interval))
'''FORMAT IN EXPECTED RETURN FORMAT'''
formatted_date = new_date.strftime('%Y-%m-%dT%H:%M:%SZ')

'''POST DATA TO SERVER'''
result_data = {'token': '4602c02f21e4b8243cc1d04e08be7161',
                'datestamp': formatted_date}
result = requests.post("http://challenge.code2040.org/api/dating/validate",
                        json=result_data)
print(result.text)
