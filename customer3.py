import requests
url = "http://localhost:9696/approve"
cus3= {
        'gender': "b", 
        'age':33.17,
        'debt' :1.04, 
        'married' : "u", 
        'bankcustomer': "g", 
        'educationlevel': "r",
        'ethnicity': "h", 
        'yearsemployed':6.5 , 
        'priordefault': "t", 
        'employed': "f", 
        'creditscore': 0,
       'driverslicense': "t", 
       'citizen': "g", 
       'zipcode': "00164", 
       'income': 31285}
print(requests.post(url, json=cus3).json())