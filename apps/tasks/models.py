from random import randint

from django.db import models
from django.utils import timezone

from apps.application import colors
from apps.general.models import Profile
from . import managers


def generate_colors():
    fore = randint(0, 5)
    back = randint(0, 5)
    if fore < back:
        return colors.lights[fore], colors.darks[back]
    return colors.darks[fore], colors.lights[back]


class Task(models.Model):

    STATUES = (
        ('i', 'instance'),
        ('a', 'accepted'),
        ('p', 'in progress'),
        # the finished status
        ('t', 'terminated'),
        ('c', 'canceled')
    )
    creator = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='created_tasks')
    receiver = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True,
        related_name='tasks')

    statue = models.CharField(max_length=1, choices=STATUES, default='i')

    label = models.CharField(max_length=255)

    # set color generator return a Tuple (fore, back) for Caption of task
    forecolor = models.CharField(max_length=10, null=True)
    backcolor = models.CharField(max_length=10, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    finished_at = models.DateTimeField(null=True)

    objects = managers.TaskQuerySet.as_manager()

    @property
    def caption(self):
        cap = self.label[:2]
        return cap.upper() if cap else 'ND'

    @property
    def statue_label(self):
        state = list(filter(lambda s: s[0] == self.statue, self.STATUES))[0]
        return state[1].title()

    @property
    def closed(self):
        return self.statue in ('t', 'c')

    @property
    def receiver_name(self):
        return self.receiver.name if self.receiver else None

    @property
    def creator_name(self):
        return self.creator.name

    @property
    def created_date(self):
        return self.created_at.strftime('%d/%m/%Y')

    @property
    def created_time(self):
        return self.created_at.strftime('%H:%M')

    @property
    def has_location(self):
        return self.paths and len(self.paths.all()) > 0

    def save(self, *args, **kwargs):
        if self.id is None:
            f, b = generate_colors()
            self.forecolor = f
            self.backcolor = b

        if self.statue in ('t', 'c'):
            self.finished_at = timezone.now()

        return super(Task, self).save(*args, **kwargs)

    def finish(self):
        if self.statue in ('t', 'c'):
            self.finished_at = timezone.now()
            # todo notify the user - creator
            # todo later notify the specific user
        return self.save()

    def finish_with_statue(self, statue):
        self.statue = statue
        return self.finish()


class TaskLocation(models.Model):
    # task can have multiple paths, and locations
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='paths')
    origin_lat = models.DecimalField(
        max_digits=50, decimal_places=20, null=True)
    origin_lng = models.DecimalField(
        max_digits=50, decimal_places=20, null=True)
    destination_lat = models.DecimalField(
        max_digits=50, decimal_places=20, null=True)
    destination_lng = models.DecimalField(
        max_digits=50, decimal_places=20, null=True)

    origin_address = models.TextField()
    destination_address = models.TextField()
    distance = models.DecimalField(max_digits=50, decimal_places=20, null=True)
    duration = models.DecimalField(max_digits=50, decimal_places=20, null=True)

    @property
    def humain_distance(self):
        km = self.distance // 1000
        return f'{km} KM'

    @property
    def humain_duration(self):

        minutes = self.duration // 60
        hours = minutes // 60
        minutes = minutes % 60
        days = hours // 24
        hours = hours % 24

        result = f'{days} jour(s) ' if days else ''
        result += f'{hours} heure(s) ' if hours else ''
        result += f'{minutes} min(s) ' if minutes else ''

        return result

    objects = managers.TaskLocationQuerySet.as_manager()

    # todo later dynamiclay by google, time and distance (short)


class TaskAttachement(models.Model):
    # task can have multiple attachements
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_docs')
    file = models.FileField(null=True)
