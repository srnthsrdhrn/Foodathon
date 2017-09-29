from django.conf.urls import url
from food_Data import views

urlpatterns = [
    url(r'^$', views.entry_view),
    url(r'^get_data', views.GetData.as_view())

]
