import requests

post_data = {'token': '4602c02f21e4b8243cc1d04e08be7161'}
'''POST TOKEN AND RECIEVE CHALLENGE DATA'''
request = requests.post("http://challenge.code2040.org/api/reverse",data=post_data)
word = request.text

'''POST REVERSED WORD USING PYTHON LIST STEP FUNCTIONALITY'''
reverse_data = {'token':'4602c02f21e4b8243cc1d04e08be7161',
                'string': word[::-1]}

result = requests.post("http://challenge.code2040.org/api/reverse/validate",data=reverse_data)

print(result.text)
