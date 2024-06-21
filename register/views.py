from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerForm
from .models import NGUOIDUNG
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, "register/register.html", {'form': rF})
    def post(self, request):
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                tendangnhap = form.cleaned_data['tendangnhap']
                email = form.cleaned_data['email']
                matkhau = form.cleaned_data['matkhau']
                if User.objects.filter(username=tendangnhap).exists():
                    form.add_error('tendangnhap', 'Tên đăng nhập đã tồn tại')
                else:
                    user = User.objects.create_user(tendangnhap, email, matkhau)
                    user.save()
                    nguoidung = NGUOIDUNG(tendangnhap=tendangnhap, email=email)
                    nguoidung.save()
                    messages.info(request, 'Đăng ký thành công')
        else:
            form = registerForm()
        return render(request, "register/register.html", {'form': form})