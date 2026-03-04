from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.forms import SnippetForm
from MainApp.models import Snippet



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # Создаем пустую форму при запросе GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form' : form
            }
    
        return render(request, 'pages/add_snippet.html', context)
    
    # Получаем данные из формы и на их основе создаем новый сниппет сохраняя его в бд

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list") # переход на страницу списка snippets-list
        return render(request, 'pages/add_snippet.html', context= {'form': form})    


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
            'pagename': 'Просмотр сниппетов',
            'snippets': snippets
            }                              
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    context = {'pagename': 'Сниппет'}
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except Snippet.DoesNotExist:
        return render(request, 'pages/errors.html', context | {'error': f"Snippet with id= {snippet_id} not found"})
     
    else:
        context['snippet']= snippet

            
        return render(request, 'pages/snippet_detail.html', context)
    

def snippet_delete(request, snippet_id):
    if request.method == 'GET' or request.method == 'POST':
        snippet = get_object_or_404(Snippet, id=snippet_id)
        snippet.delete()

    return redirect('snippets-list')
    
    pass


def snippet_edit(request, snippet_id): 
    pass   
    

   

