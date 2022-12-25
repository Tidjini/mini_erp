from django.db.models import QuerySet, Q


class TaskQuerySet(QuerySet):

    def created(self, user):
        # get list for user as creator
        return self.filter(creator=user.id)

    def affected(self, user):
        # get list for user as receiver
        return self.filter(receiver=user.id)

    def user_tasks(self, user, type=None):
        if type is None:
            return self.created(user) | self.affected(user)
        if type == "0":
            return self.created(user)
        return self.affected(user)

    def closed(self):
        return self.filter(statue__in=('t', 'c'))

    def opened(self):
        return self.filter(~Q(statue__in=('t', 'c')))

    def state(self, closed=None):
        # if there is no filter return all
        if closed is None:
            return self

        if closed == '1':
            return self.closed()
        return self.opened()


class TaskLocationQuerySet(QuerySet):

    def location_task(self, task_id):
        # get list for user as creator
        return self.filter(task=task_id)
