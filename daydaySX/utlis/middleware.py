class My_middle(object):
    url_list = ['/login/','/register/','/logout/']

    def process_view(self,request,view_func,*args,**kwargs):
        if request.path not in My_middle.url_list and not request.is_ajax():
            request.session['path'] = request.path