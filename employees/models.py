from django.db import models
from companies.models import Company


class Employee(models.Model):
    """
    Class which describes employees working on different companies.
    """

    # describing employee's sex
    male = "Male"
    female = "Female"
    secret = "Secret"
    SEX_CHOICES = (
        (male, "Male"),
        (female, "Female"),
        (secret, "Secret"),
    )

    # describing employee's model
    first_name = models.CharField(max_length=255, blank=False)
    second_name = models.CharField(max_length=255, blank=False)
    position = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    sex = models.CharField(max_length=255, choices=SEX_CHOICES, default=secret)
    salary = models.IntegerField(blank=True)
    date_of_birth = models.DateField(blank=True)
    date_of_hiring = models.DateField(blank=True)
