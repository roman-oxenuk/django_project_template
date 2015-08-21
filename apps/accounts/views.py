from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login as login_function
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse_lazy('hello'))
    else:
        form = AuthenticationForm(data=request.POST or None)
        if form.is_valid():
            login_function(request, form.get_user())
            return redirect(reverse_lazy('hello'))
        else:
            return render(request, 'accounts/login_form.html', {'form': form})
    return response
