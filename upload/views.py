from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import UploadImageForm
from .models import UploadImage

class ProfileImageView(FormView):
    template_name = 'main/profile_image_form.html'
    form_class = UploadImageForm

    def form_valid(self, form):
        profile_image = UploadImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs={'pk': self.id})

class ProfileDetailView(DetailView):
    model = UploadImage
    template_name = 'main/profile_image.html'
    context_object_name = 'image'


class ProfileImageIndexView(ListView):
    model = UploadImage
    template_name = 'main/profile_image_view.html'
    context_object_name = 'images'
    queryset = UploadImage.objects.all()