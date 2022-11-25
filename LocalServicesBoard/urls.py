from django.urls import path
from .views import MainPageView, ClassifiedsListView, ClassifiedDetailsView, AboutPageView, ClassifiedUpdateView, ClassifiedDeleteView, ClassifiedCreateView
from . import views


urlpatterns = [
    
    path("", MainPageView.as_view(), name = "home"),
    path("about/", AboutPageView.as_view(), name = "about"),
    path("classifieds/", ClassifiedsListView.as_view(), name = "classifieds"),
    path("classified/<int:pk>/", ClassifiedDetailsView.as_view(), name = "classified_detail"),
    path("register/", views.register_request, name="register"),
    path("classified/<int:pk>/edit", ClassifiedUpdateView.as_view(), name = "classified_edit" ),
    path("classified/<int:pk>/delete", ClassifiedDeleteView.as_view(), name = "classified_delete" ),
    path("classified/new/", ClassifiedCreateView.as_view(), name = "classified_new"),
    
]
