import requests
#r = requests.get('https://api.github.com/events')
r = requests.get('https://1st-lab.vladimirplisko.repl.co/?tz=Europe/Moscow')

r1 = requests.post('https://1st-lab.vladimirplisko.repl.co/', data = {'dt_sel':'{"date":"12.20.2021 22:21:05", "tz":"EST"}','tz_snd':'Europe/Moscow'})
