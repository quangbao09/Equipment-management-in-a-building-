from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class LOAI(models.Model):
    nguoi_dung = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tenloai = models.CharField(max_length=100, default="Chưa xác định tên loại!", unique=True)
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.tenloai}"
    
class PHONG(models.Model):
    nguoi_dung = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tenphong = models.CharField(max_length=100, default="Chưa xác định tên phòng!", unique=True)
    sotang = models.IntegerField(default=0)
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.tenphong}"
    
class NHACUNGCAP(models.Model):
    nguoi_dung = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tennhacungcap = models.CharField(max_length=100, default="Chưa xác định tên nhà cung cấp!", unique=True)
    diachi = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(default='example@emailx.com', null=True, blank=True)
    sodienthoai = models.CharField(max_length=15, null=True, blank=True)
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.tennhacungcap}"
    
class THIETBI(models.Model):
    nguoi_dung = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tenloai = models.ForeignKey(LOAI, on_delete=models.CASCADE)
    tenphong = models.ForeignKey(PHONG, on_delete=models.CASCADE)
    tennhacungcap = models.ForeignKey(NHACUNGCAP, on_delete=models.CASCADE)
    tenthietbi = models.CharField(max_length=100, default="Chưa xác định tên thiết bị!", unique=True)
    giamua = models.IntegerField(default=0)
    ngaythem = models.DateTimeField(auto_now_add=True)
    ngaymua = models.DateTimeField(default=datetime.now())
    ngayhethanbaohanh = models.DateTimeField(default=datetime.now())
    ngaykiemtradinhky = models.DateTimeField(default=datetime.now())
    
    TEN_tinhtrang_CHOICES = (
        ('tinhtrang1', 'Bình thường'),
        ('tinhtrang2', 'Đang hỏng'),
        ('tinhtrang3', 'Đang sửa'),
    )
    tinhtrang = models.CharField(max_length=255, choices=TEN_tinhtrang_CHOICES, default='tinhtrang1')
    mota = models.TextField(default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.tenthietbi}"