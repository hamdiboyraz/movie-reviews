from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/create', views.createReview, name='createreview'),
    path('review/<int:review_id>', views.updateReview, name='updatereview'), 
]

# updatereview -> http://localhost:8000/movie/review/2