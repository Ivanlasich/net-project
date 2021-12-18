from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
import smtplib


class MessageSender():
    def __init__(self):
        self.sent_from = "*********"
        self.gmail_password = "*********"
    def send(self, text, to):
        email_text = text
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.sent_from, self.gmail_password)
            server.sendmail(self.sent_from, to, email_text)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/revisions.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url ='/news/'
    template_name = 'news/news-delete.html'

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    #messageSender = MessageSender()
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            #to = [form.cleaned_data['mail']]
            #messageSender.send("The article has been published and is waiting for your reading!", to)
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)