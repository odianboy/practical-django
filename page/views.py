from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import News, Comment
from django.utils import timezone
from .forms import NewsForm, CommentForm


class NewsListView(ListView):
    model = News
    template_name = 'page/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.filter(date_of_creation__lte=timezone.now()).order_by('-date_of_creation')


class NewsDetailView(FormMixin, DetailView):
    model = News
    template_name = 'page/news_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        news_id = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm(initial={'news': self.object})
        comments = Comment.objects.filter(news=news_id)
        context['comments'] = comments

        return context

    def post(self, request, *args, **kwargs):
        news_id = self.kwargs['pk']
        form_comment = self.get_form()

        if form_comment.is_valid():
            form_comment.save()
            return HttpResponseRedirect('')


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'page/create_page_list.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('')
        return render(request, 'page/create_page_list.html', context={'news_form': news_form})


class NewsEditFormView(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'page/page_edit.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return render(request, 'page/page_edit.html', context={'news_form': news_form, 'news_id': news_id})
