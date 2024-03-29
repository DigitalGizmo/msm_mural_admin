"""mural URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from .schema import schema
# from django.views.generic import TemplateView
from panels import views


urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html")),
    path('graphql/', 
       csrf_exempt(GraphQLView.as_view(graphiql=True)), 
       name='graphql'),
    path('', views.PanelListView.as_view(), name='index.html'),
    path('attract/', views.AttractListView.as_view(), name='attract.html'),
    path('panels/', include('panels.urls', namespace='panels')),
    path('pops/', include('pops.urls', namespace='pops')),
    path('admin/', admin.site.urls),
]
