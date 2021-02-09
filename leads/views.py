from leads.models import Leads
from django.shortcuts import render, redirect
from leads.forms import UserForm, UserDelForm
from django.core.exceptions import ObjectDoesNotExist
import logging


def register_users(request):
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('leads:sucess')
        else:
            form_data = UserForm(request.POST)
            return render(request, 'forms/create.html', {'form': form_data})
        return render(request, 'forms/create.html', {'form': form_data})
    else:
        form_data = UserForm()
        logging.warning('erro')
        context = {
            "form": form_data,
            "title": "Cadastro"
        }
        return render(request, 'forms/create.html', context)


def cancel_users(request):
    context = dict()
    if request.method == "POST":
        form_del = UserDelForm(request.POST)
        lead_instance = Leads.objects.get(
            number=request.POST['number'])
        lead_instance.delete()
        return redirect('leads:sucess')
    else:
        context['form'] = UserDelForm()
        return render(request, 'forms/cancel.html', context)


def sucess(request):
    return render(request, 'sucess.html')


def _redirect(request):
    return redirect('leads:create')
