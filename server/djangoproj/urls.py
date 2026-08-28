"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse


def manifest_view(request):
    return JsonResponse({
        "short_name": "App",
        "name": "Dealer App",
        "start_url": "/",
        "display": "standalone"
    })


urlpatterns = [
    # Static frontend pages
    path('', TemplateView.as_view(
        template_name="Home.html"), name='home'),
    path('about/', TemplateView.as_view(
        template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(
        template_name="Contact.html"), name='contact'),
    path('login/', TemplateView.as_view(
        template_name="index.html"), name='login_page'),
    path('register/', TemplateView.as_view(
        template_name="index.html"), name='register_page'),

    # Frontend views for dealership features
    path('dealers/', TemplateView.as_view(
        template_name="index.html"), name='dealers'),
    path('dealer/<int:dealer_id>', TemplateView.as_view(
        template_name="index.html"), name='dealer_details'),
    path('postreview/<int:dealer_id>', TemplateView.as_view(
        template_name="index.html"), name='post_review'),

    # Dealer reviews API endpoint
    path('reviews/', TemplateView.as_view(
        template_name="index.html"), name='get_reviews'),
    path('reviews/dealer/<int:dealer_id>', TemplateView.as_view(
        template_name="index.html"), name='dealer_reviews'),

    # Manifest endpoint
    path('manifest.json', manifest_view),

    # Admin site
    path('admin/', admin.site.urls),

    # Django app backend API endpoints
    path('djangoapp/', include('djangoapp.urls')),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
