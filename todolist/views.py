from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import UserForm, ServiceForm
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, ServiceSerializerModel, UserSerializerModel



class Index(View):
    def get(self, request):
        return render(request, 'home.html')


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
    


def context_response_error(message):
    return {
        'status':False,
        'message':message
    }

def context_response_success(message):
    return {
        'status':True,
        'data':message
    }

class UserAPI(APIView):
    def post(self, request):
        data_global = request.data

        if data_global['type'] == 'get_service':
            data = UserSerializer(data=data_global)

            if data.is_valid():
                username = data.data['username']
                password = data.data['password']

                try:
                    user = User.objects.get(username=username)

                    if user.password == password:
                        services_user = Service.objects.filter(username__username = username)
                        serializer = ServiceSerializerModel(services_user, many=True)
                        return Response(context_response_success(serializer.data), status=status.HTTP_200_OK)
                    else:
                        return Response(context_response_error('Incorrect Infomation'), status=status.HTTP_400_BAD_REQUEST)
                except User.DoesNotExist:
                    return Response(context_response_error('User does not exits'), status=status.HTTP_400_BAD_REQUEST)
            return Response(context_response_error('Type error'), status=status.HTTP_400_BAD_REQUEST)
        
        elif data_global['type'] == 'create_acc':

            data = UserSerializerModel(data=data_global)

            if not data.is_valid():
                return Response(context_response_error('Account do exist'), status=status.HTTP_400_BAD_REQUEST)
            
            username = data.data['username']
            password = data.data['password']

            User.objects.create(username= username, password=password)
            return Response(context_response_success('Create Account Success!'), status=status.HTTP_200_OK)
    

class ServiceAPI(APIView):
    def post(self, request):

        data_r = request.data

        if data_r['type'] == 'add_service':

            data_user = {
                'username':data_r['username'],
                'password':data_r['password']
            }

            data_service = {
                'title':data_r['title'],
                'time':data_r['time']
            }

            check_user = UserSerializer(data=data_user)
            check_service = ServiceSerializerModel(data=data_service)

            if not (check_user.is_valid() and check_service.is_valid()):
                return Response(context_response_error('type error'), status=status.HTTP_400_BAD_REQUEST)
            
            username = data_user['username']
            password = data_user['password']
            
            title = data_service['title']
            time = data_service['time']


            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    Service.objects.create(username= user,  title=title, time=time)
                    return Response(context_response_success(f'Create Service for [{username}] Success!'), status=status.HTTP_200_OK)
                else:
                    return Response(context_response_error('Incorrect iformation Account!'), status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response(context_response_error('User does not exits'), status=status.HTTP_400_BAD_REQUEST)
            

        elif data_r['type'] == 'del_service':


            data_user = {
                'username':data_r['username'],
                'password':data_r['password']
            }

            data_service = {
                'title':data_r['title'],
                'time':'2023-07-25T08:31:15Z'
            }

            check_user = UserSerializer(data=data_user)
            check_service = ServiceSerializerModel(data=data_service)

            if not (check_user.is_valid() and check_service.is_valid()):
                return Response(context_response_error('type error'), status=status.HTTP_400_BAD_REQUEST)
            
            username = data_user['username']
            password = data_user['password']
            
            title = data_service['title']

            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    try:
                        service = Service.objects.get(title=title)
                        
                        service.delete()
                    
                    except Service.DoesNotExist:return Response(context_response_error(f'Not Found Service [{title}] in [{username}]'), status=status.HTTP_400_BAD_REQUEST)
                    return Response(context_response_success(f'Deleta Service with title=[{title}] of [{username}] Success!'), status=status.HTTP_200_OK)
                else:
                    return Response(context_response_error('Incorrect iformation Account!'), status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response(context_response_error('User does not exits'), status=status.HTTP_400_BAD_REQUEST)