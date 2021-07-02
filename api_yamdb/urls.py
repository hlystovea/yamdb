from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from ..API_team.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/', include('account.urls')),
    path('api/', include('API_team.urls')),
]
