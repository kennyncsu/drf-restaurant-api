from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from restaurantapi.views import UserViewSet, GroupViewSet, MenuViewSet, MenuItemViewSet, AvailableMenuList, AvailableMenuDetail

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'menuitem', MenuItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^available-menus/$', AvailableMenuList.as_view()),
    url(r'^available_menus/(?P<pk>[0-9]+)/$', AvailableMenuDetail.as_view()),
]
