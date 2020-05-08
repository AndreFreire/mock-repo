from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('paciente/createAndGetCip', hello.views.index, name="index"),
    path('paciente/busca', hello.views.index, name="index"),
    path('paciente/update', hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('scheduling', hello.views.index, name="index"),
    path('prescription', hello.views.index, name="index"),
    path('prescriptionStatus', hello.views.index, name="index"),
    path('locations', hello.views.index, name="index"),
    path('exam/v1/agendamento/unidades', hello.views.index, name="index"),
]
