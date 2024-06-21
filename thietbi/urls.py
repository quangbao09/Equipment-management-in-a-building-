from django.urls import path
from . import views

app_name = "thietbi"
urlpatterns = [
    path("", views.index, name="index"),
    path("themthietbi/", views.themthietbi.as_view(), name="themthietbi"),
    path("chitietthietbi/<int:id>/", views.chitietthietbi.as_view(), name="chitietthietbi"),
    path("xoathietbi/<int:id>/", views.xoathietbi, name="xoathietbi"),
    path("loai/", views.loai, name="loai"),
    path("loai/themloai/", views.themloai.as_view(), name="themloai"),
    path("loai/<int:id>/", views.getThietBiTheoLoai, name="thietbitheoloai"),
    path("loai/chitietloai/<int:id>/", views.chitietloai.as_view(), name="chitietloai"),
    path("loai/xoaloai/<int:id>/", views.xoaloai, name="xoaloai"),
    path("phong/", views.phong, name="phong"),
    path("phong/themphong/", views.themphong.as_view(), name="themphong"),
    path("phong/<int:id>/", views.getThietBiTheoPhong, name="thietbitheophong"),
    path("phong/chitietphong/<int:id>/", views.chitietphong.as_view(), name="chitietphong"),
    path("phong/xoaphong/<int:id>/", views.xoaphong, name="xoaphong"),
    path("nhacungcap/", views.nhacungcap, name="nhacungcap"),
    path("nhacungcap/themnhacungcap/", views.themnhacungcap.as_view(), name="themnhacungcap"),
    path("nhacungcap/<int:id>/", views.getThietBiTheoNhaCungCap, name="thietbitheonhacungcap"),
    path("nhacungcap/chitietnhacungcap/<int:id>/", views.chitietnhacungcap.as_view(), name="chitietnhacungcap"),
    path("nhacungcap/xoanhacungcap/<int:id>/", views.xoanhacungcap, name="xoanhacungcap"),
    path("searchthietbi/", views.searchthietbi, name="searchthietbi"),
    path("sortthietbi/", views.sortthietbi, name="sortthietbi"),
    path("dangxuat/", views.dangxuat, name="dangxuat"),
    path("chitietnguoidung/", views.chitietnguoidung.as_view(), name="chitietnguoidung"),
    path('locthietbitheogia/', views.locThietBiTheoGia, name='locthietbitheogia'),
    path('locthietbitheobaohanh/', views.locThietBiTheoBaoHanh, name='locthietbitheobaohanh'),
    path('dash-data/', views.dash_data, name='dash_data'),
    path('dash-chart/', views.dash_chart, name='dash_chart'),
    path('dash-data2/', views.dash_data2, name='dash_data2'),
]