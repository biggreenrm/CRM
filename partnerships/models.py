from django.db import models
from companies.models import Company


class Partnership(models.Model):
    """
    Class which describes relations between different companies.
    """

    company1 = models.ForeignKey(Company, related_name="company1")
    company2 = models.ForeignKey(Company, related_name="company2")
    start_date = models.DateField()