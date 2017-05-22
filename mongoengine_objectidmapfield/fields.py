
from bson import ObjectId
from mongoengine.fields import MapField
import six


__all__ = ('ObjectIdMapField')


class ObjectIdMapField(MapField):
    '''Similar to a MongoEngine `MapField`, but where keys are `ObjectId`s instead
    of strings'''

    def validate(self, value):
        """Make sure that a list of valid fields is being used."""
        if not isinstance(value, dict):
            self.error('Only dictionaries may be used as the value for a ObjectIdMapField')

        if not all(map(lambda k: isinstance(k, ObjectId), value.keys())):
            msg = 'Invalid key in `ObjectIdMapField` - keys must be `ObjectId`s.'
            self.error(msg)
        super(MapField, self).validate({str(key): val for key, val in six.iteritems(value)})

    def to_python(self, value):
        '''Convert a MongoDB-compatible type to a Python type.'''
        self.field._auto_dereference = self._auto_dereference
        return {ObjectId(key): self.field.to_python(item) for key, item in value.items()}

    def to_mongo(self, value, use_db_field=True, fields=None):
        return {
            str(key): self.field._to_mongo_safe_call(item, use_db_field, fields)
            for key, item in six.iteritems(value)
        }
