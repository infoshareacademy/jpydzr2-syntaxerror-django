from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'credit_app'

urlpatterns = [
    path('', views.predict_and_contact_forms, name='submit_prediction'),
    path('', views.home, name='home'),
    path('', views.testimonials, name='testimonials'),
    path('', views.predict_and_contact_forms, name='contact'),
    path('requests/', views.RequestsView.as_view(), name='requests'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)