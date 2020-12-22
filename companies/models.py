from django.db import models


class Company(models.Model):
    """
    Class that describes companies.
    """

    # setting up choices of company's area of activity
    finance = "Finance"
    marketing = "Marketing"
    distribution = "Distribution"
    production = "Production"
    unknown = "Unknown"
    AREA_CHOICES = (
        (finance, "Finance"),
        (marketing, "Marketing"),
        (distribution, "Distribution"),
        (production, "Production"),
        (unknown, "Unknown"),
    )

    # description of the model
    name = models.CharField(max_length=200, db_index=True)
    country = models.CharField(max_length=200)
    foundation = models.DateField()
    area = models.CharField(max_length=200, choices=AREA_CHOICES, default=unknown)

    def __str__(self):
        return self.name