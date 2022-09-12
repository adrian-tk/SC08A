from django.urls import path

from . import views

app_name = 'SC08A'
urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
#    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#    path('<int:pk>/results/', views.DetailView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('motor/', views.MotorsView.as_view(), name='motors'),
    path('motor/<int:pk>/', views.MotorDetail.as_view(), name='one_motor'),
    path('motor/setval/', views.SetVal.as_view(), name='setval'),
   # path('motor/<int:pk>/update_name', views.UpdateName.as_view(), name='update_name'),
    path('motor/<int:moto_id>/update_name', views.update_name, name='update_name'),
    path('motor/<int:moto_id>/update_channel', views.update_channel, name='update_channel'),
    path('motor/add_motor', views.add_motor, name='add_motor'),
    path('motor/<int:moto_id>/delete_motor', views.delete_motor, name='delete_motor'),
    ]
        
