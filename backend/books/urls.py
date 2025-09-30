from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('years', views.YearViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('books', views.BookViewSet, basename='book')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/admin/login/', views.admin_login, name='admin_login'),
    path('api/admin/logout/', views.admin_logout, name='admin_logout'),
    path('api/auth/check/', views.check_auth, name='check_auth'),
]