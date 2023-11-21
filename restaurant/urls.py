from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('reservations/', views.reservations, name="reservations"),
    # API paths
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('api/users/',
         UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('api/users/<int:pk>/', UserViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    path('api/users/me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),
]
