from django.shortcuts import redirect

def is_login(func):
    def method(request,*args,**kwargs):
        if request.session.get('is_login') == 'true':
            return func(request,*args,**kwargs)
        else:
            return redirect('/login/')
    return method

