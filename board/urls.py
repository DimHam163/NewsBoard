from django.urls import path
from . import views
from .views import AnnouncementCreate, PostList, PostDetail, PostCategory, AnnouncementUpdate, CommentCreate, \
    CommentList, CommentDetail, accept_comment, deny_comment

app_name = 'board'

urlpatterns = [
    path('', PostList.as_view(), name='announcement_list'),
    path('<int:pk>/', PostDetail.as_view(), name='announcement_detail'),
    path('add/', AnnouncementCreate.as_view(), name='ann_create'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name='ann_update'),
    path('category/<int:pk>/', PostCategory.as_view(), name='category'),
    path('<int:pk>/comment/', CommentCreate.as_view(), name="comment"),
    path('comments/', CommentList.as_view(), name="comment_list"),
    path('comments/<int:pk>/', CommentDetail.as_view(), name="comment_detail"),
    path('comments/<int:pk>/accept/', accept_comment, name="accept"),
    path('comments/<int:pk>/deny/', deny_comment, name="deny"),
    path('success/', views.SuccessView.as_view(), name="success"),
]