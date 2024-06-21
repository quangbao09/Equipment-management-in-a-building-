from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import formLoai, formPhong,formThietbi, formNhaCungCap, formChiTietLoai, formChiTietPhong, formChiTietNhaCungCap, formChiTietNguoiDung, formLocThietBiTheoGia
from django.views import View
from .models import LOAI, PHONG, NHACUNGCAP, THIETBI
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth import logout
from register.models import NGUOIDUNG
from datetime import datetime, date
from django.http import JsonResponse
from django.db import models
from django.db.models import Sum
import re
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    nguoi_dung = request.user
    thietbi_list = THIETBI.objects.filter(nguoi_dung=nguoi_dung)
    return render(request, "thietbi/thietbi.html", {"thietbi_list": thietbi_list})
                
@login_required(login_url='/login/')
def loai(request):
    nguoi_dung = request.user
    loai_list = LOAI.objects.filter(nguoi_dung=nguoi_dung)
    return render(request, "thietbi/loai.html", {"loai_list": loai_list})

@login_required(login_url='/login/')
def phong(request):
    nguoi_dung = request.user
    phong_list = PHONG.objects.filter(nguoi_dung=nguoi_dung)
    return render(request, "thietbi/phong.html", {"phong_list": phong_list})

@login_required(login_url='/login/')
def nhacungcap(request):
    nguoi_dung = request.user
    nhacungcap_list = NHACUNGCAP.objects.filter(nguoi_dung=nguoi_dung)
    return render(request, "thietbi/nhacungcap.html", {"nhacungcap_list": nhacungcap_list})

@login_required(login_url='/login/') 
def getThietBiTheoLoai(request, id):
    thietbi_list = THIETBI.objects.filter(tenloai=id)
    loai = LOAI.objects.get(id = id)
    return render(request, "thietbi/thietbi_loai.html", {"thietbi_list": thietbi_list, "loai": loai})
    
@login_required(login_url='/login/') 
def getThietBiTheoPhong(request, id):
    thietbi_list = THIETBI.objects.filter(tenphong=id)
    phong = PHONG.objects.get(id = id)
    return render(request, "thietbi/thietbi_phong.html", {"thietbi_list": thietbi_list, "phong": phong})

@login_required(login_url='/login/') 
def getThietBiTheoNhaCungCap(request, id):
    thietbi_list = THIETBI.objects.filter(tennhacungcap=id)
    nhacungcap = NHACUNGCAP.objects.get(id = id)
    return render(request, "thietbi/thietbi_nhacungcap.html", {"thietbi_list": thietbi_list, "nhacungcap": nhacungcap})
    
class themthietbi(LoginRequiredMixin, View):
    login_url='/login/'
    
    def get(self, request):
        fL = formThietbi()
        context = {"fL": fL}
        return render(request, "thietbi/themthietbi.html", context)
    
    def post(self, request):
        if request.method == "POST":
            fL = formThietbi(request.POST)
            if fL.is_valid():
                nguoi_dung = request.user
                tenloai = fL.cleaned_data["tenloai"]
                tenphong = fL.cleaned_data["tenphong"]
                tennhacungcap = fL.cleaned_data["tennhacungcap"]
                tenthietbi = fL.cleaned_data["tenthietbi"]
                giamua = fL.cleaned_data["giamua"]
                ngaymua = fL.cleaned_data["ngaymua"]
                ngayhethanbaohanh = fL.cleaned_data["ngayhethanbaohanh"]
                ngaykiemtradinhky = fL.cleaned_data["ngaykiemtradinhky"]
                tinhtrang = fL.cleaned_data["tinhtrang"]
                mota = fL.cleaned_data["mota"]
                
                if giamua < 0:  # Kiểm tra giá nhập không âm
                    fL.add_error('giamua', 'Giá nhập không được âm')
                elif ngayhethanbaohanh < ngaymua:  # Kiểm tra ngày hết hạn bảo hành không được hết hạn trước ngày mua
                    fL.add_error('ngayhethanbaohanh', 'Ngày hết hạn bảo hành không được hết hạn trước ngày mua')
                else:
                    if THIETBI.objects.filter(tenthietbi=tenthietbi).exists():
                        fL.add_error('tenthietbi', 'Tên thiết bị đã tồn tại')
                    else:
                        savefL = THIETBI(nguoi_dung=nguoi_dung, tenloai=tenloai, tenphong=tenphong, tennhacungcap=tennhacungcap, 
                                         tenthietbi=tenthietbi, giamua=giamua, ngaymua=ngaymua, ngayhethanbaohanh=ngayhethanbaohanh, 
                                         ngaykiemtradinhky=ngaykiemtradinhky, tinhtrang=tinhtrang, mota=mota)
                        savefL.save()
                        messages.info(request, 'Thêm thành công')
        else:
            fL = formThietbi()
        
        return render(request, "thietbi/themthietbi.html", {'fL': fL})


