import requests
url = "http://localhost:9696/approve"
cus1 = {
        'gender': "a", 
        'age':22.92 ,
        'debt' :11.585, 
        'married' : "u", 
        'bankcustomer': "g", 
        'educationlevel': "cc",
        'ethnicity': "v", 
        'yearsemployed':0.04 , 
        'priordefault': "t", 
        'employed': "f", 
        'creditscore': 0,
       'driverslicense': "f", 
       'citizen': "g", 
       'zipcode': "00080", 
       'income': 134}
print(requests.post(url, json=cus1).json())