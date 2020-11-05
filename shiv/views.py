from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# from .forms import PostForm
from .filters import ProjectFilter

from .models import Project

# Create your views here.

def home(request):
	projects = Project.objects.filter(active=True, featured=True)[0:3]

	context = {'projects':projects}
	return render(request, 'base/index.html', context)

def projects(request):
	projects = Project.objects.filter(active=True)
	myFilter = ProjectFilter(request.GET, queryset=projects)
	projects = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(projects, 9)

	try:
		projects = paginator.page(page)
	except PageNotAnInteger:
		projects = paginator.page(1)
	except EmptyPage:
		projects = paginator.page(paginator.num_pages)

	context = {'projects':projects, 'myFilter':myFilter}
	return render(request, 'base/projects.html', context)


def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['shiv71290@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'base/email_sent.html')