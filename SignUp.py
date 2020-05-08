
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.Company
print('Enter the Username that you want')
user=input()
print('Enter your password')
pas=input()
l=len(pas)


posts=db.Users
post_data={'Username':user,'Password':pas}
result=posts.insert_one(post_data)
print('Successfly inserted: {0}'.format(result.inserted_id))
