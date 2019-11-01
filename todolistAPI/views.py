from django.views.generic import TemplateView

class Landing_Page(TemplateView):
    template_name = 'landingpage.html'

class Main_Page(TemplateView):
    template_name = 'mainpage.html'