from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
#ViewSets을 사용할때
from rest_framework import renderers
from snippets.views import api_root, SnippetViewSet, UserViewSet
#from snippets import views 중복
from django.urls import include
from rest_framework.routers import DefaultRouter

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
#router와 register를 사용하면 뷰셋을 라우팅할때 더 간단하게 할수 있음
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

#이렇게 하면 라우터를 통해서 API URL들이 자동으로 생성됨
#뷰셋은 자동으로 list와 detail을 생성해줌
urlpatterns = [
    path('', include(router.urls)),
]
#라우터레지스터를 사용하면 url을 하나씩 작성해서 뷰와 연결하지 않아도 자동으로 연결해줌
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