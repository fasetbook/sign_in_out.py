from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

# login processing
def signin( request):

    userName = request.POST.get('username')
    passWord = request.POST.get('password')

# Use the methods in the Django auth library to verify the username and password
    user = authenticate(username=userName, password=passWord)
    
# If the user can be found and the password is correct
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # Store the user type in the session
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': 'Please log in with an administrator account'})
        else:
            return JsonResponse({'ret': 0, 'msg': 'User has been disabled'})
        
# Otherwise, the username and password are wrong
    else:
        return JsonResponse({'ret': 1, 'msg': 'Username or password is incorrect'})


# logout process
def signout( request):
# use logout method
    logout(request)
    return JsonResponse({'ret': 0})
