from django.db import models

# Create your models here.

Region=[
    ('1','中国大陆'),
    ('2','中国香港'),
    ('3','中国台湾'),
    ('4','美国'),
    ('5','韩国'),
    ('6','日本'),
    ('7','其他'),

]

Quality=[
    (1,'720p'),
    (2,'1080p'),
    (3,'4k'),
]

Hot=[
    (False,'否'),
    (True,'是')
]

Top=[
    (False,'否'),
    (True,'是')
]
Show=[
    (False,'否'),
    (True,'是')
]
Free=[
    (False,'否'),
    (True,'是')
]


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name=models.CharField(verbose_name='分类名',max_length=30)

    class Meta:
        db_table='category'
        verbose_name='分类管理'
        verbose_name_plural='分类管理'
    
    def __str__(self):
        return self.category_name

class Movie(models.Model):
    id=models.AutoField(primary_key=True)
    movie_name=models.CharField(verbose_name='电影名称',max_length=100)
    release_year=models.IntegerField(verbose_name='上映年份')
    director=models.CharField(verbose_name='导演',max_length=100)
    scriptwriter=models.CharField(verbose_name='编剧',max_length=100)
    actors=models.CharField(verbose_name='演员',max_length=200)
    region=models.CharField(verbose_name='地区',choices=Region,max_length=100)
    types=models.CharField(verbose_name='类型',max_length=50)
    language=models.CharField(verbose_name='语言',max_length=100)
    release_date=models.DateField(verbose_name='上映日期')
    duration=models.CharField(verbose_name='时长(集数)',max_length=50)
    alternate_name=models.CharField(verbose_name='又名',max_length=100,blank=True,null=True)
    image_url=models.CharField(verbose_name='图片链接',max_length=300,blank=True)
    rate=models.FloatField(verbose_name='评分',blank=True)
    review=models.TextField(verbose_name='简介',max_length=500,blank=True)
    is_hot=models.BooleanField(verbose_name='是否热门',default=False,choices=Hot)
    is_top=models.BooleanField(verbose_name='是否置顶',default=False,choices=Top)
    quality=models.SmallIntegerField(verbose_name='清晰度',choices=Quality,blank=True)
    subtitle=models.CharField(verbose_name='字幕',blank=True,max_length=400)
    update_info=models.CharField(verbose_name='更新信息',blank=True,max_length=200)
    update_progress=models.CharField(verbose_name='更新情况',blank=True,max_length=200)

    download_info=models.CharField(verbose_name='网盘信息',blank=True,max_length=500)
    is_show=models.BooleanField(verbose_name='是否展示',default=True,choices=Show)
    is_free=models.BooleanField(verbose_name='是否免费',default=True,choices=Free)

    category=models.ForeignKey(Category,blank=False,verbose_name='分类名',on_delete=models.CASCADE)

    class Meta:
        db_table='movie'
        verbose_name='电影管理'
        verbose_name_plural='电影管理'

    def __str__(self):
        return self.movie_name