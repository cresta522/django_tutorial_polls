from django.contrib import admin

# Register your models here.
from .models import Question, Choice

"""
モデルの admin のオプションを変更したいときには、モデルごとに admin クラスを作成して、 admin.site.register() の 2 番目の引数に渡す
"""

"""
class ChoiceInline(admin.StackedInline):

の場合、縦に追加されていく
"""

class ChoiceInline(admin.TabularInline):
    # poll追加ダイアログに、choiceモデルを3つ初期表示する
    model = Choice
    extra = 3
    
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    # poll追加ダイアログに、choiceモデルを3つ初期表示する
    inlines = [ChoiceInline]
    
    # 表示列の追加 デフォは__str__
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # フィルターサイドバーの表示
    list_filter = ['pub_date']
    
    # 検索窓
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)