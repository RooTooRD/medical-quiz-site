from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    text = models.TextField()
    year = models.IntegerField()
    course = models.CharField(max_length=100)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text};;;;;{self.id}'
    
    def get_form(self):
        from .forms import AnswerForm
        return AnswerForm(question=self)
    
    def getAnswers(self):
        return [ str(choice) for choice in self.choice_set.all() ]

    def getTrueAnswers(self):
        return [choice.id for choice in self.choice_set.all() if choice.correct]

    def getFalseAnswers(self):
                return [choice.id for choice in self.choice_set.all() if not choice.correct]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text};;;;;{self.id}'