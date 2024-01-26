from django.urls import path

from pitch_management_app import views

urlpatterns = [
    path('',views.pitchlist),
    path('pitch-list', views.pitchList, name='pitch-list'),
    path('pitch-create', views.pitchCreate, name='pitch-create'),
    path('pitch-update/<int:id>', views.pitchUpdate, name='pitch-update'),
    path('pitch-delete/<int:id>', views.pitchDelete, name='pitch-delete'),
    path('update_pitch_data_with_weather/<int:pitch_id>/',
        views.update_pitch_data_with_weather,
        name="update_pitch_data_with_weather",
    ),
]