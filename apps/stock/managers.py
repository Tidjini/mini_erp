from django.db.models import QuerySet


class ProductQuerySet(QuerySet):

    def raw_materials(self):
        return self.filter(type='RM')

    def finals(self):
        return self.filter(type='FP')

    def semi_finished(self):
        return self.filter(type='SFP')

    def services(self):
        return self.filter(type='S')
