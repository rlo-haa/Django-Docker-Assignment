from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200) # 프로젝트 제목
    description = models.TextField() # 프로젝트 설명
    created_at = models.DateTimeField(auto_now_add=True) # 생성 시각 (자동저장)

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # 어떤 프로젝트에 대한 평가인지
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) # 1~5중에서 하나의 점수
    submitted_at = models.DateTimeField(auto_now_add=True) # 평가 제출 시간
