from inspect import isclass


class ModelSerializerTest:
    class FieldNameError(Exception):
        def __init__(self, message=None):
            self.message = message

    class UnexpectedError(Exception):
        def __init__(self, message=None):
            self.message = message

    class FieldDoesNotMatch(Exception):
        def __init__(self, message=None):
            self.message = message

    @classmethod
    def get_model_name_ls(cls, app):
        model_name_ls = []
        for x in dir(app.models):
            app_class = getattr(app.models, x)
            if not isclass(app_class):
                continue
            if getattr(app_class, '_meta', None) is None:
                continue
            app_name = app.__path__[0].split('/')[-1]
            if not app_class._meta.app_label == app_name:
                continue
            if app_class._meta.abstract == True:
                continue
            model_name_ls.append(x)

        return model_name_ls

    @classmethod
    def test_model_serializer(cls, app, model_name_ls):

        for model_name in model_name_ls:

            try:
                model_class = getattr(app.models, model_name, None)
                serializer_class = getattr(app.serializers.basic_serializer, f'{model_name}Serializer', None)

                instances = model_class.objects.all()[:10]
                serializer = serializer_class(instances, many=True)
                try:
                    serializer.data
                except Exception as e:
                    raise cls.FieldNameError(message=f'{model_name}Serializer FieldNameError: {e}')

                model_fields = [f.name for f in filter(lambda f: f.related_model is None, \
                                                       [f for f in model_class._meta.get_fields()])]
                serializer_fields = serializer_class.Meta.fields

                if set(model_fields) != set(serializer_fields):
                    diff_at_model = set(model_fields).difference(set(serializer_fields))
                    diff_at_serializer = set(serializer_fields).difference(set(model_fields))
                    raise cls.FieldDoesNotMatch(f'{model_name} model, serializer 간의 필드가 맞지 않음 \n    model: ',
                                                diff_at_model, '\n    serializer', diff_at_serializer)
            except Exception as e:
                raise cls.UnexpectedError(model_name, e)
