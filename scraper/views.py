from django.shortcuts import render, redirect
from .models import Blogs
from bs4 import BeautifulSoup
import requests
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Class-based Views
from django.contrib.auth.decorators import login_required




def Scraper(request):
	return render(request, 'scraper/scraper.html')


# add try and accept block
# becuz when no internet then page crash 
# to handle the crash use try and except 
# and the show message that pls check you internet connection ! 
@login_required
def BlogList(request):
	src = 'https://www.dataquest.io/blog/'
	source = requests.get(src).text
	soup = BeautifulSoup(source, 'lxml')

	count = 0

	headings = []
	summaries = []
	categories = []
	links = []

	data_set = []
	
	for article in soup.find('div', class_='bSeCont').find('section', class_='bSe left').find_all('article'):
		heading = article.find('div', class_='awr').find('h2', class_='entry-title').text
		headings.append(heading)
		

		summary = article.find('div', class_='awr').find('p').text
		summaries.append(summary)
		

		category = article.find('div', class_='awr').find('div', class_='category').text.strip()
		categories.append(category)
	

		link = article.find('div', class_='awr').find('div', class_='category').find('span').find('a')['href']
		links.append(link)
		
		data_set.append(headings)
		data_set.append(summaries)
		data_set.append(categories)
		data_set.append(links)

		count += 1 

	context = {
		'headings' : headings, 
		'summaries' : summaries,
		'categories' : categories,
		'links' : links,
		'data_set' : data_set
	}
		
	return render(request, 'scraper/bloglist.html', context)






