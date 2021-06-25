import datetime
import pytz


def getSub():
  IST = pytz.timezone('Asia/Kolkata')
  now = datetime.datetime.now(IST)
  day = now.strftime("%A")
  hr = float(now.strftime("%H"))
  sub = "Aaj chhutti hai bhay"
  if day == "Monday":
   if hr in (10,11) : sub = "Physics"
   if hr in (11,12) : sub = "Computer"
   if hr in (12,13) : sub = "Maths"
   if hr in (14,15) : sub = "Comm Skills"
   if hr in (15,16) : sub = "Ecology"
   if hr in (16,17) : sub = "Chemistry"
   if hr in (17,18) : sub = "Computer"
   else: sub = "Abhi lunch break hai bhay"

  elif day == "Tuesday":
   if hr in (10,11) : sub = "Physics"
   if hr in (11,12) : sub = "Maths"
   if hr in (14,15) : sub = "English"
   if hr in (15, 16, 17, 18) : sub = "Engineering Graphics"
   else: sub = "Abhi lunch break hai bhay"
   
  elif day == "Wednesday":
   if hr in (10,11) : sub = "Comm Skills"
   if hr in (11,12) : sub = "Chemistry"
   if hr in (12,13) : sub = "Maths"
   if hr in (14,15) : sub = "Physics"
   if hr in (15,16) : sub = "Chemistry"
   if hr in (16,17) : sub = "Maths"
   if hr in (17,18) : sub = "Computer"
   else: sub = "Abhi lunch break hai bhay"
   
  elif day == "Thursday":
   if hr in (9, 10, 11, 12) : sub = "Chemistry"
   if hr in (14,15) : sub = "Ecology"
   if hr in (15,16) : sub = "Physics"
   if hr in (16,17) : sub = "Chemistry"
   else: sub = "Abhi lunch break hai bhay"

   
  elif day == "Friday":
   if hr in (14, 16, 17) : sub = "Computer"
   if hr in (17,18) : sub = "Physics"

  else: sub = "Abhi lunch break hai bhay"

  return(sub)

    
