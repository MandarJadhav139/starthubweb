
from django.urls import path, include
from django.contrib import admin
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name="index"),
    path('app1/', include('app1.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) is very important as without this media files cannot be displayed example images
