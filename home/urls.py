from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="home"),
    path("class_upload/", views.UploadPdf.as_view(), name="upload"),
    path("book/<int:pk>", views.delete, name="delete"),
    path("preview/<int:pk>", views.preview, name='preview'),
    path('edit/<int:pk>', views.UpdatePdf.as_view(), name='edit')
]
