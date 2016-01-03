
from django.conf.urls import url

import views

app_name = 'vote'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/', views.questions),
    url(r'^newquest/', views.submit_question),
    url(r'^submit/', views.submit),
    url(r'^responses', views.responses),
]
