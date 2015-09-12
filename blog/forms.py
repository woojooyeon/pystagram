from django import forms
from blog.models import Post, Comment
from my_pystagram.widgets import PointWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #모든 필드 노출
        #fields = '__all__'

        #노출시키고 싶지 않은 필드를 설정할때는 아래와 같이 exclude
        #exclude = ('author')
        # 모든 필드를 노출하고 싶지 않은 경우 아래와 같이 구현한다.
        fields = ('category', 'title', 'content', 'photo', 'lnglat', 'tags', 'origin_url')
        widgets = {
            'lnglat': PointWidget
        }


    # 특정 필드에 관하여 에러메시지의 조건과 메시지를 정의하고 싶은 경우
    # clean_필드명 으로 함수명 정의
    def clean_title(self):
        title = self.cleaned_data.get('title','')

    # 만약 입력받은 특정 필드를 후처리하고 싶은경우 아래와 같이 후처리 후 값을 리턴
        title = self.cleaned_data.get('title','').strip()
        if len(title) < 10:
            raise forms.ValidationError('10자 이상 입력하세요.')
        return title




    # 여러 필드의 에러머시지와 조건을 정의하고 싶은 경우
    def clean(self):
        title = self.cleaned_data.get('title','')
        content = self.cleaned_data.get('content','')
        if len(title) < 10 and len(content) < 10:
            raise forms.ValidationError('제목과 내용을 10자 이상 입력하세요.')
        return self.cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)