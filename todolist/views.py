from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import UserForm, ServiceForm
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class Index(View):
    def get(self, request):
        return redirect('login')


class Login(View):
    def get(self, reuqest):
        return render(reuqest, 'login.html')
    def post(self, request):
        re_password = request.POST.get('re-password', None)
        if re_password is not None:
            password = request.POST.get('password')
            if password == re_password:
                form = UserForm(request.POST)
                if form.is_valid():
                    form.save()
                    request.session['username'] = request.POST.get('username')
                    return redirect('show')
                message = request.session['message'] = 'Tài khoản đẫ tồn tại'
                return render(request, 'login.html', {'message' : message})
            message = request.session['message'] = 'Mật khẩu không trùng khớp'
            return render(request, 'login.html', {'message' : message})
        
        else:
            username_POST = request.POST.get('username')
            try:
                USER_DB = User.objects.get(username = username_POST)
                password_POST = request.POST.get('password')
                if password_POST == USER_DB.password:
                    request.session['username'] = request.POST.get('username')
                    return redirect('show')
                message = request.session['message'] = 'Mật khẩu không đúng'
                return render(request, 'login.html', {'message' : message})
            except:
                message = request.session['message'] = 'Tên đăng nhập không tồn tại'
                return render(request, 'login.html', {'message' : message})
class Show(View):
    
    def get(self, request):
        global username
        username = request.session.get('username', None)
        if username != None:
            try:
                services = Service.objects.filter(username__username = username)
                context = {
                    'username':username,
                    'services': services,
                }
                
                return render(request, 'show.html', context)
            except Service.DoesNotExist:
                context = {
                    'username':username
                }
                return render(request, 'show.html', context)
        return redirect('login')
    

    def post(self, request):


        username = request.session.get('username', None)
        user = User.objects.get(username = username)
        form = ServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.username = user
            service.save()
            return redirect('show')
        
        messages.error(request, 'Dữ liệu không hợp lệ')
        return redirect('show')


class DeleteItem(View):
    def post(self, request, item_id):
        item = get_object_or_404(Service, id = item_id)
        item.delete()

        return redirect('show')