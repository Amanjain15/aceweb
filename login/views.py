from django.shortcuts import render
from .models import login_data
import jwt
import random 
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth import authenticate, login,logout
from django.core.mail import EmailMessage,get_connection
from custom_key.models import *
from django.core.mail.backends.smtp import EmailBackend
from internal_key.models import *
from student.models import *
from faculty.models import *
from alumni.models import *

class UploadFileForm(forms.Form):
    file = forms.FileField()

#Group_id distributions
# 1 - student
# 2 - faculty
# 3 - alumni
# 4 - admin
# 5 - developer
@login_required
@csrf_exempt
def import_login_table(request):
	if request.user.is_authenticated():
		user=str(request.user)
		try:
			login_data_row=login_data.objects.get(login_id=str(user))
			if login_data_row.group_id==5:
			    if request.method == "POST":
			    	print "27"
			        form = UploadFileForm(request.POST,request.FILES)
			        if form.is_valid():
			        	print "30"
			        	request.FILES['file'].save_to_database(model=login_data,mapdict=['login_id','group_id'])
			        	return HttpResponse("OK")
			        else:
			            return HttpResponseBadRequest()
			    else:
			        form = UploadFileForm()
			        return render(request,'upload.html',{'form':form})
		except:
			return HttpResponse("Page not found")
	else:
		return HttpResponse("page not found")


def email_verification(request,value):
	try:
		print value
		jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
		print jwt_key
		email_decoded_json=jwt.decode(value,jwt_key,algorithms =['HS256'])
		print email_decoded_json
		email=email_decoded_json['email']
		roll_no=email_decoded_json['roll_no']
		# otp=jwt.decode(otp,'secret',algorithms=['HS256'])
		print email
		print roll_no
		# print otp
		try:
			login_data_row=login_data.objects.get(email=email)
			group_id=login_data_row.group_id
			setattr(login_data_row,'email_flag',True)
			login_data_row.save()
			if group_id==1:
				return HttpResponse("student signup")
			else:
				if group_id==2:
					return HttpResponse("faculty signup")
				else:
					if group_id==3:
						return HttpResponse("alumni signup")
					else:
						return HttpResponse("ok")
		except:
			return HttpResponse("email_id and otp not get")
	except:
		return HttpResponse("Failed")

# http://127.0.0.1:8000/verify_email?email=arpitj938@gmail.com&otp=123456

def login_view(request):
	if request.user.is_authenticated():
		return render(request,'main.html',{'logout':'logout'})
	else:
		if request.method=='POST':
			login_id=str(request.POST.get('login_id'))
			password=str(request.POST.get('password'))
			# password=jwt.decode(password,'secret',algorithms=['HS256'])
			try:
				login_data_row=login_data.objects.get(login_id=login_id)
				print login_id
				if login_data_row.password==password:
					if login_data_row.email_flag==1:
						user = authenticate(username=login_id, password=password)
						if user is not None:
							login(request, user)
							print 'login done'
							return HttpResponseRedirect("/welcome/")
						else:
							return render(request,'main.html',{'login_status':'wrong login_id or password'})
					else:
						return render(request,'main.html',{'login_status':'complete your email verification'})
				else:
					return render(request,'main.html',{'login_status':'wrong login_id or password'})
			except:
				return render(request,'main.html',{'login_status':'wrong login_id or password'})
		else:
			return render(request,'main.html')

@csrf_exempt
def signup_view(request):
	if request.user.is_authenticated():
		return render(request,'welcome.html')
	else:
		if request.method=='POST':
			try:
				print "try"
				# roll_no='151258'
				roll_no=str(request.POST.get('roll_no'))
				print roll_no
				# name='arpit'
				name=str(request.POST.get('name'))
				print name
				mobile=str(request.POST.get('mobile'))
				email=str(request.POST.get('email'))
				# email='arpitj938@gmail.com'
				print email
				try:
					print "try 1"
					login_data_row=login_data.objects.get(login_id=roll_no)
					group_id=login_data_row.group_id
					print group_id
					if login_data_row.email_flag==True:
						print 'your account is registered already'
						# return HttpResponse("your account is registered already")
						return render(request,"signup.html",{'msg':'your account is registered already'})	
					else:
						print roll_no
						if group_id==1:
							try:
								student_data_row=student_data.objects.get(roll_no=roll_no)
								setattr(student_data_row,'name',str(name))
								setattr(student_data_row,'mobile',str(mobile))
								setattr(student_data_row,'email',str(email))
								student_data_row.save()
							except:
								student_data.objects.create(roll_no=roll_no,name=name,email=email,mobile=mobile)
								print '148'
						else:
							if group_id==2:
								try:
									faculty_data_row=faculty_data.objects.get(faculty_id=roll_no)
									setattr(faculty_data_row,'name',str(name))
									setattr(faculty_data_row,'mobile',str(mobile))
									setattr(faculty_data_row,'email',str(email))
									faculty_data_row.save()
								except:
									faculty_data.objects.create(faculty_id=roll_no,name=name,email=email,mobile=mobile)
							else:
								if group_id==3:
									try:
										alumni_data_row=alumni_data.objects.get(roll_no=roll_no)
										setattr(alumni_data_row,'name',str(name))
										setattr(alumni_data_row,'mobile',str(mobile))
										setattr(alumni_data_row,'email',str(email))
										alumni_data_row.save()
									except:
										alumni_data.objects.create(roll_no=roll_no,name=name,email=email,mobile=mobile)
						setattr(login_data_row,'email',str(email))
						login_data_row.save()
						print '160'
						host_email=str(custom_keys_data.objects.get(key='host').value)
						port_email=custom_keys_data.objects.get(key='port').value
						username_email=str(custom_keys_data.objects.get(key='username').value)
						password_email=str(custom_keys_data.objects.get(key='password').value)
						print host_email
						email_json={'email':str(email),
						'roll_no':str(roll_no)}
						jwt_key=str(internal_key_data.objects.get(key='jwt_key').value)
						email_encoded_url=jwt.encode(email_json,jwt_key,algorithm='HS256')
						print email_encoded_url
						link=str(request.scheme+"://"+request.get_host()+"/verify_email/"+email_encoded_url)
						url='<a href='+link+'>verify email</a>'
						image='<img src='+'"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTEgRR_jTgKgGkHyVYFbXHg51pzhpWmx1bsgREGMcV621HdH39q"'+'>'
						print url
						# email_body=str(custom_keys_data.objects.get(key='email_test').value)
						email_body=str(email_send_data.objects.get(key='email_verify').email_data)
						print email_body % (image,name,url)
						backend = EmailBackend(host=str(host_email), port=int(port_email), username=str(username_email), 
			                       password=str(password_email), use_tls=True, fail_silently=True)
						EmailMsg=EmailMessage("ACE",email_body % (image,name,url) ,'no-reply@gmail.com',[email] ,connection=backend)
						EmailMsg.content_subtype = "html"
						EmailMsg.send()
						return HttpResponse("done")
				except:
					print 'enroll_no is not valid'
					return render(request,"signup.html",{'msg':'enroll_no is not valid'})
			except:
				print 'enroll_no not get'
				return render(request,"signup.html",{'msg':'enroll_no not get'})
		else:
			return render(request,"signup.html")