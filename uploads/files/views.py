from django.shortcuts import render, redirect #puedes importar render_to_response
from files.form import UploadForm
from files.models import Document
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
        	newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
        	newdoc.save(form)
        	return redirect("subir:cargar")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'Documento/upload.html', {'form': form})


class DocumentoList(ListView):
    model = Document
    template_name = 'Documento/Lista.html'

class DocumentoUpdate (UpdateView):
    model = Document
    form_class = UploadForm
    template_name = 'Documento/update.html'
    success_url = reverse_lazy ('subir:cargar')
