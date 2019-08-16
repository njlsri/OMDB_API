import requests
import json
import sys

try:
   try:
       movie = str(sys.argv[1])
   except:
       raise Exception('Please provide movie name as an argument')
   params = (('t', movie),('apikey', 'fab1fac7'),)
   response = requests.get('http://www.omdbapi.com/', params=params, verify=False)
   values=None
   responsedata = str(response.text)
   res_json = json.loads(responsedata)
   try:   
    movie_name = (res_json['Title'])
   except:
    movie_name = movie
   if res_json['Response']== 'True':
     for i in range(len(res_json['Ratings'])):
        if res_json['Ratings'][i]['Source']=='Rotten Tomatoes':
         values=res_json['Ratings'][i]['Value']
         break
     if values is None and res_json['Response']== 'True':
        print('Movie name: '+movie_name)
        print('No Rating Found in Rotten Tomatoes.')
     else:
        print('Movie name: '+movie_name)
        print( "Rotten Tomatoes Rating is {}. ".format(values))

   elif res_json['Response']== 'False':
    print(response.text)

   else:
       print('Please Provide Movie Name.')

except Exception as err:
    print("Error : %s",str(err) )
    pass
	
