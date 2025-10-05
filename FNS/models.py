from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=50)
    coordinator_contact = models.CharField(max_length=20)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )
    disciplines = models.TextField(help_text="Enter disciplines separated by commas")

    def __str__(self):
        return f"{self.code} - {self.name}"

    def disciplines_list(self):
        return [d.strip() for d in self.disciplines.split(",")]


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    degree = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )

    def __str__(self):
        return self.name


class HomePage(models.Model):
    title = models.CharField(max_length=100, default="Faculty of Natural Sciences")
    description = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.title
