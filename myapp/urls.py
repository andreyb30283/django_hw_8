from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, SubTaskListCreateView, \
    SubTaskRetrieveUpdateDestroyView, CategoryViewSet, LoginView, LogoutUserView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
    path('', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutUserView.as_view(), name= 'logout')

]
