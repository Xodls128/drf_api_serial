from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLES_CHOICES

#유저 모델에 엔드포인트 추가
from django.contrib.auth.models import User


class SnippetSerializer(serializers.serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLES_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source='owner.username')#이렇게하면 owner필드는 읽기전용이 됨, 유저 이름을 보여줌
    #owner = serializers.CharField(read_only=True) 이렇게 해도 읽기전용이 됨
    
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        
        return instance

class SnippetModelSerializer(serializers.ModelSerializer):#이렇게하면 create랑 update 자동으로 해줌, 직렬화도 필드일일이 지정안하고 자동으로 해줌
    
    owner = serializers.ReadOnlyField(source='owner.username')#메타 밖에다 정의해야 리드온리로 할수 있음. 이러면 유저 이름으로 반환됨
    class Meta:
#만약 메타 안에다가 정의하면 owner필드는 외래키 이므로 기본적으로 ID로 변환됨 + 리드온리 설정안됨됨
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style','owner',]


#유저 정보를 API에 추가하기위해 새 직렬화를 만듦
class UserSerializer(serializers.Modelserializer):
    snippet = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
#스니펫은 '유저 모델'에서 역직렬화를 해야하기 때문에 새로운 직렬화클래스가 필요함

#5.hyperlinked APIs

class UserSerializerHyperlinked(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet-detail',
        read_only=True
    )
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

class SnippetSerializerHyperlinked(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']

