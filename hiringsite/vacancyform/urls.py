from django.urls import path
from .views import vacancy_detail, get_my_vacancy, \
VacancyCreateView, VacancyDeleteView, VacancyResponse

urlpatterns = [
    path('<vacancy_id>/detail', vacancy_detail, name='vacancy_detail'),
    path('<vacancy_id>/response', VacancyResponse.as_view(), name='vacancy_response'),
    path('my', get_my_vacancy, name='vacancy_my'),
    path('my/create', VacancyCreateView.as_view(), name='vacancy_create'),
    path('my/<int:pk>/delete', VacancyDeleteView.as_view(), name='vacancy_delete'),
]
