from django.shortcuts import render
from .forms import loginForm
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, "login/login.html", {"lF": lF})
    def post(self, request):
        if request.method == 'POST':
            lF = loginForm(request.POST)
            tendangnhap = request.POST["tendangnhap"]
            matkhau = request.POST["matkhau"]
            user = authenticate(request, username = tendangnhap, password = matkhau)
            if user is not None:
                login(request, user)
                thietbi_url = reverse('thietbi:index')
                return redirect(thietbi_url)
            else:
                lF.add_error('tendangnhap', 'Tên đăng nhập hoặc mật khẩu không hợp lệ')
        else:
            form = loginForm()
        return render(request, "login/login.html", {'lF': lF})