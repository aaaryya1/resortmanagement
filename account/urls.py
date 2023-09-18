
from .views import HomeView, Userregview
from django.urls import path,include
from django.conf import settings
from guests.views import Guesthmview
from django.conf.urls.static import static
 


urlpatterns=[ path('userreg',Userregview.as_view(),name='Ureg'),
            
              path('guest',Guesthmview.as_view(),name='guesthm'),
              path('hm',HomeView.as_view(),name='hm')
             
             ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
             