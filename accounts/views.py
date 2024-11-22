from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from accounts.models import profile

# Create your views here.

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get("loginUser")
        password = request.POST.get("loginPassword")

        # Check if email or password fields are empty
        if not email.strip() or not password.strip():
            messages.warning(request, "Please do not leave any field blank.")
            return HttpResponseRedirect(request.path_info)

        # Authenticate the user
        user_obj = authenticate(username=email, password=password)

        # Check if authentication was successful
        if user_obj is None:
            messages.warning(request, "Invalid user credentials.")
            return HttpResponseRedirect(request.path_info)

        # Check if the user's email is verified via the profile
        if not user_obj.profile.is_email_verified:
            messages.warning(request, "Your account is not verified.")
            return HttpResponseRedirect(request.path_info)

        # Log the user in and redirect to the homepage
        login(request, user_obj)
        return redirect("/")

    return render(request, "accounts/login.html")

def RegisterPage(request):
    if request.method=='POST':
        first_name = request.POST.get('First Name')
        last_name  = request.POST.get('Last Name')
        user_name = request.POST.get('User Name')
        email = request.POST.get('Email')
        password = request.POST.get('loginPassword')

        if not first_name.strip() or not last_name.strip() or not user_name.strip() or not email.strip() or not password.strip():
            messages.warning(request,"Do not leave any field blank")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.filter(username = email)
        
        if user_obj.exists():
            messages.warning(request,'User already exist')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name = first_name,last_name = last_name,email = email,username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,f"An email has been send to {email}")
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html')

def logOutUser(request):
    # Log out the user
    logout(request)
    
    # Debug: print the path to ensure it's correct
    print("Redirecting to:", request.path_info)
    
    # Redirect to the same page after logout
    return render(request,'home/landingPage.html')

def activate_account(request,email_token):
    try:
         user = profile.objects.get(email_token = email_token)
         user.is_email_verified=True
         user.save()
         messages.success(request,"Your account has been activated successfully ")
         return render(request,'accounts/login.html')
    except Exception as e:
        return HttpResponse("Invalid token")

