from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # 토큰 생성 뷰
    TokenRefreshView, # 토큰 유효성 검증 뷰
    TokenVerifyView, # 토큰 재발급 뷰 (refresh token > access token)
)

urlpatterns = [
    path('login/', views.login_view),
    path('signup/', views.create_user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
