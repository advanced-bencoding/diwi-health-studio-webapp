"""diwihealthstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings

import staff.views
import blog.views
import appointment.views
from services import views as services_view
from home import views as home_view
import basicapp.views
urlpatterns = [
    path('', home_view.home, name='home'),
    path('book/', appointment.views.book, name='book'),
    path('manage/', appointment.views.manage, name='manage'),
    path('view/', appointment.views.view, name='view'),
    path('staff/', staff.views.staff,name="staffpage"),
    path('admin/', admin.site.urls),
    path('services/', services_view.services, name='services'),
    path('blog/', blog.views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', blog.views.detail, name='detail'),
    path('edit/<appointment_id>', appointment.views.edit, name='edit'),
    path('create/', appointment.views.create, name='create'),
	path('otp/',basicapp.views.otp,name='otp'),
    path('book/send_otp',basicapp.views.send_otp,name='send_otp')
] + static (settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
