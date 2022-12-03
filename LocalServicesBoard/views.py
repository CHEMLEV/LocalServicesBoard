from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Classified
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import NewUserForm, ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse





class MainPageView (TemplateView):
    template_name = 'home.html'

class AboutPageView (TemplateView):
    template_name = 'about.html'

class ClassifiedsListView(ListView):
    model = Classified
    template_name = "classifieds.html"

class ReviewGet(DetailView):
    model = Classified
    template_name = "classified_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context
    
class ReviewPost(SingleObjectMixin, FormView):
    model = Classified
    form_class = ReviewForm
    template_name = "classified_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.classified = self.object
        #form.instance.classified = self.request.classified
        form.instance.author = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        classified = self.get_object()
        return reverse("classified_detail", kwargs={"pk": classified.pk})


class ClassifiedDetailsView(DetailView): 
    model = Classified
    template_name = "classified_detail.html"

    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)
		

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


class ClassifiedUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Classified
    fields = (
        "title",
        "body",
        "area",
        "phone"
    )
    template_name = "classified_edit.html"

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user

class ClassifiedDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Classified
    fields = (
        "title",
        "body",
    )
    template_name = "classified_delete.html"
    success_url = reverse_lazy('classifieds')

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user

class ClassifiedCreateView(LoginRequiredMixin, CreateView):  # new
    model = Classified
    template_name = "classified_new.html"
    fields = ("title", "body", "area", "phone")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


