from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import PageURL

# Create your views here.
def index(request):
	if request.method == 'POST' : 


		result = shorten_url(request)
		
#
		context = {
			'title' : 'Home',
			'new_url' : result,
			'old_url' : request.POST.get('old_url'),
		}

#		query = PageURL(url=request.POST.get('old_url'), short_url=result)
#		if query.save() :
#			context['error'] = 'Successfully save the record'
#		else :

#			context['error'] = 'Failed to save record'

		return render(request, 'pages/index.html', context)		

#		return HttpResponse("Record NOT Save")

	else :

		context = {
			'title' : 'Home',
		}

		return render(request, 'pages/index.html', context)

def shorten_url(request) :
	curl = request.POST.get('old_url')

	data = {
		"secret" : "sf0d7GUaqogM3A8I5DvOqLcon5h4oodH",
		"hashes" : "512",
		"url" : curl,
	}

	response = requests.post("https://api.coinhive.com/link/create", data)
	print("Old URL: ",request.POST.get('old_url'))
	print("Shorten URL response : ", response.json()['url'])
	return response.json()['url']