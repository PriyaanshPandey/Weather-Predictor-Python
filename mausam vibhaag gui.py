       #project weather
#importing everything
from tkinter import *
import tkinter.messagebox as tm
from tkinter import filedialog

#geometry
a=Tk()
a.geometry('1024x600')
a.configure(bg='#E9D8B5')
a.title('                                                                                                                                          MAUSAM VIBHAAG ')

#dark mode 

def dark():
    a.configure(bg='#0F172A')
    darkmodebutton1.configure(bg='white',fg='black') 
    darkmodebutton2.configure(bg='green',fg='black')   
def norm():
     a.configure(bg='#E9D8B5')
     darkmodebutton1.configure(bg='green',fg='black') 
     darkmodebutton2.configure(bg='white',fg='black')
def support():
    tm.showinfo('SUPPORT','WE WUD SHORTLY REACH YOU')
def aboutus():
     tm.showinfo('ABOUT US','MADE BY-PRIYAANSH PANDEY')
     
   
#side bar   
f1 = Frame(a,bg='black')
f1.pack(side='left',fill='y')
homelabel=Label(f1,text='HOME     ',borderwidth=5,relief=FLAT,font=('segoe UI',10),bg='black',fg='white')
homelabel.pack()
f2=Frame(a,bg='white')
f2.pack(side='right')
darkmodelabel=Label(f1,text='DARK MODE',borderwidth=5,relief=FLAT,font=('segoe UI',10),bg='black',fg='white')
darkmodelabel.pack()
darkmodebutton1=Button(f1,text='ON',command=dark,bg='green',fg='black')
darkmodebutton1.pack()
darkmodebutton2=Button(f1,text='OFF',command=norm,bg='white',fg='black')
darkmodebutton2.pack()
supportlabel=Label(f1,text='SUPPORT  ',borderwidth=5,relief=FLAT,font=('segoe UI',10),bg='black',fg='white')
supportlabel.pack()
supportbutton=Button(f1,text='📞',command=support)
supportbutton.pack()
aboutuslabel=Label(f1,text='ABOUT US   ',borderwidth=5,relief=FLAT,font=('segoe UI',10),bg='black',fg='white')
aboutuslabel.pack()
aboutusbutton=Button(f1,text='📜',command=aboutus)
aboutusbutton.pack()

#main home
hframe=Frame(a,bg='#4B3832',height='60')
hframe.pack(side='top',fill='x' )
mainlabel=Label(hframe, text='🌦️MAUSAM VIBHAAG  🌦️',borderwidth=5,relief=FLAT,font=('segoe UI',20,'bold'),bg='#4B3832',fg='#FAF3E0',pady=10)
mainlabel.pack()
entryframe=Frame(a)
entryframe.pack(side='top' )
entryvar=StringVar()

from datetime import datetime
now=datetime.now()
c=(now.hour)
index=0
now1=(now.strftime("%I:%M:%p"))

if c in range(0,4):
    
 index==0
elif c in  range(4,7):
 index ==1
elif c in  range(7,10):
 index==2
elif c in  range(10,13):   
 index==3  
elif c in  range(13,16):
 index==4
elif c in  range(16,19): 
 index==5 
elif c in  range(19,22): 
 index==6
else:
 index==7
 
