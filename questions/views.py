from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import Question, Module, Choice
from .forms import AnswerForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json 
from django.http import JsonResponse


class ModuleListView(ListView):
    model = Module
    template_name = 'questions/modules.html'
    context_object_name = 'modules'

# class QuestionListView(ListView):
#     model = Question
#     template_name = 'questions/questions.html'
#     context_object_name = 'questions'

#     def get_queryset(self):
#         module_id = self.kwargs.get('module_id')
#      return Question.objects.filter(module_id=module_id)

    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['forms'] = [AnswerForm(question=question) for question in context['questions']]
#         return context

class ModuleDetailView(DetailView):
    model = Module
    template_name = 'questions/questions.html'
    context_object_name = 'module'

def QuestionDataView(request, pk):
    questions = Question.objects.filter(module_id=pk)
    data = []
    
    for q in questions:
        data.append({str(q): q.getAnswers()})
    
    return JsonResponse({
        'data': data
    })

def QuestionAnswerView(request, pk):
    checked_true = [] # -- green
    checked_false = [] # -- red
    unchecked_true = [] # -- red
    

    question = Question.objects.get(id=request.POST['id'])
    true_list = question.getTrueAnswers()
    false_list = question.getFalseAnswers()

    
    post_data = request.POST.copy()  # Make a copy to modify
    post_data.pop('id', None)
    post_data.pop('csrfmiddlewaretoken', None)
    
    for item in dict(post_data):
        print(item)
        answer = Choice.objects.get(id=item)
        if answer.id in true_list:
            checked_true.append(answer.id)
            true_list.remove(answer.id)
        else:
            checked_false.append(answer.id)
        
    for item in true_list:
            unchecked_true.append(item) 
    
    return JsonResponse({
        'checked_true': checked_true,
        'checked_false': checked_false,
        'unchecked_true': unchecked_true,
        'question':question.id
    })

# async def receive_answers(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         selected_choices = data.get('choices', [])
        
#         correct_choices = []
#         wrong_choices = []

#         for choice_id in selected_choices:
#             try:
#                 choice = Choice.objects.get(id=choice_id)
#                 if choice.correct:
#                     correct_choices.append(choice_id)
#                 else:
#                     wrong_choices.append(choice_id)
#             except Choice.DoesNotExist:
#                 wrong_choices.append(choice_id)

#         response_data = {
#             'message': 'Choices evaluated',
#             'correct_choices': correct_choices,
#             'wrong_choices': wrong_choices
#         }

#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def submit_answer(request, question_id):
    if request.method == 'POST':
        choice_ids = request.POST.getlist('choices')
        choices = Choice.objects.filter(id__in=choice_ids)
        correct_choices = Choice.objects.filter(question_id=question_id, correct=True)
        correct = set(choices) == set(correct_choices)
        return JsonResponse({
            'correct': correct,
            'chosen': list(choices.values_list('id', flat=True)),
            'correct_answers': list(correct_choices.values_list('id', flat=True))
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
