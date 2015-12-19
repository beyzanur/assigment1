
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^histogram/(?P<filename>.*)/$', 'histogram.views.myHistogram', name='myHistogram'),
]
