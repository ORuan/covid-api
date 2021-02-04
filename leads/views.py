from leads.models import Leads
from django.shortcuts import render
from leads.forms import UserForm

def register_users(request):
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('/')
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
    if request.method == "POST":
        form_data = UserForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('painel')
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

