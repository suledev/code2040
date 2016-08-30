import requests

post_data = {'token': '4602c02f21e4b8243cc1d04e08be7161'}
'''POST TOKEN AND RECIEVE CHALLENGE DATA'''
request = requests.post("http://challenge.code2040.org/api/haystack",data=post_data)
haystack_data = request.json()
needle = haystack_data['needle']
haystack = haystack_data['haystack']

'''GO THROUGH EACH LOCATION IN ARRAY, IF NEEDLE IS IN LOCAITON POST NEEDLE
   LOCATION TO SERVER'''
for x in range(len(haystack)):
    if needle == haystack[x]:
        result_data = {'token': '4602c02f21e4b8243cc1d04e08be7161',
                        'needle': x}
        result = requests.post("http://challenge.code2040.org/api/haystack/validate",
                                data=result_data)
        print(result.text)
        break
