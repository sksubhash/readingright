
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('account.urls')),
]