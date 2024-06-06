from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    titles = models.IntegerField(default=0, null=True, blank=True)
    top_scorer = models.CharField(max_length=50, null=False, blank=False)
    fifa_code = models.CharField(max_length=3, unique=True, null=False, blank=False)
    first_cup = models.DateField(null=True, blank=True)

    def __repr__(self):
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"
