import requests
import json



sfile= open('somefile.wav', "rb")
 
 
response = requests.post("https://stream.watsonplatform.net/speech-to-text/api/v1/recognize",
         auth=("YOUR_ID", "YOUR_PASSWORD"),
         headers = {"content-type": "audio/wav"},
         data=sfile
         )
 
print json.loads(response.text)

