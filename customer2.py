import requests
url = "http://localhost:9696/approve"
cus2 = {
        'gender': "b", 
        'age':42.50 ,
        'debt' :4.915, 
        'married' : "y", 
        'bankcustomer': "p", 
        'educationlevel': "w",
        'ethnicity': "v", 
        'yearsemployed':3.165 , 
        'priordefault': "t", 
        'employed': "f", 
        'creditscore': 0,
       'driverslicense': "t", 
       'citizen': "g", 
       'zipcode': "00052", 
       'income': 1442}
print(requests.post(url, json=cus2).json())