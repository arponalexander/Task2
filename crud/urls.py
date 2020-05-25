from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CRUD API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_register.urls')),
    path('crud/', schema_view),

]
