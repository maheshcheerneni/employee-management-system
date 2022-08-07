from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name






class Role(models.Model):
    role_name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.role_name





class Employee(models.Model):
    emp_id=models.IntegerField(null=False)
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    email=models.EmailField()
    salary=models.CharField(max_length=100,null=False)
    bonus=models.CharField(max_length=100,null=False)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)


    def __str__(self):
        return "%s   %s    %s" %(self.emp_id,self.first_name,self.last_name)


