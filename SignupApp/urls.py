''' /SignupApp/urls.py '''

from SignupApp.views import *
from django.urls import include, re_path

urlpatterns=[
	re_path(r'^signup/',signup),
	re_path(r'^adduserinfo/',adduserinfo),
]