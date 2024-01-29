from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('jobs',views.viewsetsjobs)

app_name = 'api'
urlpatterns = [

    #1 No rest
    path('norest/',views.no_rest),
    path('fbv/',views.FBV_list),
    path('fbv/<int:pk>',views.FBV_pk),
    path('cbv/',views.CBV_list.as_view()),
    path('cbv/<int:pk>',views.CBV_pk.as_view()),
    path('mixins/',views.Mixins_list.as_view()),
    path('mixins/<int:pk>',views.Mixins_pk.as_view()),
    path('generic/',views.Generic_list.as_view()),
    path('generic/<int:pk>',views.Generic_pk.as_view()),
    path('viewsets/',include(router.urls))

]