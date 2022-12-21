from django.urls import path
from customer import views

urlpatterns = [
    path('',views.home,name="home"),
    path('api/recharge-list', views.recharge, name="recharge_list"),
    path('api/history/<int:num>', views.history, name="history"),
    path('recharge/<int:id>/<int:num>', views.do_recharge, name="detail_recharge")

]