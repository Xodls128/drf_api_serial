from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
'''인증 및 권한 설정'''
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item,item) for item in get_all_styles()])


class Snippet(models.Model):
    onwer = models.ForeignKey('auth.User', related_name='snippets', on_delete= models.CASCADE)
    #onwer는 사용자를 나타내는 필드 >>> 이제 .save()모델 클레스에 메스드를 추가할 수 있음
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLES_CHOICES, default='friendly',max_length=100)

    class Meta:
        ordering = ['created']

def save(self, *args, **kwargs):
    '''
    pygments 라이브러리를 이용해서 코드 스니펫의 강조 표시된 HTML 표현을 만듦듦
    '''
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super().save(*args, **kwargs)

