from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Authentication routes
    path(route='register', view=views.registration, name='register'),
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),

    # Car details route
    path(route='get_cars', view=views.get_cars, name='getcars'),

    # Dealership routes (matches /fetchDealers and /fetchDealers/:state)
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>',
         view=views.get_dealerships, name='get_dealers_by_state'),

    # Single dealer details route (matches /fetchDealer/:id)
    path(route='dealer/<int:dealer_id>',
         view=views.get_dealer_details, name='dealer_details'),

    # Dealer reviews route (matches /fetchReviews/dealer/:id)
    path(route='get_reviews', view=views.get_reviews, name='get_reviews'),
    path(route='reviews/dealer/<int:dealer_id>',
         view=views.get_dealer_reviews, name='dealer_reviews'),

    # Add review route (matches POST /insert_review)
    path(route='add_review', view=views.add_review, name='add_review'),

    # Post review route
    path(route='postreview/<int:dealer_id>',
         view=views.post_review_view, name='post_review_view'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
