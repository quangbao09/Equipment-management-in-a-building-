from django import forms
from .models import LOAI, PHONG, NHACUNGCAP, THIETBI
from django.core.validators import RegexValidator
from register.models import NGUOIDUNG

class formLoai(forms.Form):
    tenloai = forms.CharField(max_length=100, label="Tên loại")
    mota = forms.CharField(widget=forms.Textarea, label="Mô tả", required=False)
    
class formChiTietLoai(forms.ModelForm):
    class Meta:
        model = LOAI
        fields = ['tenloai', "mota"]
        label = {
            'tenloai': 'Tên loại',
            "mota": "Mô tả",
        }
        
class formPhong(forms.Form):
    tenphong = forms.CharField(max_length=100, label="Tên phòng")
    sotang = forms.IntegerField(label="Số tầng")
    mota = forms.CharField(widget=forms.Textarea, label="Mô tả", required=False)
    
class formChiTietPhong(forms.ModelForm):
    class Meta:
        model = PHONG
        fields = ['tenphong', "sotang", "mota"]
        label = {
            'tenphong': 'Tên phong',
            "sotang": "Số tầng",
            "mota": "Mô tả",
        }
    
class formThietbi(forms.ModelForm):
    ngaymua = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ngayhethanbaohanh = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ngaykiemtradinhky = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = THIETBI
        fields = ['tenloai', 'tenphong', 'tennhacungcap', "tenthietbi", "giamua", "ngaymua",
                  "ngayhethanbaohanh", "ngaykiemtradinhky", "tinhtrang", "mota"]
        labels = {
            'tenloai': 'Tên loại',
            "tenphong": "Tên phòng",
            "tennhacungcap": "Tên nhà cung cấp",
            "tenthietbi": "Tên thiết bị",
            "giamua": "Giá mua",
            "ngaymua": "Ngày mua",
            "ngayhethanbaohanh": "Ngày hết hạn bảo hành",
            "ngaykiemtradinhky": "Ngày kiểm tra định kỳ",
            "tinhtrang": "Tình trạng",
            "mota": "Mô tả",
        }
        
class formChiTietNhaCungCap(forms.ModelForm):
    class Meta:
        model = NHACUNGCAP
        fields = ['tennhacungcap', "diachi", "email", "sodienthoai", "mota"]
        label = {
            'tennhacungcap': 'Tên nhà cung cấp',
            "diachi": "Địa chỉ",
            "email": "Email",
            "sodienthoai": "SĐT",
            "mota": "Mô tả",
        }
        
class formNhaCungCap(forms.Form):
    tennhacungcap= forms.CharField(max_length=100, label="Tên nhà cung cấp")
    diachi = forms.CharField(max_length=100, label="Địa chỉ", required=False)
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput)
    sodienthoai = forms.CharField(max_length=15, label="SĐT", required=False)
    mota = forms.CharField(widget=forms.Textarea, label="Mô tả", required=False)
    
class formChiTietNguoiDung(forms.ModelForm):
    ngaysinh = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Validator cho trường phone, chỉ cho phép nhập 10 số
    phone_validator = RegexValidator(regex=r'^\d{10}$', message='Phone phải chứa đúng 10 chữ số.')
    
    # Áp dụng validator vào trường phone
    phone = forms.CharField(max_length=10, label="SĐT", validators=[phone_validator])
    
    class Meta:
        model = NGUOIDUNG
        fields = ['hoten', "email", "phone", "ngaysinh", "gioitinh", "diachi"]
        labels = {
            'hoten': 'Họ tên',
            "email": "Email",
            "phone": "SĐT",
            "ngaysinh": "Ngày sinh",
            "gioitinh": "Giới tính",
            "diachi": "Địa chỉ",
        }

class formLocThietBiTheoGia(forms.Form):
    x = forms.IntegerField(label='X')
    y = forms.IntegerField(label='Y')