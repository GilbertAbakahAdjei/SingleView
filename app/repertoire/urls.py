from django.urls import path
from .views import FileViews, FileDataViews

urlpatterns = [
    path('', FileViews.as_view()),
    path('<int:id>', FileViews.as_view()),
    path('<int:file_id>/works', FileDataViews.as_view()),
    path('<int:file_id>/works/<int:id>', FileDataViews.as_view()),


]