from django.contrib.gis.db import models


class Airport(models.Model):
    c28_001 = models.CharField(verbose_name="行政区域コード", max_length=5)
    c28_003 = models.BigIntegerField(verbose_name="種別")
    c28_004 = models.CharField(verbose_name="供用中・建設中の区別", max_length=6)
    c28_005 = models.CharField(verbose_name="名称", max_length=22)
    c28_006 = models.BigIntegerField(verbose_name="設置者")
    c28_007 = models.BigIntegerField(verbose_name="管理者")
    c28_008 = models.CharField(verbose_name="特定飛行場の指定状況", max_length=126)
    c28_009 = models.CharField(verbose_name="運用時間（開始）", max_length=4)
    c28_010 = models.CharField(verbose_name="運用時間（終了）", max_length=4)
    c28_011 = models.BigIntegerField(verbose_name="定期便の有無")
    c28_012 = models.CharField(verbose_name="滑走路延長", max_length=19)
    c28_013 = models.CharField(verbose_name="滑走路幅", max_length=11)
    c28_101 = models.CharField(verbose_name="標点", max_length=11,  blank=True, null=True)
    c28_102 = models.CharField(verbose_name="ターミナルビル", max_length=11, blank=True, null=True)
    c28_103 = models.CharField(verbose_name="調査内容", max_length=254, blank=True, null=True)
    c28_104 = models.CharField(verbose_name="調査内容（続き）", max_length=254, blank=True, null=True)
    c28_000 = models.CharField(verbose_name="空港ID", max_length=13, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.c28_005


class AdminiBoundary(models.Model):
    n03_001 = models.CharField(verbose_name="都道府県明", max_length=10)
    n03_002 = models.CharField(verbose_name="支庁・振興局名", max_length=20, null=True)
    n03_003 = models.CharField(verbose_name="郡・政令都市名", max_length=20, null=True)
    n03_004 = models.CharField(verbose_name="市区町村名", max_length=20, null=True)
    n03_007 = models.CharField(verbose_name="行政区域コード", max_length=5, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.n03_004 is not None:
            return self.n03_004
        if self.n03_003 is not None:
            return self.n03_003
        if self.n03_002 is not None:
            return self.n03_002
        if self.n03_001 is not None:
            return self.n03_001