from django.urls import path
from .views import SignupView, Login_View, Logout_View, StartupListView, StartupDetailView, ApplicationFormView
app_name = 'app1'
urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', Login_View, name="login"),
    path('logout/', Logout_View, name="logout"),
    path('home/', StartupListView.as_view(), name="home"),
    path('detail/<slug:slug>/', StartupDetailView.as_view(), name="detail"),
    path('form/', ApplicationFormView, name="form"),
]
