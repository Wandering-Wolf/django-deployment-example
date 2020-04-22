from django.urls import path, include
from basic_app import views

#for template tagging (app_name is a keyword)
app_name = 'basic_app' #this name(basic_app) is used in the relative_url_templates.html page
#and so is the values assigned to the name parameter for eavh path()
urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/', views.other, name = 'other'),
]
