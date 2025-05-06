"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from studentorg import views as a
from django.contrib.auth import views as auth_views
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth

from django.db.models import Count
from datetime import datetime

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', a.HomePageView.as_view(), name='home'),
    path('home.html', a.HomePageView.as_view(), name='home.html'),

    path('organization_list', a.OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', a.OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', a.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', a.OrganizationDeleteView.as_view(), name='organization-delete'),

    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    path('student_list/', a.StudentListView.as_view(), name='student-list'),
    path('student_list/add/', a.StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>/', a.StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete/', a.StudentDeleteView.as_view(), name='student-delete'),

    path('orgmember_list/', a.OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmember_list/add', a.OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/<pk>', a.OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/<pk>/delete/', a.OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    
    path('college_list/', a.CollegeListView.as_view(), name='college-list'),
    path('college_list/add/', a.CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>/', a.CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<pk>/delete/', a.CollegeDeleteView.as_view(), name='college-delete'),

    path('program_list/', a.ProgramListView.as_view(), name='program-list'),
    path('program_list/add/', a.ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<pk>/', a.ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete/', a.ProgramDeleteView.as_view(), name='program-delete'),

    path('dashboard_chart', a.ChartView.as_view(), name='dashboard-chart'),
    path('barChart/', a.BarCountStudentsPerOrganization, name='bar-chart'),
    path('pieChart/', a.PieCountStudentsPerProgram, name='pie-chart'),
    path('lineChart/', a.LineChartStudentsJoinedOrg, name='line-chart'),
    path('horizontalBarChart/', a.HorizontalBarChartStudentsPerProgram, name='horizontal-bar-chart'),
    path('floatingChart/', a.FloatingBubbleChartStudentsPerOrganization, name='floating-chart'),
]
