request_sqnce =[0,41,30,100,62,51,20]
head = 70
total_seek = 0
for request in [62,51,41,30,20,0]:
  movemnt = abs (request - head)
  total_seek  += movemnt
  print ( head , "=>", request, "=>", movemnt)
  head = request
print ("Total Movement:", total_seek)
for request in [100]:
  movemnt = abs (request - head)
  total_seek  += movemnt
  print ( head , "=>", request, "=>", movemnt)
  head = request
print ("Total Movement:", total_seek)

request_sqnce =[0,41,30,100,62,51,20]
head = 70
total_seek = 0
for request in [100]:
  movemnt = abs (request - head)
  total_seek  += movemnt
  print ( head , "=>", request, "=>", movemnt)
  head = request
print ("Total Movement:", total_seek)
for request in [62,51,41,30,20,0]:
  movemnt = abs (request - head)
  total_seek  += movemnt
  print ( head , "=>", request, "=>", movemnt)
  head = request
print ("Total Movement:", total_seek)