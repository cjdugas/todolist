from django.views import generic

from core.models import List, Task


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'list_list'

    def get_queryset(self):
        return List.objects.order_by('-title')


class DetailView(generic.DetailView):
    model = List
    template_name = 'core/detail.html'

    def get_queryset(self):
        return List.objects


#add tasks page


