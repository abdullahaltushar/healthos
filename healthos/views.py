
from django.shortcuts import redirect, render
import random
import math

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from codes.forms import CodeForm
from codes.models import Code
from user.models import CustomUser
from django.contrib import messages
from Plan.models import Plan
from Company.models import Company
from payment.models import Payment
from datetime import date

from twilio.rest import Client

def registration(request):
    if request.method == 'POST':
        first_name=request.POST.get('first')
        last_name=request.POST.get('last')
        phone_number = request.POST.get('phone')
        password=request.POST.get('password')
        email=request.POST.get('email')
        username=email.split('@')[0]
        company = Company.objects.get(id=request.POST.get('company'))
        plan = Plan.objects.get(name=request.POST.get('plan'))
        customer = CustomUser.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,password=password,username=username,email=email, company=company, plan=plan)
        #save data customer model
        customer.save()
        #create session
        request.session['username']=username

        #code makeing
        digits = [i for i in range(0, 10)]
        random_str = ""
        for i in range(6):
            index = math.floor(random.random() * 10)
            random_str += str(digits[index])
        #end code

        #check usercode exist or not
        value=Code.objects.filter(user=username)
        # if exist
        if value!=None:
            #create code existing user
            value=Code.objects.filter(number=phone_number).create(number=random_str)
            value.save()
            #verify user
            return redirect("verify_user")
        else:
            # else crate new code new user
            value=Code.objects.create(user=username,number=random_str)
            value.save()

            #verify user
            return redirect("verify_user")
    else:
        #next database value resgister html page 
        companies = Company.objects.filter(active=True).all()
        plans = Plan.objects.all()
        return render(request, 'registration.html', {'companies': companies, 'plans': plans})

#home page       
@login_required
def home_view(request):
    username=request.session.get('username')
    user=CustomUser.objects.get(username=username)
    pk=user.pk
    data=Payment.objects.get(username=pk)
    package=data.package
    #here mantain the pack activite
    if(data.package=="Globalnet Gold"):
        context={
            'data':package,
        }

    elif(data.package=="Globalnet Silver"):
        context={
            'data':package,
        }
    else:
        context={
            'data':package,
        }
    return render(request, 'main.html',context)

#login page
def auth_view(request):
    form=AuthenticationForm()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
         #check user is valid or not
        if user is not None:
            # if valid create session
            request.session['pk']=user.pk
            request.session['username']=user.username
            # and send payment checking method
            return redirect('payment_chcek')
    return render(request,'auth.html',{'form':form})

def verify_user(request):
    form=CodeForm(request.POST or None)
    # get username
    username=request.session.get('username')
    # check user data exist
    if username:
        #get user form code
        user=Code.objects.get(username=username)
        code=user.number
        code_user=f"{user.user}:{user.number}"
        if not request.POST:
            #send sms
            print(user.number)

        if form.is_valid():
            num=form.cleaned_data.get('number')
            otp=user.number
            # Send the OTP via SMS using Twilio
            account_sid = 'your sid'
            auth_token = 'your token'
            client = Client(account_sid, auth_token)
            message = client.messages \
                            .create(
                                body="Your OTP is: " + otp,
                                from_='+8801313406617',
                                to=num
                            )
            # Save the OTP in session for later verification
            request.session['otp'] = otp
            messages.success(request, 'OTP sent to ' + num)

            # match otp
            if str(code)==num:
                value=CustomUser.objects.get(username=username)
                # active user
                value.active=True
                value.save()
                login(request, user)
                #send login page
                return redirect('auth_view')

            else:
                return redirect('auth_view')
    return render(request,'verify.html',{'form':form})

def Company1(request):
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        email=request.POST.get("email")
        password=request.POST.get("password")
        phone_number=request.POST.get("phone")
        website=request.POST.get("website")
        username=email.split('@')[0]
        print(username)

        data=Company.objects.create(name=name,address=address,email=email,username=username,phone_number=phone_number,password=password,website=website)
        data.save()
        request.session['username']=username
       #code makeing
        digits = [i for i in range(0, 10)]
        random_str = ""
        for i in range(5):
            index = math.floor(random.random() * 10)
            random_str += str(digits[index])

        value=Code.objects.filter(phone=phone_number).values()
        if value.exists():
            value = Code.objects.get(phone=phone_number)
            value.number=random_str
            value.save()
            print("error")
            return redirect('verify_company')
        else:
            value=Code.objects.create(user=username,number=random_str,phone=phone_number)
            value.save()
            print("eroor")
            return redirect("verify_company")
    return render(request, 'company.html')

def verify_company(request):
    form=CodeForm(request.POST or None)
    username=request.session.get('username')
    if username:
        user=Code.objects.get(user=username)
        code=user.number
        code_user=f"{user.user}:{user.number}"
        if not request.POST:
            #send sms
            print(user.number)

        if form.is_valid():
            num=form.cleaned_data.get('number')
            otp=user.number
            # Send the OTP via SMS using Twilio
            account_sid = 'your sid'
            auth_token = 'your token'
            client = Client(account_sid, auth_token)
            message = client.messages \
                            .create(
                                body="Your OTP is: " + otp,
                                from_='+8801313406617',
                                to=num
                            )
            # Save the OTP in session for later verification
            request.session['otp'] = otp
            messages.success(request, 'OTP sent to ' + num)

            if str(code)==num:
                value=Company.objects.get(username=username)
                value.active=True
                value.save()
                login(request, user)
                return redirect('auth_view')

            else:
                return redirect('auth_view')
    return render(request,'verify.html',{'form':form})


def payment_chcek(request):
    #get username 
    username=request.session.get('username')
    #get user id
    user=CustomUser.objects.get(username=username)
    pk=user.pk
    # check user id is exist
    data=Payment.objects.filter(username=pk)
    # get current date
    current_date=date.today()
    # check data is exits
    if(data.exists()):
        #get payment data use existing user
        data=Payment.objects.get(username=pk)
        # check expire year 
        if(data.expire_year>current_date):
            # check expire date
            if(data.expire_date>current_date):
                #all condition valid go home page
                return redirect('home_view')
            else:
                # otherwise send message
                messages("your time is expire! Please Recharger First")
        else:
            # otherwise send message
            messages("your Package time is expire! Please Change Package")
    else:
        # otherwise go registation page
        return redirect('registration')

    

