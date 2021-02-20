from django.shortcuts import render
import justext
from django.shortcuts import render
from .models import DATA
from collections import Counter
# from rest_framework.response import Response
import urllib
import requests
from six.moves.urllib.request import urlopen
import requests
import justext
# from htmldate import find_date
# from nltk.corpus import stopwords
import json
import ast 
from bs4 import BeautifulSoup
import re

def index(request):
    if request.method =='POST':
        url=request.POST.get('name', '')
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        urls = ''
        str1='https://www.eventbrite.com/d/online'
        str2='https://www.eventbrite.com/e/','https://www.eventbrite.com.au/e/','https://www.eventbrite.co.uk/e/','https://www.eventbrite.ca/e'
        str3='https://www.eventbrite.ca/e'
        str4='Technologies','Engineering', 'Computer Engineering','Civil Engineering','Mechanical Engineering','Electronics Engineering','Electrical Engineering','Doctors','Obstetrics','Gynaecology','Dentistry','Internal Medicines','Paediatrics','General Medicine (MBBS)','Sports','Basketball','Cricket','Hockey','Table Tennis','Badminton','Artists','Photography','Music','Painting','Dancing','Theatre and Film','Writing','Hip Hop Dancing','Salsa Dancing','Zumba','Classical Dancing','Activism','Social Activism','Political Activism','Animal Welfare','Environment Activism','Lawn Tennis','Fitness','Gym','Running','Cycling','Yoga','Wrestling','Kizomba Dancing','Food and Nutrition','Bollywood','Belly Dancing','Football','Golf','Skating','Blockchain & Cryptocurrency','Travelling','Lawyer','Leisure','Trekking & Hiking','Business','Startup','Code Development','QA & testing','DevOps','Designing','Parenting','UI Designing','Graphic Designing','Meditation','Self Healing','Computer Networking','Party','Cyber Security','Dermatology','Neurology','Ophthalmology','Psychiatry','Toxicology','Baseball','Volleyball','Rugby','Boxing','Motorsports','Cardiology','Orthopaedic','Endocrinology','Oncology','Anesthesia','Gardening','Infertility''Immigration','Makeup Artist','MBA','Human Resource','Finance','Marketing','Leadership','Financial Planning','Management','Containers','Accounts','Physics','Chemistry','Economics','Literature','Chartered Accountant','Linguistic and Languages','English Learning','Spanish Learning','Beer','Marijuana','Real Estate','Emerging Technologies','Data Analytics','Mental Peace','Sketching','Russian Language','German Language','Business Strategy','Wine','Linux','Business Networking','Artificial Intelligence','Game Developing','Internet Of Things','Aeronautical Engineering','Chemical Engineering','Fashion','Flight Attendant','Pilot','Robotic Engineering','Poetry','Philosophy','Architecture','Rowing','Virtual Reality','Biochemistry','Religion','Spirituality','Agriculture','Book Reading','History','Space','Pharmacy','Education','Entrance Exam','Musical Instrument','Lifestyle','Maths','French Language','Student','Chess','Guitar','Tabla','Piano','Violin','Flute','Drum','Saxophone','Keyboard','Harmonium','Mythology','Market Analysis','LGBT','Class 11','Class 10','Class 12','Teacher','Festival','Beauty','IIT JEE','Archaeology','Civilisation','Astronomy','Cooking','Trading','Movie Watching','Archery','Bowling','Curling','Karate','Weight Lifting','Shooting','Ballet','Kathak','Aerial','Tango','Cancan','Magic','Horse Riding','Self Defence','Swimming','Product Reviews','Massage','Mass media and Journalism','Dating','Database Administrator','Machine Learning','Personal Development','Career Counselling','Gaming','Construction','Urban Planning','Structural Engineering','Transportation Engineering','Geotechnical Engineering','Industrial Automation Engineering','Nanotechnology Engineering','Mechatronics Engineering','Industrial Engineering','Robotics Engineering','Pottery','Politics','Gender Issue','Humanity','DJ','Digital Marketing','Volunteering','Venture Capital','Hotel Management','Adventure','Bungee Jumping','Sky Diving','Ocean Diving','Canoeing','Camping','Inventors','Anthropology','Fine Arts','Freeflying','Scuba Diving','Wind Surfing','Homeless','mountain biking','Music Producers','Performing and visual arts','Operations','Driving','R&D','Evolution','ITI','Affiliate Marketing','Content Marketing','Email Marketing','Pay per Click Advertising','Search Engine Marketing','Social media marketing','ATG_INTERNAL'
        urls1 = []
        for link in soup.find_all('a'):
            try:
                da=link.get('href')
                if str1 in da:
                    if da== 'https://www.eventbrite.com/d/online/events/':
                        pass
                    
                    else:
                        reqs1 = requests.get(da)
                        soup = BeautifulSoup(reqs1.text, 'html.parser')
                        for link in soup.find_all('a'):
                            try:
                                data=link.get('href')
                                for j in str2:
                                    if j in data :
                                        html = urlopen(data)
                                        bs = BeautifulSoup(html, 'html.parser')
                                        images = bs.find_all('picture', {'content':re.compile('')})
                                        i=0
                                        for image in images:
                                            if i==0:
                                                img=image['content']+'\n'
                                                i=i+1
                                            else:
                                                pass
                                        reqs2= requests.get(data)
                                        soup=BeautifulSoup(reqs2.text, 'html.parser')
                                        for link in soup.find_all('title'):
                                            title=link.get_text()
                                            # print(title)
                                            for j in str4:
                                                if j in title:
                                                    ata=DATA(title=title,
                                                            img=img,
                                                            int_grp=j)
                                                    try:
                                                        DATA.objects.get(title=title)
                                                        pass
                                                    except:
                                                        ata.save()
                                                        print("DATA SAVE")
                                                        print("TITLE:",title)
                                                        print("IMAGE:",img)
                                                        print("INTERSETED GROUP:",j)
                                                                                                                    
                            except:
                                pass

            except:
                pass
        return render(request, 'index.html')

    return render(request, 'index.html')