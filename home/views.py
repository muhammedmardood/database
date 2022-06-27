from django.shortcuts import redirect, render
from .models import Pdf
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


def delete(request, pk):
    if request.method == 'POST':
        pdf = Pdf.objects.get(pk=pk)
        pdf.delete()
    return redirect("home")


def preview(request, pk):
    pdf = Pdf.objects.get(pk=pk)

    context = {
        'pdf': pdf,
    }
    return render(request, 'home/preview.html', context)


class BookListView(ListView):
    model = Pdf
    template_name = "home/class_book_list.html"
    context_object_name = "pdf"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.order_by('-id').filter(name__icontains=query)
        else:
            object_list = self.model.objects.all().order_by('-id')
        return object_list


class UploadPdf(CreateView):
    model = Pdf
    fields = ("name", "uploader", "pdf")
    success_url = reverse_lazy("home")
    template_name = "home/upload.html"


class UpdatePdf(UpdateView):
    model = Pdf
    fields = ("name", "uploader", "pdf")
    template_name = "home/update.html"

    def get_success_url(self):
        return reverse_lazy("home")
