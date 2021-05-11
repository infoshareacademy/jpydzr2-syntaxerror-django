from django.urls import path
from . import views

app_name = 'credit_app'

urlpatterns = [
    path('calc_predict/', views.predict, name='predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    ]