class themloai(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self, request):
        fL = formLoai
        context = {"fL": fL}
        return render(request, "thietbi/themloai.html", context)
    
    def post(self, request):
        if request.method == "POST":
            fL = formLoai(request.POST)
            if fL.is_valid():
                nguoi_dung = request.user
                tenloai = fL.cleaned_data["tenloai"]
                mota = fL.cleaned_data["mota"]
                if LOAI.objects.filter(tenloai=tenloai).exists():
                    fL.add_error('tenloai', 'Tên loại đã tồn tại')
                else:
                    savefL = LOAI(nguoi_dung=nguoi_dung, tenloai=tenloai, mota=mota)
                    savefL.save()
                    messages.info(request, 'Thêm thành công')
        else:
            fL = formLoai()
        return render(request, "thietbi/themloai.html", {'fL': fL})

class themphong(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self, request):
        fL = formPhong
        context = {"fL": fL}
        return render(request, "thietbi/themphong.html", context)
    
    def post(self, request):
        if request.method == "POST":
            fL = formPhong(request.POST)
            if fL.is_valid():
                nguoi_dung = request.user
                tenphong = fL.cleaned_data["tenphong"]
                sotang = fL.cleaned_data["sotang"]
                mota = fL.cleaned_data["mota"]
                if sotang < 0:  # Kiểm tra số tầng không âm
                    fL.add_error('sotang', 'Số tầng không được âm')
                elif PHONG.objects.filter(tenphong=tenphong).exists():
                    fL.add_error('tenphong', 'Tên phòng đã tồn tại')
                else:
                    savefL = PHONG(nguoi_dung=nguoi_dung, tenphong=tenphong, sotang=sotang, mota=mota)
                    savefL.save()
                    messages.info(request, 'Thêm thành công')
        else:
            fL = formPhong()
        return render(request, "thietbi/themphong.html", {'fL': fL})

    


class themnhacungcap(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self, request):
        fL = formNhaCungCap
        context = {"fL": fL}
        return render(request, "thietbi/themnhacungcap.html", context)
    
    def post(self, request):
        if request.method == "POST":
            fL = formNhaCungCap(request.POST)
            if fL.is_valid():
                nguoi_dung = request.user
                tennhacungcap = fL.cleaned_data["tennhacungcap"]
                diachi = fL.cleaned_data["diachi"]
                email = fL.cleaned_data["email"]
                sodienthoai = fL.cleaned_data["sodienthoai"]
                mota = fL.cleaned_data["mota"]
                
                # Kiểm tra số điện thoại có đúng định dạng hay không
                if not re.match(r'^\d{10,11}$', sodienthoai):
                    fL.add_error('sodienthoai', 'Số điện thoại không hợp lệ')
                elif NHACUNGCAP.objects.filter(tennhacungcap=tennhacungcap, diachi=diachi, email=email, sodienthoai=sodienthoai).exists():
                    fL.add_error('tennhacungcap', 'Tên nhà cung cấp đã tồn tại')
                else:
                    savefL = NHACUNGCAP(nguoi_dung=nguoi_dung, tennhacungcap=tennhacungcap, diachi=diachi, email=email, sodienthoai=sodienthoai, mota=mota)
                    savefL.save()
                    messages.info(request, 'Thêm thành công')
        else:
            fL = formNhaCungCap()
        return render(request, "thietbi/themnhacungcap.html", {'fL': fL})

