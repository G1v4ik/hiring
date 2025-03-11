from django.urls import path
from .views import vacancy_detail

urlpatterns = [
    path('<vacancy_id>', vacancy_detail)
]
