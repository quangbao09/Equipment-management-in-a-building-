from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class NGUOIDUNG(models.Model):
    tendangnhap = models.CharField(max_length=50, unique=True)
    hoten = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(default='you default value or example@email.com')
    phone = models.CharField(max_length=15, null=True, blank=True)
    ngaysinh = models.DateField(default=timezone.now)
    
    TEN_gioitinh_CHOICES = (
        ('gioitinh1', 'Nam'),
        ('gioitinh2', 'Nữ'),
        ('gioitinh3', 'Khác'),
    )
    gioitinh = models.CharField(max_length=255, choices=TEN_gioitinh_CHOICES, default='gioitinh3')
    diachi = models.CharField(max_length=100, null=True, blank=True)
    ngaycapnhat = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.tendangnhap}"