from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False
    return render(request, 'index.html')

def registration(request):
    reg_errors = User.objects.basic_validator(request.POST)

    if len(reg_errors) > 0:
        for key , value in reg_errors.items():
            messages.error(request, value, extra_tags='reg_error')
        return redirect('/')

    else:
    
        hashed = bcrypt.hashpw(request.POST['reg_password'].encode(), bcrypt.gensalt())
        decoded_hash = hashed.decode()

        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['reg_email'], password=decoded_hash)

        current_user = User.objects.last()
        request.session['current_user_id'] = current_user.id

        request.session['logged_in'] = True

        return redirect('/success')

def login(request):    
    log_errors = User.objects.login_validator(request.POST)

    if len(log_errors) > 0:
        for key , value in log_errors.items():
            messages.error(request, value, extra_tags='login_error')
        return redirect('/')

    else:

        
        logging_in = User.objects.filter(email=request.POST['log_email'])
        if bcrypt.checkpw(request.POST['log_password'].encode(), logging_in[0].password.encode()):
            request.session['current_user_id'] = logging_in[0].id

            request.session['logged_in'] = True

            return redirect('/success')

        else:
            messages.error(request, "Your login info is incorrect!", extra_tags='login_error')
            return redirect('/')

def success(request):
    if request.session['logged_in'] != True:
        return redirect('/')

    else:
        current_user = User.objects.get(id = request.session['current_user_id'])
        context = {
            'current_user': current_user
        }
        return render(request, 'success.html', context)

def faq(request):
    return render(request, 'faq.html')

def logout(request):
    request.session.clear()
    request.session['logged_in'] = False
    return redirect('/')