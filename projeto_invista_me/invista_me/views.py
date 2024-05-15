from django.shortcuts import render, redirect, HttpResponse
from .models import Investimentos
from .forms import InvestimentosForm
from django.contrib.auth.decorators  import login_required


def investimentos(request):
    dados = { 'dados' : Investimentos.objects.all()  }
    return render(request,'investimentos/investimentos.html', context=dados)



def detalhe(request, id_investimento):
    dados ={ 'dados': Investimentos.objects.get(pk=id_investimento)  }
    return render(request, 'investimentos/detalhe.html', dados)



def criar(request):
    if request.method =='POST':
        investimento_form = InvestimentosForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:            
        investimento_form =  InvestimentosForm()
        formulario = { 'formulario' : investimento_form   }
        return render(request,'investimentos/novo_investimento.html', context=formulario)
   
@login_required    
def editar(request, id_investimento):
    investimento_instance = Investimentos.objects.get(pk=id_investimento)
    # quando alguem acessa a pagina pela primeira vez fazemos um get
    if request.method == 'GET':
        formulario = InvestimentosForm(instance=investimento_instance)
        return render(request, 'investimentos/novo_investimento.html',{'formulario': formulario})
    # caso o contrario, ou seja estamos atualizando e envieando dados fazemos um post
    else:
        formulario = InvestimentosForm(request.POST, instance= investimento_instance)
        if formulario.is_valid():
            formulario.save()
        return redirect ('investimentos')
    
@login_required
def excluir(request, id_investimento):
        # Aqui estamos lindan com envio de dados pelo o usuario - método POST
    investimento = Investimentos.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request,'investimentos/confirmar_exclusao.html', {'item': investimento})
        
    