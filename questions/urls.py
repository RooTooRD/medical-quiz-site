from django.urls import path
from . import views

urlpatterns = [
    path('modules/', views.ModuleListView.as_view(), name='modules'),
    path('<pk>/', views.ModuleDetailView.as_view(), name='module-detail'),
    path('<pk>/data', views.QuestionDataView, name='questions-data'),
    path('<pk>/answer/', views.QuestionAnswerView, name='question-answer'),
    #path('receive-answers/', views.receive_answers, name='receive_answers'),
    #path('questions/submit/<int:question_id>/', views.submit_answer, name='submit-answer'),
    #path('<str:question_name>/', views.AnswerQuestionView.as_view(), name='answer_question'),
]
