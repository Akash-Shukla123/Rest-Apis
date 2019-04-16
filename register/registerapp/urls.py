from django.urls import path,include
from .import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('student',views.studentview)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.createuserView.as_view(),name='user'),
    path('api-auth',include('rest_framework.urls', namespace='rest_framework')),

]