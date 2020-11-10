from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

from course.models import Course, CourseTypes
# Create your views here.

def courselist(request):
    course_list = Course.objects.order_by('course_type')
    template = loader.get_template('courselist.html')

    context = {'course_list': course_list}
    for course in course_list:
        course.course_type = CourseTypes[course.course_type][1]
    return HttpResponse(template.render(context))


def detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        course.course_name = course.course_name
        course.course_type = CourseTypes[course.course_type][1]
        # logger.info('course retrieved from db :%s' % course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request, 'course.html', {'course': course})
