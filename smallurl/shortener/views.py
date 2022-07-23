from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from smallurl.core.utils import generate_absolute_redirection_url

from .forms import ShortenerForm
from .models import Shortener


def home_view(request):
    template = "home.html"
    context = {}
    context["form"] = ShortenerForm()
    if request.method == "GET":
        return render(request, template, context)
    elif request.method == "POST":
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = generate_absolute_redirection_url(
                request.build_absolute_uri("/"), shortened_object.hash_url
            )
            context.update({
                "new_url": new_url,
                "full_url": shortened_object.full_url
            })
            return render(request, template, context)
        context["errors"] = used_form.errors
        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    shortener = get_object_or_404(Shortener, hash_url=shortened_part)
    shortener.follow()
    return HttpResponseRedirect(shortener.full_url)
