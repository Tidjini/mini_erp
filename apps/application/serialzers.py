from rest_framework import serializers


class ModelSerializerMixin(serializers.ModelSerializer):
    def clean_validate_data_keys(self, *keys):
        """Clean Data
        keys: Specific Keys to clean
        Clean extensions fields from validated data to be conform with model fields"""
        for key in keys:
            if key in self._validated_data:
                del self._validated_data[key]

    def clean_validate_data(self):
        """Clean Data, to match  the model fields

        Clean extensions fields from validated data to be conform with model fields"""
        self._validated_data = {
            key: value
            for key, value in self._validated_data.items()
            if key in self.Meta.model.keys()
        }
