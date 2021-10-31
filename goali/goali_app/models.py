from django.db import models


class Goal(models.Model):
    name = models.TextField()
    description = models.TextField()
    # STATUS_CHOICES = [
    #         ('NS', 'Not started'),
    #         ('PS', 'Planning stage'),
    #         ('IP', 'In progress'),
    #         ('OG', 'Ongoing'),
    #         ('AD', 'Almost Done'),
    #         ('CO', 'Completed')
    # ]
    # status = models.CharField(
    #         max_length=2,
    #         choices=STATUS_CHOICES,
    #         default=STATUS_CHOICES[0],
    # )