def weatherinfo(a):
    import json

    import requests
    city=a
    b=requests.get(f'https://wttr.in/{city}?format=j1')
    aparsed=b.json()
    data=aparsed
    location=data['nearest_area'][0]
    astro=data['weather'][0]['astronomy'][0]
    current=data['current_condition'][0]
    hour=data['weather'][0]['hourly'][index]
    
   ##address and time
    date=current['localObsDateTime'].split()[0]
    time=now1
    city=city
    country=location['country'][0]['value']
    latitude=location['latitude']
    longitude=location['longitude']
   ##weather information
    temp=hour['tempC']
    feetemp=hour['FeelsLikeC']
    cloud=hour['cloudcover']
    humidity=hour['humidity']
    visibility=hour['visibility']
    precipitation=hour['chanceofrain']
    wind=hour['windspeedKmph']
    description=hour['weatherDesc'][0]['value']
   ##astronomy
    sunrise=astro['sunrise']
    sunset=astro['sunset']
    moonrise=astro['moonrise']
    moonset=astro['moonset']
    mintemp=data['weather'][0]['mintempC']
    maxtemp=data['weather'][0]['maxtempC']   
    d= {'date':date,'time':time,'city':city,'country':country,'latitude':latitude,'longitude':longitude,'temperature':temp,'Feels':feetemp, 'cloud':cloud,'humidity':humidity,'visibility':visibility,'precipitation' : precipitation,'wind':wind,'description' :description,'maxtemp':maxtemp,'mintemp':mintemp, 'sunrise':sunrise,'sunset' : sunset,'moonrise':moonrise,'moonset': moonset  }
    return d

def info(event):
    entrybutton.config(bg='white',fg='black')
    global entry
    if entry !=' ' :
     city=entry.get()
     info=weatherinfo(city)
     print(info)
     label2.config(text= f"{info['date']}")
     label5.config(text= f"{info['time']}")
     label8.config(text= f"{info['city']}")
     label11.config(text= f"{info['country']}")
     label14.config(text= f"{info['latitude']}N")
     label14o.config(text= f"{info['longitude']}E")
     label17.config(text= f"{info['temperature']}C")
     label23.config(text= f"{info['precipitation']}%")
     label29.config(text= f"{info['Feels']}C")
     label38.config(text= f"{info['wind']}kmph")
     label41.config(text= f"{info['maxtemp']}C")
     label50.config(text= f"{info['cloud']}%")
     label53.config(text= f"{info['mintemp']}C")
     label62.config(text= f"{info['description']}")
     label66.config(text= f"{info['sunrise']}")
     label76.config(text= f"{info['moonrise']}")
     label79.config(text= f"{info['sunset']}")
     label88.config(text= f"{info['moonset']}")
    

        

citylabel=Label(entryframe, text='ENTER CITY',font=('segoe UI',15,'bold'),bg='#4B3832',fg='#FAF3E0')
citylabel.pack(side='left')
entry=Entry(entryframe,textvariable=entryvar,font=('segoe UI',15,'bold'),fg='#333',relief=SOLID)
entry.pack(side='left')

entrybutton=Button(entryframe,text='🔎',font=('segoe UI',10,'bold'),bg='#4B3832',fg='#FAF3E0')
entrybutton.pack(side='left')
entrybutton.bind('<Button-1>',info)

sep=Frame(a,height=10,bg='#E9D8B5')
sep.pack(side='top',fill='x')
frame1=Frame(a)
frame1.pack(side='top' )

