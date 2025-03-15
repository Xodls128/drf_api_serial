from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


'''함수기반 뷰일때'''
# urlpatterns =[ 
#      path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

'''클래스기반 뷰일때'''
# urlpatterns =[
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>', views.SnippetDetail.as_view()),

#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>', views.UserDetail.as_view()),
#     #하이라이트 엔드포인트 추가
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
#     ]

#urlpatterns = format_suffix_patterns(urlpatterns)

'''릴레이션쉽과 하이퍼링크드 API'''
#API endpoint
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
])