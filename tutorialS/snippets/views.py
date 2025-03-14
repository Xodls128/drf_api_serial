from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetModelSerializer

#1api Rq and Rp
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#2Class based Views
from django.http import Http404
from rest_framework.views import APIView
#from rest_framework.response import Response 중복복
from rest_framework import status
#3generic APIView & Mixins
from rest_framework import mixins
from rest_framework import generics
#4.Authentication 
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

#4.Permissions
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

#5.Relationships 
#from rest_framework.decorators import api_view 중복복
#from rest_framework.response import Response 중복복
from rest_framework.reverse import reverse

#5.Hyperlinked APIs
from rest_framework import renderers

#6.ViewSets
from rest_framework import viewsets
#from rest_framework import renderers 중복
from rest_framework.decorators import action
#from rest_framework.response import Response 중복복




'''1. Serialization'''
# @csrf_exempt
# def snippet_list(request):


#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetModelSerializer(snippets, many= True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetModelSerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status=400)
# 
# 
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetModelSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetModelSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

'''Requests and Responses'''
# @api_view(['GET','POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetModelSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SnippetModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    


#     if request.method == 'GET':
#         serializer = SnippetModelSerializer(snippet)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SnippetModelSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

'''Class based views'''

# class SnippetList(APIView):
#     "List all snippets, or craet a new snippet"
#     def get(sef, request, format=None):
#         snippet = Snippet.objects.all()
#         serializer = SnippetModelSerializer(snippet, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = SnippetModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     "Retrieve, update or delete a snippet instance."
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetModelSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetModelSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''Generic APView & Mixin을 사용'''
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#     #리스트 믹신이랑 크리에이트믹신을 클래스 인자로 가져왔으니까 
#     # self.리스트랑 self.크리에이트 사용 가능

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

'''list와 detail을 제네릭뷰로 만듦'''
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
#사용자와 스니펫 연결하기기
    def perform_create(self, serializer):#create()메서드를 오버라이드해서 owner필드를 저장
        serializer.save(owner=self.request.user)#owner필드에 현재 인증된 사용자를 할당
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#인증된 사용자만 수정가능

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#인증된 사용자만 수정가능

'''유저 list와 detail을 제네릭뷰로 만듦'''
class UserList(generics.ListAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
#이렇게하면 API의 루트로 이동할 수 있는 URL을 반환함


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    # 이 뷰는 JSON이 아니라 HTML 데이터를 직접 반환해야 하므로
    #StaticHTMLRenderer를 사용함
    #Snippet의 하이라이티드 필드는 하이라이트 된 HTML을 저장하는필드임
    #따라서 변환없이 그대로 반환하는 것이 적절

'''ViewSets을 사용'''
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    '''ReadOnlyModelViewSet은 자동으로 list와 detail을 생성해줌'''

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    '''ModelViewSet은 자동으로 list, create, retrieve, update, destroy를 생성해줌'''
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #action 데코레이터는 사용자 정의의 뷰셋 액션을 추가할 수 있게 해줌
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    #이렇게하면 하이라이트 액션을 추가할 수 있음

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    #이렇게하면 스니펫을 생성할때 owner필드에 현재 인증된 사용자를 할당함
    #이렇게하면 인증된 사용자만 수정가능하게 할수 있음