from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.


def register(request):
      is_valid = True 
      if request.method =='POST':
          first_name = request.POST['first_name'];
          last_name = request.POST['last_name'];
          username = request.POST['username'];
          password1 = request.POST['password1'];
          password2 = request.POST['password2'];
          email = request.POST['email'];
          if password1!=password2:
              is_valid = False
              mistake = ["password is not matching",True]
          if User.objects.filter(username=username).exists():
              is_valid = False
              mistake = ["Username is already taken",True]
          if User.objects.filter(email=email).exists():
              is_valid = False
              mistake = ["Email is already taken",True]
          if is_valid:    
              user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
              user.save()
              return redirect('/')
          else:
              return render(request,'register.html',{'mistake':mistake})
      else:
        return render(request,'register.html')
         
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            mistake = ["Invalid Credentials",True]
            return render(request,'login.html',{'mistake':mistake})


    else:
        return render(request,'login.html')



def profile(request):
     return render(request,'profile.html')

def logout(request):
    auth.logout(request)
    return redirect('/')