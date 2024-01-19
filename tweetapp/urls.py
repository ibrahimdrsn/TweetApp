
from django.urls import path
from . import views



app_name= 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name="listtweet"),      #ibrahimdursun.com/tweetapp
    path('addtweet/', views.addtweeet, name="addtweet"),    #ibrahimdursun.com/tweetapp/addtweet/
    path('addtweetbyform/', views.addtweetbyform, name="addtweetbyform"),
    path('addtweetmodelform/', views.addtweetmodelform, name="addtweetmodelform"),
    path("signup/", views.SignUpView.as_view(),name="signup"),
    path("deletweet/<int:id>", views.deletetweet, name="deletetweet")
    
]