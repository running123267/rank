

from django.urls import path
from rankings import views
urlpatterns = [

    path('index/',views.Index.as_view()),
    path('show/',views.Show.as_view()),
]
