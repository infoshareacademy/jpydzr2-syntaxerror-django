from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'credit_app'

urlpatterns = [
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('requests/', views.RequestsView.as_view(), name='requests'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)