def timeandlocation():
  import random
  timelist= ['7:30', '8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30' ]
  loclist = ['Technology Tower', 'Silver Jubilee Tower']
  n=random.randint(0,len(timelist)-1)
  m=random.randint(0,1)
  return timelist[n],loclist[m]

