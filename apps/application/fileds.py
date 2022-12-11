from django.db import models


class AppDecimalField(models.DecimalField):

    def __init__(self, *args, **kwargs) -> None:
        self.decimal_places = 3
        self.max_digits = 30
        self.default = 0.0
        super(models.DecimalField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["decimal_places"]
        del kwargs["max_digits"]

        return name, path, args, kwargs


class DecimalField(models.DecimalField):

    def __init__(self, *args, **kwargs) -> None:
        self.decimal_places = 3
        self.max_digits = 30
        self.default = 0.0
        super(models.DecimalField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["decimal_places"]
        del kwargs["max_digits"]

        return name, path, args, kwargs