from django.db import models
from tinymce.models import HTMLField
from django.conf import settings
from django.core.validators import FileExtensionValidator


def user_directory_path(instance, filename):
    print("Contents : 사용자 ID", instance.userFK.id)
    print("Contents : 콘텐츠 타입", instance.contentType)
    print("Contents : 파일명", filename)

    return 'contents/UID-{0}/{1}/{2}'.format(instance.userFK.id, instance.contentType, filename)


class Contents(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    lastEditDate = models.DateTimeField(auto_now=True)
    is_Accepted = models.BooleanField(default=True)
    contentType = models.CharField(max_length=3, null=True)
    hits = models.DecimalField(max_digits=11, decimal_places=0, default=0, null=True)   # 조회수
    likes = models.DecimalField(max_digits=11, decimal_places=0, default=0, null=True)   # 좋아요수

    # 특정 확장자만 허용
    # https://sundries-in-myidea.tistory.com/85
    # 메인화면으로 REDIRECT는 함, db에 저장되지않음, 확장자 검사는 HTML에서해야할 듯
    upload_file = models.FileField(null=True, upload_to=user_directory_path, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4'])])

    theme_id = models.ForeignKey("Theme", related_name="contents", on_delete=models.CASCADE, db_column="theme_id",
                                 null=True, blank=True)

    userFK = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userFK", null=False)

    def __str__(self):
        return self.title


class Contents_Description(models.Model):
    id = models.AutoField(primary_key=True)
    description = HTMLField()
    width = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    HVType = models.CharField(max_length=10, null=True)  # 가로형 세로형 horizontal, vertical
    thumbnailPath = models.CharField(max_length=200, null=True)
    contentFK = models.ForeignKey(Contents, on_delete=models.CASCADE, db_column="contentsFK", null=True, blank=True)


class Theme(models.Model):
    # CHOICE = (('문화/관광', '문화/관광'), ('스포츠/레저', '스포츠/레저'), ('공예', '공예'), ('연예', '연예'), ('놀이','놀이'))

    id = models.AutoField(primary_key=True)
    # themeValue = models.CharField(max_length=100, choices=CHOICE, null=True, default="")
    themeValue = models.CharField(max_length=100, null=True, default="")

    def __str__(self):
        return self.themeValue


class Detail_Theme(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, null=False)
    theme_id = models.ForeignKey("Theme", related_name="Detail_Theme", on_delete=models.CASCADE, db_column="theme_id")


class Content_Like(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    contents_id = models.ForeignKey("Contents", related_name="Content_Like", on_delete=models.CASCADE,
                                    db_column="contents_id")
    userFK = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userFK", null=False)


class Content_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    contents_id = models.ForeignKey("Contents", related_name="Content_Comment", on_delete=models.CASCADE,
                                    db_column="contents_id")
    userFK = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userFK", null=False)
