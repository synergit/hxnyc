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

from opentelemetry import metrics
from opentelemetry.exporter.opencensus.metrics_exporter import (
    OpenCensusMetricsExporter,
)
from opentelemetry.sdk.metrics import Counter, Meter, MeterProvider
# from opentelemetry.exporter.prometheus import PrometheusMetricsExporter

# TODO: move the receiver and exporter code out to be reused by other components
exporter = OpenCensusMetricsExporter(
    service_name="basic-service", endpoint="localhost:55678"
)

metrics.set_meter_provider(MeterProvider())
meter = metrics.get_meter(__name__)
metrics.get_meter_provider().start_pipeline(meter, exporter, 5)

requests_counter = meter.create_counter(
    name="hxnyc",
    description="number of requests",
    unit="1",
    value_type=int,
)

def index(request):
    logger.info("Requesting index page.")
    course_list = Course.objects.order_by('course_type')
    context = {'course_list': course_list}
    for course in course_list:
        course.course_type = CourseTypes[course.course_type][1]
    
    
    requests_counter.add(1, {"page": "index"})

    return render(request, 'index.html', context)


def detail(request, course_id):
    logger.info('Displaying course {}'.format(course_id))

    # OTEL
    requests_counter.add(1, {"page": f'detail:{course_id}'})
    try:
        course = Course.objects.get(pk=course_id)
        course.course_name = course.course_name
        course.course_type = CourseTypes[course.course_type][1]
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
        # OTEL
        requests_counter.add(1, {"RegisterCreateView-save": f'{self.object.contact_name}'})
        return HttpResponseRedirect(self.get_success_url())