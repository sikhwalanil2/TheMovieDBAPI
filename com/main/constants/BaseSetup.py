import json

import requests
from com.main.constants.Endpoints import EndPoints

class BaseSetup:

    BASE_URL = "https://api.themoviedb.org"
    version = "/3"

    def constructUrl(self,endPoint,api_key):
        url =  self.BASE_URL+self.version+endPoint+"?api_key="+api_key
        print("Hitting this api:",url)
        return  url;

    def get_request(self,endPoint,apikey):
        return  requests.request("GET",self.constructUrl(endPoint,apikey))
        # return requests.get(self.constructUrl(endPoint,apikey))

    def post_request(self,endpoint,body,apikey,guestSessionId,headers):
        url = self.constructUrl(endpoint,apikey)+"&guest_session_id="+guestSessionId
        print(url)
        return requests.post(url, data=json.dumps(body), headers=headers)


    def commonRequest(self,method,url,params,data):
        return requests.request(method,url,params,data)

    def getRatedMovies(self,apiKey):
        return self.get_request(EndPoints.getTopRatedMovies, apiKey)

    def postRateMovie(self,movieId, body,apiKey,guestSessionId):
        headers = {
            'Content-Type': 'application/json'
        }
        return  self.post_request(EndPoints.rateMovie.format(movieId),body,apiKey,guestSessionId,headers=headers)

    def getNewGuestSessionId(self,apiKey):
        return self.get_request(EndPoints.guestSessionKey,apiKey)


