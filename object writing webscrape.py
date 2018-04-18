#! python3
# Object Writing - Using Task Sheduler, after 10am(and random interval)
#                 open up text file with Dictionary.com Word Of The
#                 Day, and timer for creative writing. Text me a reminder

import requests, bs4, os, subprocess, webbrowser, textme, time, random

# Change directory to writing folder
os.chdir(r'D:\DOCUMENTS\Songs\Object writing')

# Request URL for dictionary.com word of the day
url = 'http://www.dictionary.com/wordoftheday/'
res = requests.get(url)
res.raise_for_status()

# Find word of the day in html
soup = bs4.BeautifulSoup(res.text, 'html.parser')
word = soup.find('strong').text

# Create text file with word of the day file-name, and word at top of text file
file = open(word + '.txt', 'a')
file.write(word + '\n\n')
file.close()

# Text me for reminder
textme.textme('Time to write!')

# After text, wait 15 - 30 seconds, then open text file, website for word definition, then timer
time.sleep(15)
subprocess.Popen(['C:\\Program Files (x86)\\Notepad++\\notepad++.exe', f'{word}.txt'])
webbrowser.open('http://www.dictionary.com/wordoftheday/')
webbrowser.open('https://www.online-stopwatch.com/timer/10minutes/')
