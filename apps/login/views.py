from django.shortcuts import render, redirect
from .models import User
from apps.Checkout.models import *
from .forms import *
from django.contrib import messages
import bcrypt

def index(request):
    current_user = User.objects.get(id = request.session['current_user_id'])

    if 'logged_in' not in request.session:
        request.session['logged_in'] = False

    context={
        'logged_in': request.session['logged_in'],
        'current_user': current_user
    }
    
    return render(request, 'index.html', context)

def registration(request):
    reg_errors = User.objects.basic_validator(request.POST)

    if len(reg_errors) > 0:
        for key , value in reg_errors.items():
            messages.error(request, value, extra_tags='reg_error')
        return redirect('/')

    else:
    
        hashed = bcrypt.hashpw(request.POST['reg_password'].encode(), bcrypt.gensalt())
        decoded_hash = hashed.decode()

        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], user_name=request.POST['user_name'], email=request.POST['reg_email'], password=decoded_hash)

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

            return redirect('/')

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

    context={
        'logged_in': request.session['logged_in'],
    }

    return render(request, 'faq.html', context)

def pic_upload(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        user = User.objects.get(id = request.session['current_user_id'])
        user.profile_pic = request.FILES['profile_pic']
        user.save()
        return redirect('/bio')
    else:
        #error message about empty field
        return redirect('/profile')

def new_profile(request):
    form = DocumentForm()
    current_user = User.objects.get(id = request.session['current_user_id'])
    context = {
        'current_user': current_user,
        'form': form
    }
    return render(request, 'new_profile.html',context)

# def create_profile(request):
#     user = User.objects.get(id = request.session['current_user_id'])

#     user.bio = request.POST['bio']
#     user.save()

#     Shipping.objects.create(first_name = request.POST['shipping_first_name'], last_name = request.POST['shipping_last_name'], address = request.POST['shipping_address'], city = request.POST['shipping_city'], zipcode = request.POST['shipping_zip'], state = request.POST['shipping_state'], user =  user)

#     Billing.objects.create(first_name = request.POST['billing_first_name'], last_name = request.POST['billing_first_name'], address = request.POST['billing_first_name'], city = request.POST['billing_first_name'], zipcode = request.POST['billing_first_name'], state = request.POST['billing_first_name'], user = user )

#     form = DocumentForm(request.POST, request.FILES)
#     if form.is_valid():
#         user = User.objects.get(id = request.session['current_user_id'])
#         user.profile_pic = request.FILES['profile_pic']
#         user.save()

#     return redirect('/profile')

def bio(request):
    if request.session['logged_in'] != True:
        return redirect('/')
    return render(request, 'bio.html')

def bio_submit(request):
    print('*' * 50)
    print('submit bio reached')
    user = User.objects.get(id = request.session['current_user_id'])
    user.bio = request.POST['bio']
    user.save()
    return redirect('/shipping')

def shipping(request):
    if request.session['logged_in'] != True:
        return redirect('/')
    return render(request, 'shipping.html')

def shipping_submit(request):
    reg_errors = Shipping.objects.form_validator(request.POST)
    if len(reg_errors) > 0:
        for key , value in reg_errors.items():
            messages.error(request, value, extra_tags='reg_error')
        return redirect('/shipping')
    else:
        user = User.objects.get(id = request.session['current_user_id'])

        Shipping.objects.create(first_name = request.POST['shipping_first_name'], last_name = request.POST['shipping_last_name'], address = request.POST['shipping_address'], city = request.POST['shipping_city'], zipcode = request.POST['shipping_zip'], state = request.POST['shipping_state'], user =  user)
        return redirect('/billing')

def billing(request):
        if request.session['logged_in'] != True:
            return redirect('/')
        return render(request, 'billing.html')

def billing_submit(request):
    reg_errors = Billing.objects.bill_validator(request.POST)
    if len(reg_errors) > 0:
        for key , value in reg_errors.items():
            messages.error(request, value, extra_tags='reg_error')
        return redirect('/billing')
    else:
        user = User.objects.get(id = request.session['current_user_id'])
        Billing.objects.create(first_name = request.POST['billing_first_name'], last_name = request.POST['billing_last_name'], address = request.POST['billing_address'], city = request.POST['billing_city'], zipcode = request.POST['billing_zip'], state = request.POST['billing_state'], phone_number = request.POST['billing_phone'], user = user )
        return redirect('/profile')

def profile(request):
    if request.session['logged_in'] != True:
        return redirect('/')

    current_user = User.objects.get(id = request.session['current_user_id'])
    print('-'*50)
    print(current_user.first_name)
    context = {
        'current_user': current_user,
        'logged_in': request.session['logged_in']
    }
    return render(request, 'profile.html', context)

def to_profile(request):
    user = User.objects.get(id = request.session['current_user_id'])

    if request.session['logged_in'] != True:
        messages.info(request, "Please login or register")
        return redirect('/')
        
    if user.bio:
        return redirect('/profile')

    else:
        return redirect("/new_profile")
    

def about(request):
    context={
        'logged_in': request.session['logged_in'],
    }
    return render(request, "about.html", context)


def contact(request):
    context={
        'logged_in': request.session['logged_in'],
    }
    return render(request, "contact.html", context)

def hiw(request):
    context={
        'logged_in': request.session['logged_in'],
    }
    return render(request, "hiw.html", context)


def logout(request):
    # request.session.clear()
    request.session['logged_in'] = False
    return redirect('/')