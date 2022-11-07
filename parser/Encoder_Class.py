import json
import DataClass

import requests
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

class Encoder:
    def __init__(self):
        self._headers = {"Content-Type":"application/json"}
        self._url = 'http://127.0.0.1:8000/'
        self.Project = ""
    
    def delete_from_database(self,project,folder):
        
        print("Deleting project: ",self._url+folder+project)
        
        response = requests.delete(self._url+folder+project)
        print("Response = ",response.text)
    
    def send_to_database(self,object,folder):
        print("Är i send to database")
        string = json.dumps(object,cls=ComplexEncoder,indent=4)
        
        #print("Postar detta:",self._headers,string)
        #print("Till foldern: ",self._url + folder)
        print(string)
        print("Sending to: " ,self._url+ folder)
        response = requests.post(self._url+ folder,string,headers=self._headers)
        print("response from send",response.text)
        #########