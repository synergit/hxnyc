from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from course.models import Course, CourseTypes, Registration
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    logger.info("Requesting index page.")
    course_list = Course.objects.order_by('course_type')
    context = {'course_list': course_list}
    for course in course_list:
        course.course_type = CourseTypes[course.course_type][1]
    # return HttpResponse(template.render(context))
    return render(request, 'index.html', context)


def detail(request, course_id):
    logger.info('Displaying course {}'.format(course_id))
    try:
        course = Course.objects.get(pk=course_id)
        course.course_name = course.course_name
        course.course_type = CourseTypes[course.course_type][1]
        # logger.info('course retrieved from db :%t' % course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request, 'course.html', {'course': course})

class RegisterCreateView(LoginRequiredMixin, CreateView):
    template_name = 'register_form.html'
    success_url = '/'
    model = Registration
    fields = ["student_name", "address", "phone",
        "email", "registered_class"]

    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.contact_name = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())