from django.urls import path

from . import views

app_name = 'redditapp'
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('r/<str:subreddit_name>/', views.subreddit, name='subreddit'),
    path('r/<str:subreddit_name>/<int:pk>/<slug:post_slug>/comments/', views.comments_page, name='comments_page'),
    path('user/', views.UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('users/', views.RegistrationAPIView.as_view(), name='users'),
    path('users/login/', views.LoginAPIView.as_view(), name='login'),
    path('subreddit/create/', views.CreateSubredditView.as_view(), name='create_subreddit'),
    path('r/<str:subreddit_name>/create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('comments/', views.CreateCommentView.as_view(), name='create_comment'),
    path('subreddits/', views.SubredditList.as_view(), name='subreddit_list'),
    path('comment/vote/', views.VoteOnComment.as_view(), name='vote_comment')
]
