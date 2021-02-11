from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApi,PostApi,UserApi
urlpatterns = [
      path('api/register/', RegisterApi.as_view()),
      path('api/post/', PostApi.as_view()),
      path('api/user/', UserApi.as_view()),

]