"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from accounts.views import *
import os
from main import views


# api 문서를 위한 setting
schema_view = get_schema_view(
    openapi.Info(
        title="Thin9",
        default_version='0.0.0',
        description="Thin9의 Backend api를 위한 문서입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="이메일"), # 부가정보
        # license=openapi.License(name="mit"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # 관리자 페이지
     # path('admin/', admin.site.urls),

    # API 요청(/api 로 시작)
    path('api/', include('api.urls')),
    
    # document
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    # 이 아랫 부분은 우리가 사용하는 app들의 URL들을 넣습니다.
    # path('app이름', include('app이름.urls'))

    # # 웹페이지
    # !: front 분리로 인해 주석처리
    # path('', TemplateView.as_view(template_name='index.html')), # 메인 화면
    # path('login/', TemplateView.as_view(template_name='index.html')), # 로그인 화면
    # path('join/', TemplateView.as_view(template_name='index.html')), # 회원가입 화면
    # path('success/', TemplateView.as_view(template_name='index.html')),
    # path('Mypage/', TemplateView.as_view(template_name='index.html')),
    # # 식단 업로드
    # path('calendar/', TemplateView.as_view(template_name='index.html')),
    # path('calendar/<str:date>', TemplateView.as_view(template_name='index.html')), # 특정 날짜 선택

    # path('daily/', TemplateView.as_view(template_name='index.html')), # Daily 식단
    # path('stats/', TemplateView.as_view(template_name='index.html')), # 식단 통계
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('login/', serve, {'document_root': settings.STATIC_ROOT, 'path': 'capstone-cra/build/index.html'}),


#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#STATIC_URL = '/static/'

#STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'static'),
    #os.path.join(BASE_DIR, 'static/capstone-cra/build')
#]

#STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'staticfiles')

#STATICFILES_EXCLUDE = [
    #'node_modules',
#]