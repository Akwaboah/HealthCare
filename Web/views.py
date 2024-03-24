from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Home(View):

    context = {'page' :'home'}

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):

        if 'page' in kwargs:
            self.context.update({'page':kwargs['page']})
            template_name = f"Web/partials/blocks/{kwargs['page']}.html"
            return render(request, template_name, self.context)
        else:
            self.context.update({'page':'home'})
        return render(request, 'Web/home.html', self.context)
    
 