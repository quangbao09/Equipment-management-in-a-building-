from django import forms

class loginForm(forms.Form):
    tendangnhap = forms.CharField(max_length=50, label='Tên đăng nhập')
    matkhau = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')