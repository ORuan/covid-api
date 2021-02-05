from leads.models import Leads
from django.shortcuts import render, redirect
from leads.forms import UserForm
from django.core.exceptions import ObjectDoesNotExist

def register_users(request):
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('leads:create')
        else:
            form_data = UserForm(request.POST)
            return render(request, 'forms/create.html', {'form':form_data})
        return render(request, 'forms/create.html', {'form':form_data})
    else:
        form_data = UserForm()
        context = {
            "form":form_data,
            "title":"Cadastro"
        }
        return render(request, 'forms/create.html', context)

def cancel_users(request):
    errors = dict()
    if request.method == "GET":
        number = request.GET['telephoneNumber']
        try:
            lead_instance = Leads.objects.get(number=number)
            lead_instance.delete()
            return redirect('leads:sucess')
        except ObjectDoesNotExist:
            errors['noexist'] = "Número não encontrado"
            return render(request, 'forms/cancel.html', context=errors)
        except Exception as err:
            errors['others'] = err
            return render(request, 'forms/cancel.html', context=errors)

        return render(request, 'forms/cancel.html', context=errors)

def sucess(request):
    return render(request, 'sucess.html')