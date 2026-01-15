class Student(models.Model):
    name = models.Charfield()
    age = models.IntegerField()

    student = Student.objects.all()