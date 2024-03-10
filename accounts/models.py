from django.db import models

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model): # 기본정보: 유저아이디, 비밀번호, 이름, 닉네임, 성별, 나이, 주소, 전화번호
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=(('male', '남성'), ('female', '여성')))
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # User 모델에 이미 존재하는 필드는 제외 (username, password, first_name, last_name, email)

    def __str__(self):
        return f"{self.user.username}'s profile"

class StudentProfile(Profile): # 학생 유저: 학년, 다니는 학교, 다니는 학원 수집
    GRADE_CHOICES = (
        ('elementary', '초등학생'),
        ('middle', '중학생'),
        ('high', '고등학생'),
    )
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES)
    academy = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

class AdultProfile(Profile): # 성인 유저: 학부모와 학부모가 아닌 일반 성인으로 분류 학부모라면 자녀정보 저장, 일반 성인이면 어떤 분야를 찾는지, 다니는 학교 정보 수집
    is_parent = models.BooleanField(default=False)
    looking_for_academy = models.CharField(max_length=100, blank=True, null=True)
    school_info = models.CharField(max_length=100, blank=True, null=True)

class ChildInfo(models.Model): # 학부모 유저일 때 자녀정보 수집
    parent = models.ForeignKey(AdultProfile, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=(('male', '남성'), ('female', '여성')))
    grade = models.CharField(max_length=10, choices=StudentProfile.GRADE_CHOICES)
    academy = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

class InstructorProfile(Profile): # 강사 유저 : 경력 or 경험
    experience = models.TextField()

class AcademyAdminProfile(Profile): # 학원관리자 : 학원 이미지, 학원 이름, 분야, 주소, 전화번호, 정원, 한 반에 수용인원, 기숙사여부, 수강료, 강사수, 학원 이벤트(수강료 할인 등) 정보 수집
    academy_image = models.ImageField(upload_to='media/academy_images/%Y/%m/%d', default='academy_images/no_image.png')
    academy_name = models.CharField(max_length=100)
    field = models.CharField(max_length=50)
    academy_address = models.CharField(max_length=100)
    academy_phone = models.CharField(max_length=20)
    total_capacity = models.IntegerField()
    has_dormitory = models.BooleanField(default=False)
    tuition = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_instructors = models.IntegerField()
    events = models.TextField(blank=True, null=True)
    class_capacity = models.IntegerField()