@login_required(login_url='/login/') 
def xoathietbi(request, id):
    thietbi = THIETBI.objects.get(id=id)
    thietbi.delete()
    return redirect("thietbi:index")

@login_required(login_url='/login/') 
def xoaloai(request, id):
    loai = LOAI.objects.get(id=id)
    loai.delete()
    return redirect("thietbi:loai")

@login_required(login_url='/login/') 
def xoaphong(request, id):
    phong = PHONG.objects.get(id=id)
    phong.delete()
    return redirect("thietbi:phong")

@login_required(login_url='/login/') 
def xoanhacungcap(request, id):
    nhacungcap = NHACUNGCAP.objects.get(id=id)
    nhacungcap.delete()
    return redirect("thietbi:nhacungcap")

class chitietthietbi(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, id):
        thietbi = THIETBI.objects.get(id=id)
        form = formThietbi(instance=thietbi)
        return render(request, "thietbi/chitietthietbi.html", {"thietbi": thietbi, "form": form})
    
    def post(self, request, id):
        if 'xoa' in request.POST:
            try:
                thietbi = THIETBI.objects.get(id=id)
                thietbi.delete()
                messages.success(request, 'Xóa thiết bị thành công.')
                return redirect('thietbi:index')
            except THIETBI.DoesNotExist:
                messages.error(request, 'Thiết bị không tồn tại.')
                return redirect('thietbi:index')
        else:
            if request.method == "POST":
                thietbi = THIETBI.objects.get(id=id)
                form = formThietbi(request.POST, instance=thietbi)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Lưu thành công.')
                    return redirect('thietbi:chitietthietbi', id=thietbi.id)
            else:
                thietbi = THIETBI.objects.get(id=id)
                form = formThietbi(instance=thietbi)
            return render(request, "thietbi/chitietthietbi.html", {'form': form, 'thietbi': thietbi})
        
class chitietloai(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, id):
        loai = LOAI.objects.get(id=id)
        form = formChiTietLoai(instance=loai)
        return render(request, "thietbi/chitietloai.html", {"loai": loai, "form": form})
    
    def post(self, request, id):
        if 'xoa' in request.POST:
            try:
                loai = LOAI.objects.get(id=id)
                loai.delete()
                messages.success(request, 'Xóa loại thành công.')
                return redirect('thietbi:loai')
            except LOAI.DoesNotExist:
                messages.error(request, 'Loại không tồn tại.')
                return redirect('thietbi:loai')
        else:
            if request.method == "POST":
                loai = LOAI.objects.get(id=id)
                form = formChiTietLoai(request.POST, instance=loai)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Lưu thành công.')
                    return redirect('thietbi:chitietloai', id=loai.id)
            else:
                loai = LOAI.objects.get(id=id)
                form = formChiTietLoai(instance=loai)
            return render(request, "thietbi/chitietloai.html", {'form': form, 'loai': loai})
        
class chitietphong(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, id):
        phong = PHONG.objects.get(id=id)
        form = formChiTietPhong(instance=phong)
        return render(request, "thietbi/chitietphong.html", {"phong": phong, "form": form})
    
    def post(self, request, id):
        if 'xoa' in request.POST:
            try:
                phong = PHONG.objects.get(id=id)
                phong.delete()
                messages.success(request, 'Xóa phòng thành công.')
                return redirect('thietbi:phong')
            except PHONG.DoesNotExist:
                messages.error(request, 'Phòng không tồn tại.')
                return redirect('thietbi:phong')
        else:
            if request.method == "POST":
                phong = PHONG.objects.get(id=id)
                form = formChiTietPhong(request.POST, instance=phong)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Lưu thành công.')
                    return redirect('thietbi:chitietphong', id=phong.id)
            else:
                phong = PHONG.objects.get(id=id)
                form = formChiTietPhong(instance=phong)
            return render(request, "thietbi/chitietphong.html", {'form': form, 'phong': phong})
        
