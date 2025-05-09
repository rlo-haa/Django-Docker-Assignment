from django.contrib import admin
from django.db.models import Avg
from .models import Project, Rating

class ProjectAdmin(admin.ModelAdmin):
    # 'average_score'와 'ranking'을 리스트에 추가
    list_display = ('title', 'created_at', 'average_score', 'ranking')  # 평균 점수와 등수 표시

    def average_score(self, obj):
        # 프로젝트별 평균 점수를 계산하고 가독성을 위해 소수점 3자리로 반올림
        average_score = obj.rating_set.aggregate(Avg('score'))['score__avg']
        return round(average_score, 3) if average_score is not None else 0  # None일 경우 0 반환
    average_score.short_description = 'Average Score'  # 컬럼 제목 설정

    def ranking(self, obj):
        # 평균 점수 기준으로 내림차순 정렬하여 프로젝트의 등수 계산
        all_projects = Project.objects.annotate(average_score=Avg('rating__score')).order_by('-average_score')
        rank = list(all_projects).index(obj) + 1  # 등수는 1부터 시작
        return rank
    ranking.short_description = 'Rank'  # 컬럼 제목 설정

admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating)