#ocation
label1=Label(frame1, text='📍 Location 📍',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label1.pack()
sep2=Frame(a,height=10,bg='#E9D8B5')
sep2.pack(side='top',fill='x')
frame2=Frame(a)
frame2.pack(side='top' )
label2=Label(frame2, text='📅DATE-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label2.pack(side='left',anchor='w')
label2=Label(frame2, text='--------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label2.pack(side='left',anchor='w')
label3=Label(frame2, text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label3.pack(side='left',anchor='w')
label4=Label(frame2, text='⏱️ TIME-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label4.pack(side='left',anchor='w')
label5=Label(frame2, text='--------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label5.pack(side='left',anchor='w')
label6=Label(frame2, text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label6.pack(side='left',anchor='w')
label7=Label(frame2, text='🏙️CITY-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label7.pack(side='left',anchor='w')
label8=Label(frame2, text='--------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label8.pack(side='left',anchor='w')
label9=Label(frame2, text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label9.pack(side='left',anchor='w')
label10=Label(frame2, text='🏙️NATION',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label10.pack(side='left',anchor='w')
label11=Label(frame2, text='--------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label11.pack(side='left',anchor='w')
label12=Label(frame2, text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label12.pack(side='left',anchor='w')
frame3=Frame(a)
frame3.pack(side='top' )
label13=Label(frame3 , text='🌏LATITUDE-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label13.pack(side='left',anchor='w')
label14=Label(frame3 , text='------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label14.pack(side='left',anchor='w')
label15=Label(frame3 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label15.pack(side='left',anchor='w')
label16=Label(frame3 , text='🌏LONGITUDE-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label16.pack(side='left',anchor='w')
label14o=Label(frame3 , text='------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label14o.pack(side='left',anchor='w')
label15o=Label(frame3 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label15o.pack(side='left',anchor='w')
#weather
sep4=Frame(a,height=10,bg='#E9D8B5')
sep4.pack(side='top',fill='x')
frame4=Frame(a)
frame4.pack(side='top' )
label15p=Label(frame4 , text='🛰️WEATHER🛰️',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label15p.pack()
sepe2=Frame(a,height=10)
sepe2.pack(side='top')
frame5=Frame(a)
frame5.pack(side='top' )
label16=Label(frame5 , text='🌡️TEMP-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label16.pack(side='left')
label17=Label(frame5 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label17.pack(side='left')
label18=Label(frame5 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label18.pack(side='left',anchor='w')
label19=Label(frame5 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label19.pack(side='left')
label20=Label(frame5 , text='      ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label20.pack(side='left')
label21=Label(frame5 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label21.pack(side='left',anchor='w')
label25=Label(frame5 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label25.pack(side='left')
label26=Label(frame5 , text='      ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label26.pack(side='left')
label27=Label(frame5 , text='                     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label27.pack(side='left',anchor='w')
label22=Label(frame5 , text='☔RAIN-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label22.pack(side='left')
label23=Label(frame5 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label23.pack(side='left')
label24=Label(frame5 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label24.pack(side='left',anchor='w')

frame6=Frame(a)
frame6.pack(side='top' )
label28=Label(frame6 , text='🌡️FEELS-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label28.pack(side='left')
label29=Label(frame6 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label29.pack(side='left')
label30=Label(frame6 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label30.pack(side='left',anchor='w')
label31=Label(frame6 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label31.pack(side='left')
label32=Label(frame6 , text='      ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label32.pack(side='left')
label33=Label(frame6 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label33.pack(side='left',anchor='w')
label34=Label(frame6 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label34.pack(side='left')
label35=Label(frame6 , text='    ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label35.pack(side='left')
label36=Label(frame6 , text='                     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label36.pack(side='left',anchor='w')
label37=Label(frame6 , text='🍃WIND-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label37.pack(side='left')
label38=Label(frame6 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label38.pack(side='left')
label39=Label(frame6 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label39.pack(side='left',anchor='w')

frame7=Frame(a)
frame7.pack(side='top' )
label40=Label(frame7 , text='🌡️MAX-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label40.pack(side='left')
label41=Label(frame7 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label41.pack(side='left')
label42=Label(frame7 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label42.pack(side='left',anchor='w')
label43=Label(frame7 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label43.pack(side='left')
label44=Label(frame7 , text='      ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label44.pack(side='left')
label45=Label(frame7 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label45.pack(side='left',anchor='w')
label46=Label(frame7 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label46.pack(side='left')
label47=Label(frame7 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label47.pack(side='left')
label48=Label(frame7 , text='                     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label48.pack(side='left',anchor='w')
label49=Label(frame7 , text='☁️ CLOUD-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label49.pack(side='left')
label50=Label(frame7 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label50.pack(side='left')
label51=Label(frame7 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label51.pack(side='left',anchor='w')

frame8=Frame(a)
frame8.pack(side='top' )
label52=Label(frame8 , text='🌡️MIN-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label52.pack(side='left')
label53=Label(frame8 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label53.pack(side='left')
label54=Label(frame8 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label54.pack(side='left',anchor='w')
label55=Label(frame8 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label55.pack(side='left')
label56=Label(frame8 , text='      ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label56.pack(side='left')
label57=Label(frame8 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label57.pack(side='left',anchor='w')
label58=Label(frame8 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label58.pack(side='left')
label59=Label(frame8 , text='     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label59.pack(side='left')
label60=Label(frame8 , text='                     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label60.pack(side='left',anchor='w')
label61=Label(frame8 , text='📑-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label61.pack(side='left')
label62=Label(frame8 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label62.pack(side='left')
label63=Label(frame8 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label63.pack(side='left',anchor='w')
sepe=Frame(a,height=10)
sepe.pack(side='top')

frame9=Frame(a)
frame9.pack(side='top')
label65=Label( frame9 , text='🔆SUNRISE-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label65.pack(side='left')
label66=Label(frame9 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label66.pack(side='left')
label67=Label(frame9 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label67.pack(side='left',anchor='w')
label68=Label(frame9 , text='    ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label68.pack(side='left')
label70=Label(frame9 , text='    ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label70.pack(side='left')
label71=Label(frame9 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label71.pack(side='left',anchor='w')
label72=Label(frame9 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label72.pack(side='left')
label73=Label(frame9 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label73.pack(side='left')
label74=Label(frame9 , text='                     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label74.pack(side='left',anchor='w')
label75=Label(frame9 , text='🌙MOONRISE-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label75.pack(side='left')
label76=Label(frame9 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label76.pack(side='left')
label77=Label(frame9 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label77.pack(side='left',anchor='w')

frame10=Frame(a)
frame10.pack(side='top')
label78=Label( frame10 , text='🔆 SUNSET-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label78.pack(side='left')
label79=Label(frame10 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label79.pack(side='left')
label80=Label(frame10, text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label80.pack(side='left',anchor='w')
label81=Label(frame10 , text='    ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label81.pack(side='left')
label82=Label(frame10 , text='    ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label82.pack(side='left')
label83=Label(frame10 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label83.pack(side='left',anchor='w')
label84=Label(frame10 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label84.pack(side='left')
label85=Label(frame10 , text='   ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label85.pack(side='left')
label86=Label(frame10 , text='                     ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label86.pack(side='left',anchor='w')
label87=Label(frame10 , text='🌙MOONSET-',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label87.pack(side='left')
label88=Label(frame10 , text='----------',font=('segoe UI',15,'bold'),bg='#4B3832',fg='pink')
label88.pack(side='left')
label89=Label(frame10 , text='  |  ',font=('segoe UI',15,'bold'),bg='#4B3832',fg='white')
label89.pack(side='left',anchor='w')
sepe1=Frame(a,height=10)
sepe1.pack(side='top')

def download():
    global entry,label17,label29,label41,label53,label23,label50,label62
    path=filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Text files","*.txt")],title='Save Weather Report As',initialfile='weather.txt')
    city=entry.get()
    temp=label17.cget('text')
    fee=label29.cget('text')
    maxt=label41.cget('text')
    mint=label53.cget('text')
    rain=label23.cget('text')
    coud=label50.cget('text')
    desc=label62.cget('text')
    downbutton.config(bg='yellow')
    save_path=path.name
    if save_path:               
       with open(save_path,'a',encoding ="utf-8") as f:
            f.write(f"For {city} the Weather is Reported as- " )
            f.write(f"\nTemperature is- {temp} that feels like- {fee}  ")
            f.write(f"\nMinimum is {mint} and Maximum is {maxt} , With chance of Rain as {rain}")
            f.write(f"\nThe Sky is {coud} Full of cloud and in one word its{desc}  ")
    
frame11=Frame(a)
frame11.pack(side='top')
label90=Label(frame11 , text='DOWNLOAD REPORT',font=('segoe UI',15,'bold'),bg='red',fg='white')
label90.pack(side='left',anchor='w')
label91=Label(frame11 , text='                                           ',font=('segoe UI',15,'bold'),bg='red',fg='white')
label91.pack(side='left',anchor='w')
downbutton=Button(frame11,text='💾',font=('segoe UI',12,'bold'),bg='red',fg='white',command=download)
downbutton.pack(side='left',anchor='w')


   
    

a.mainloop()
