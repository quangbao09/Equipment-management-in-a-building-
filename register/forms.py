from django import forms

class registerForm(forms.Form):
    tendangnhap = forms.CharField(max_length=50, label='Tên đăng nhập')
    email = forms.EmailField()
    matkhau = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')
    nhaplaimatkhau = forms.CharField(widget=forms.PasswordInput, label='Nhập lại mật khẩu')
    
    def clean(self):
        cleaned_data = super().clean()
        matkhau = cleaned_data.get('matkhau')
        nhaplaimatkhau = cleaned_data.get('nhaplaimatkhau')
        if matkhau and nhaplaimatkhau and matkhau != nhaplaimatkhau:
            raise forms.ValidationError("Mật khẩu không khớp")