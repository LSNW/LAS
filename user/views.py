from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from split.models import ServiceRecord
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


class profile(LoginRequiredMixin, ListView):
    model = ServiceRecord
    template_name = "user/profile.html"
    context_object_name = 'sr'

    def get_queryset(self):
        allQ = super().get_queryset()
        return allQ.filter(user = self.request.user)
