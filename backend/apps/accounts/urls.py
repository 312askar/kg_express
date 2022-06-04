from django.urls import path
from .views import *
urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('logout', userLogout, name='logout'),
    path('user/profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('user/profile/update/<int:pk>/', update_user_profile(), name='user_update'),
]
