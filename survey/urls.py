from django.contrib import admin
from django.urls import path, include
import account.views
import mypage.views
import register.views
import main.views
import commentcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('login/', account.views.login, name="login"),
    path('logout/', account.views.logout, name="logout"),
    path('signup/', account.views.signup, name="signup"),
    path('search/', main.views.search, name="search"),
    path('register/write', register.views.write, name="write"),
    path('register/join2', register.views.join2, name="join2"),
    path('register/join2/administration', register.views.administration, name="administration"),
    path('register/join2/economy', register.views.economy, name="economy"),
    path('register/join2/engineering', register.views.engineering, name="engineering"),
    path('register/join2/art', register.views.art, name="art"),
    path('register/postcreate', register.views.postcreate, name='postcreate'),
    path('register/<int:post_id>', register.views.show, name="show"),
    path('mypage', mypage.views.mypagesee, name="mypage"),

    path('commentcreate/<int:post_id>', commentcrud.views.commentcreate, name='commentcreate'),

    #path('commentcrud/', include('commentcrud.urls')),
]
