from django.urls import path
from app import views
urlpatterns =[
    path('', views.home_page, name='home_page'),
    path('hello/', views.hello, name='hello'),
    path('job/<int:id>',views.jobPage, name='job_url')
]