from flask import Flask
from flask import request
import urllib
from flask_restful import Resource, Api, reqparse
import wikipedia
import petfinder
import requests
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
	
class getJson(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('url', type=str)
	   # parser.add_argument('breed', type=str)
	    parser.add_argument('location', type=str)	
            args = parser.parse_args()
	    url= args['url']
	    location = args['location']
	    #breed = args['breed']
            breed = 'Beagle'
            # Download the image from the url
            urllib.urlretrieve(url,"image.png")
            # Search Wikipedia for info
	    search = wikipedia.summary(breed, sentences =5)
            # Instantiate the client with your credentials.
            api = petfinder.PetFinderClient(api_key='90999df88cd81af6e271a7a661ee5bf6', api_secret='57d9d3da742d84021f892c623667db77')
            # search for pets
 	    pet = api.pet_getrandom(animal="dog", location=location,breed=breed, output = "basic")
  	    # Package Info in dict/json object
            data = {}
            data['breed'] = breed
            data['name'] = pet['name']
	    data['shelterId'] = pet['shelterId']
            data['sex'] = pet['sex']
            data['age'] = pet['age']	
            data['size'] = pet['size']     
            data['breed_info'] = search
            data['shelter Contact'] = pet['contact']
            data['photos'] = pet['photos']

         
            return data

        except Exception as e:
            return {'error': str(e)}

api.add_resource(getJson, '/')
	
	
	



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

