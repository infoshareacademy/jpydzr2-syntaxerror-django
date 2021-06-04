from django.urls import path
from . import views

app_name = 'credit_app'

urlpatterns = [
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('requests/', views.RequestsView.as_view(), name='requests'),
    ]