class chitietnhacungcap(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, id):
        nhacungcap= NHACUNGCAP.objects.get(id=id)
        form = formChiTietNhaCungCap(instance=nhacungcap)
        return render(request, "thietbi/chitietnhacungcap.html", {"nhacungcap": nhacungcap, "form": form})
    
    def post(self, request, id):
        if 'xoa' in request.POST:
            try:
                nhacungcap = NHACUNGCAP.objects.get(id=id)
                nhacungcap.delete()
                messages.success(request, 'Xóa nhà cung cấp thành công.')
                return redirect('thietbi:nhacungcap')
            except NHACUNGCAP.DoesNotExist:
                messages.error(request, 'Nhà cung cấp không tồn tại.')
                return redirect('thietbi:nhacungcap')
        else:
            if request.method == "POST":
                nhacungcap = NHACUNGCAP.objects.get(id=id)
                form = formChiTietNhaCungCap(request.POST, instance=nhacungcap)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Lưu thành công.')
                    return redirect('thietbi:chitietnhacungcap', id=nhacungcap.id)
            else:
                nhacungcap = NHACUNGCAP.objects.get(id=id)
                form = formChiTietNhaCungCap(instance=nhacungcap)
            return render(request, "thietbi/chitietnhacungcap.html", {'form': form, 'nhacungcap': nhacungcap})

