from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.Company
print('Enter Username :')
user=input()
print('Enter your password')
pas=input()

result = db.Users.find( { 'Username':user,'Password':pas } )
if result.count() > 0:  
  print('your are ok')
else:
    print('you are not ok')
