from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from tabo import views
from tabo.views import base_views, main_views

urlpatterns = [
    path('', main_views.show_main, name='show_main'),
    path('tabo/', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('tabo/', include('tabo.urls')),
    path('common/', include('common.urls')),
    path('QA/', include('QA.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)