@login_required(login_url='/login/') 
def searchthietbi(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = THIETBI.objects.filter(
            Q(id__icontains=query) |
            Q(tenthietbi__icontains=query) |
            Q(tenloai__tenloai__icontains=query) |
            Q(tenphong__tenphong__icontains=query) |
            Q(tennhacungcap__tennhacungcap__icontains=query) |
            Q(tinhtrang=query)
        )

    context = {'results': results}
    return render(request, 'thietbi/searchthietbi.html', context)

@login_required(login_url='/login/') 
def sortthietbi(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by')
    sort_order = request.GET.get('sort_order')
    thietbi_list = THIETBI.objects.all()

    if query:
        thietbi_list = thietbi_list.filter(tenthietbi__icontains=query)
    if sort_by:
        if sort_order == 'desc':
            thietbi_list = thietbi_list.order_by(f'-{sort_by}')
        else:
            thietbi_list = thietbi_list.order_by(sort_by)
            
    context = {
        'thietbi_list': thietbi_list,
    }
    return render(request, 'thietbi/sortthietbi.html', context)

@login_required(login_url='/login/') 
def dangxuat(request):
    logout(request)
    return redirect("login:loginUser")

class chitietnguoidung(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        user = request.user
        nguoidung = NGUOIDUNG.objects.get(tendangnhap=user.username)
        form = formChiTietNguoiDung(instance=nguoidung)
        return render(request, "thietbi/chitietnguoidung.html", {"nguoidung": nguoidung, "form": form})
    
    def post(self, request):
        if request.method == "POST":
            user = request.user
            nguoidung = NGUOIDUNG.objects.get(tendangnhap=user.username)
            form = formChiTietNguoiDung(request.POST, instance=nguoidung)
            if form.is_valid():
                form.save()
                messages.success(request, 'Lưu thành công.')
                return redirect('thietbi:chitietnguoidung')
        else:
            user = request.user
            nguoidung = NGUOIDUNG.objects.get(tendangnhap=user.username)
            form = formChiTietNguoiDung(instance=nguoidung)
        return render(request, "thietbi/chitietnguoidung.html", {'form': form, 'nguoidung': nguoidung})

   
@login_required(login_url='/login/')     
def locThietBiTheoGia(request):
    if request.method == 'GET':
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        # Kiểm tra xem min_price và max_price không rỗng và không âm
        if min_price and max_price and min_price.isdigit() and max_price.isdigit() and float(min_price) >= 0 and float(max_price) >= 0:
            min_price = float(min_price)
            max_price = float(max_price)
            # Kiểm tra xem min_price không lớn hơn max_price
            if min_price <= max_price:
                condition = Q(giamua__gte=min_price) & Q(giamua__lte=max_price)
            else:
                # Nếu min_price lớn hơn max_price, không áp dụng bộ lọc và trả về trang không có kết quả
                thietbi_list = []
                context = {'thietbi_list': thietbi_list}
                return render(request, 'thietbi/locthietbitheogia.html', context)
        else:
            # Nếu một trong hai giá trị không hợp lệ hoặc cả hai đều rỗng, không áp dụng bộ lọc và trả về trang không có kết quả
            thietbi_list = []
            context = {'thietbi_list': thietbi_list}
            return render(request, 'thietbi/locthietbitheogia.html', context)

        # Áp dụng bộ lọc
        thietbi_list = THIETBI.objects.filter(condition)
        context = {'thietbi_list': thietbi_list}
    else:
        # Trường hợp người dùng không gửi yêu cầu GET, không áp dụng bộ lọc
        thietbi_list = []
        context = {'thietbi_list': thietbi_list}

    return render(request, 'thietbi/locthietbitheogia.html', context)




    
@login_required(login_url='/login/')     
def locThietBiTheoBaoHanh(request):
    if request.method == 'GET':
        expiration = request.GET.get('expiration')
        if expiration == 'conhan':
            thietbi_list2 = THIETBI.objects.filter(ngayhethanbaohanh__gte=date.today())
        elif expiration == 'hethan':
            thietbi_list2 = THIETBI.objects.filter(ngayhethanbaohanh__lt=date.today())
        else:
            thietbi_list2 = THIETBI.objects.all()

        context = {'thietbi_list2': thietbi_list2}
        return render(request, 'thietbi/locthietbitheogia.html', context)

def dash_data(request):
    category = request.GET.get('category', 'loai')
    data = []

    if category == 'loai':
        categories = LOAI.objects.all()
        for cat in categories:
            total_value = THIETBI.objects.filter(tenloai=cat).aggregate(total=models.Sum('giamua'))['total']
            data.append({'category': cat.tenloai, 'total_value': total_value})
    elif category == 'phong':
        categories = PHONG.objects.all()
        for cat in categories:
            total_value = THIETBI.objects.filter(tenphong=cat).aggregate(total=models.Sum('giamua'))['total']
            data.append({'category': cat.tenphong, 'total_value': total_value})
    elif category == 'nhacungcap':
        categories = NHACUNGCAP.objects.all()
        for cat in categories:
            total_value = THIETBI.objects.filter(tennhacungcap=cat).aggregate(total=models.Sum('giamua'))['total']
            data.append({'category': cat.tennhacungcap, 'total_value': total_value})

    return JsonResponse(data, safe=False)

def dash_chart(request):
    return render(request, 'thietbi/dash_chart.html')

def dash_data2(request):
    category = request.GET.get('category', 'loai')
    data = []

    if category == 'loai':
        categories = LOAI.objects.all()
        for cat in categories:
            count = THIETBI.objects.filter(tenloai=cat).count()
            data.append({'category': cat.tenloai, 'count': count})
    elif category == 'phong':
        categories = PHONG.objects.all()
        for cat in categories:
            count = THIETBI.objects.filter(tenphong=cat).count()
            data.append({'category': cat.tenphong, 'count': count})
    elif category == 'nhacungcap':
        categories = NHACUNGCAP.objects.all()
        for cat in categories:
            count = THIETBI.objects.filter(tennhacungcap=cat).count()
            data.append({'category': cat.tennhacungcap, 'count': count})

    return JsonResponse(data, safe=False)