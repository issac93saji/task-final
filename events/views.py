from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from events.forms import UserForm,UserProfileForm,UserForm2,ContactForm
from events.models import Events,Comments,UserProfile
from django.views import generic



def index(request):
	contactform=ContactForm()

	try:
		fbuser=request.user
		profile=UserProfile.objects.create(user=fbuser)
		profile.save()
	except:
		pass

	events=Events.objects.all()
	if request.user.is_authenticated():
		print("..............................is authrenticated......")
		profile=UserProfile.objects.get(user=request.user)

		return render(request,'events/index.html',{ 'events':events, 'profile':profile,'contactform':contactform })
	else:
		return render(request,'events/index.html',{'events':events,'contactform':contactform})



def DetailView(request,event_id):

	# comment=request.POST.get('comment')
	# event_id=request.POST.get('id')
	# c=Comments(data=comment,uid=request.user,events=event_id)
	# c.save()
	event=Events.objects.get(pk=event_id)
	comments=Comments.objects.filter(events__pk=event_id)
	context_dict={'event':event,'comments':comments}
	return render(request,'events/detail.html',context_dict)

@login_required
def comment(request):
	comment=request.POST.get('comment')
	event=request.POST.get('id')
	event_ob=Events.objects.get(pk=event)
	userid=UserProfile.objects.get(user=request.user)
	c=Comments.objects.create(data=comment)
	c.uid.add(userid)
	c.events.add(event_ob)
	c.save()
	# c=Comments(data=comment,uid=request.user,events=event_ob)
	c.save()
	return redirect(DetailView,event_id=event)
	# return render(request,'events/'+event)


def updateProfile(request):
	updated=False
	if request.method =='POST':
		user_form = UserForm2(data=request.POST)
		if user_form.is_valid() :
			user=request.user
			uprofile=UserProfile.objects.get(user=request.user)
			uname=user.username
			resetuname = user_form['username'].value()
			resetmail=user_form['email'].value()
			resettitle=user_form['title'].value()
			resetpass=user_form['password'].value()
			if 'profile_pic' in request.FILES:
				uprofile.profile_image=request.FILES['profile_pic']

			user=User.objects.get(username=uname)
			user.username=resetuname
			user.email=resetmail
			uprofile.title=resettitle
			user.save()
			uprofile.save();
			user.set_password(resetpass)
			user.save()
			# profile = profile_form.save(commit=False)
			# profile.user = user
			# profile.save()
			updated=True
		else:
			print user_form.errors
	else:
		user=request.user
		uname=user.username
		mail=user.email
		uprofile=UserProfile.objects.get(user=request.user)
		role=uprofile.title
		user_form = UserForm2({'username':uname, 'email':mail,'title':role })

	print("............................................")
	print(updated)
	return render(request,
			'events/update.html',
			{'user_form': user_form, 'updated':updated })



def register(request):
	registered = False
	if request.method == 'POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'profile_image' in request.FILES:
				profile.profile_image = request.FILES['profile_image']
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,
			'events/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'events/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')



def contact(request):
	print(request.POST)
	print(".................................contact view")
	saved=False
	if request.method == 'POST':
		contactform=ContactForm(data=request.POST)
		if contactform.is_valid():
			contactf=contactform.save();
			contactf.save()
			saved=True
			print("................return 1")
			# return render(request,'events/index.html',{'contactsaved':saved})
			return HttpResponse()
		else:
			print("................return 2")
			print contactform.errors

	else:
		contactform=ContactForm()
		print("................return 3")
	return render(request,'events/contact.html',{'contactform':contactform,'contactsaved':saved})