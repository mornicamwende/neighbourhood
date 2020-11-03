from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   path('add_hood/', views.add_hood, name='add_hood'),
   path('post/<hood_id>', views.create_post, name='add_post'),
   path('', views.hoods, name='all_hoods'),
   path('hood/<hood_id>', views.hood, name='hood'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)