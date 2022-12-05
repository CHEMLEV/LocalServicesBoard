from django.urls import path
from .views import MainPageView, ClassifiedsListView, ClassifiedDetailsView, AboutPageView, ClassifiedUpdateView, ClassifiedDeleteView, ClassifiedCreateView, ReviewUpdateView, ReviewDeleteView, ReviewCreateView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    
    path("", MainPageView.as_view(), name = "home"),
    path("about/", AboutPageView.as_view(), name = "about"),
    path("classifieds/", ClassifiedsListView.as_view(), name = "classifieds"),
    path("classified/<int:pk>/", ClassifiedDetailsView.as_view(), name = "classified_detail"),
    path("register/", views.register_request, name="register"),
    path("classified/<int:pk>/edit", ClassifiedUpdateView.as_view(), name = "classified_edit" ),
    path("classified/<int:pk>/delete", ClassifiedDeleteView.as_view(), name = "classified_delete" ),
    path("classified/new/", ClassifiedCreateView.as_view(), name = "classified_new"),
    path("review/<int:pk>/edit", ReviewUpdateView.as_view(), name = "review_edit" ),
    path("review/<int:pk>/delete", ReviewDeleteView.as_view(), name = "review_delete" ),
    path("review/<int:pk>/new/", ReviewCreateView.as_view(), name = "review_new"),
    
]

urlpatterns += staticfiles_urlpatterns()