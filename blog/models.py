from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    REQUIREMENT_TYPES = (
        ('N', "New Requirement"),
        ('E', "Enhancement"),
        ('R', "Roll Out"),
        ('T', "Training"),
    )
    PRIORITASS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    TARGETS = (
        ('1', 'TW-I'),
        ('2', 'TW-II'),
        ('3', 'TW-III'),
        ('4', 'TW-IV'),
    )
    DIR_APS = (
        ('CON', 'Controller'),
        ('DEV', 'Development'),
        ('FIN', 'Finance & Treasury'),
        ('HR', 'HR-GA'),
        ('ICT', 'ICT & DM'),
        ('AUDIT', 'Internal Audit'),
        ('LEGAL', 'Legal'),
        ('NUN', 'Nunukan'),
        ('ONWJ', "ONWJ"),
        ('OPS', 'Operation & Production'),
        ('PHI', 'PHI'),
        ('PPRM', 'PPRM'),
        ('QHSSE', 'QHSSE'),
        ('REL', 'Relation'),
        ('SCM', 'SCM'),
        ('SK', 'Siak-Kampar'),
        ('CO', 'Commercial'),
        ('WMO', 'WMO'),
    )
    user1 = models.CharField(max_length=15)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dir_ap = models.CharField(max_length=5, choices=DIR_APS)
    requirement = models.TextField()
    requirement_type = models.CharField(max_length=1, choices=REQUIREMENT_TYPES)
    prioritas = models.CharField(max_length=1, choices=PRIORITASS)
    target = models.CharField(max_length=1, choices=TARGETS)
    budget = models.IntegerField()

    def __str__(self):
        return self.requirement[:50]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Update(models.Model):
    STATUSS = (
        ('C', 'Closed'),
        ('D', 'Dropped'),
        ('E', 'Execution'),
        ('I', 'Initiation'),
        ('P', 'Planning'),
    )
    posting = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='updates',)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    last_update = models.DateField(auto_now_add=False)
    progress = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUSS)
    status_akhir = models.TextField()

    def __str__(self):
        return self.status_akhir[:50]


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.posting.id)])
