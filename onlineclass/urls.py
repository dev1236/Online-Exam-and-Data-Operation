from django.urls import path
from django.conf.urls import include, url
from . import views



urlpatterns = [
    #path('',views.upload,name='upload'),
   
    path('',views.index),
    path('',views.login),
    path('',views.userdetails),
    path('',views.exampage),
    path('',views.Resultpage),
    path('',views.Dashboard),
    path('',views.StringCalc),
    path('',views.stringresult),
    path('',views.admin),               #admin dashboard funtion created 
    path('',views.qupload),    #question upload funtion declaration
    path('',views.admlogin),
    path('',views.OnlineCompiler),

       
  
  
    
    
    
   
   
   
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^exampage/$', views.exampage, name='exampage'),
    url(r'^Dashboard/$', views.Dashboard, name='Dashboard'),
    url(r'^Resultpage/$', views.Resultpage, name='Resultpage'),
    url(r'^userdetails/$', views.userdetails,name='userdetails'),
    url(r'^StringCalc/$', views.StringCalc,name='StringCalc'),
    url(r'^stringresult/$', views.stringresult,name='stringresult'),
    url(r'^admin/$', views.admin,name='admin'),                 #admin dashboard page link 
    url(r'^qupload/$', views.qupload,name='qupload'),    #question upload html file source link  
    url(r'^admlogin/$', views.admlogin, name='admlogin'),
    url(r'^OnlineCompiler/$', views.OnlineCompiler, name='OnlineCompiler'),
    
    #url(r'^upload/$', views.upload, name='upload'),
    #url(r'^showitem/$', views.showitem, name='showitem'),
]