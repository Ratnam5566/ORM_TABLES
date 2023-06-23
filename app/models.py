from django.db import models

# Create your models here.
class Dept(models.Model):
    Dname = models.CharField(max_length=100)
    Deptno= models.IntegerField()
    Loc= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Dname

class Emp(models.Model):
    Eno=models.IntegerField()
    Ename=models.CharField(max_length=100)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Ename