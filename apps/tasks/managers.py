from django.db.models import QuerySet, Q


class TaskQuerySet(QuerySet):

    def closed(self):
        return self.filter(statue__in=('t', 'c'))

    def opened(self):
        return self.filter(~Q(statue__in=('t', 'c')))
