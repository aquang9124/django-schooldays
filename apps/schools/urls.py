from django.conf.urls import url
from .views import Students, Teachers, Subjects, TeacherDetailView, SubjectDetailView

urlpatterns = [
	url(r'^$', Students.as_view(), name="students"),
	url(r'^teachers/$', Teachers.as_view(), name="teachers"),
	url(r'^teacher/(?P<pk>[-\w]+)/$', TeacherDetailView.as_view(), name="details"),
	url(r'subjects/$', Subjects.as_view(), name="subjects"),
	url(r'^subject/(?P<pk>[-\w]+)/$', SubjectDetailView.as_view(), name="subjectdetails"),
]