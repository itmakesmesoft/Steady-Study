from django import forms
from .models import Articles
# models의 Articles클래스를 불러옴

# form class : model에 없는 값을 입력받고 싶을 때



# modelform class: model에 있는 값만 입력받고 싶을 때
class ArticleForm(forms.ModelForm):
    # 이 클래스를 설명하는 클래스 = Meta
    class Meta:
        model = Articles
        # 사용자의 입력을 원하는 필드 종류
        fields = '__all__' # 모델에 있는 모든 필드
        # exclude
        