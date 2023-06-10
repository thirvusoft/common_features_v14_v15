from common_features_v14.common_features_v14.utils.custom_field.custom_fields import custom_field
from common_features_v14.common_features_v14.utils.custom_field.todo.todo import todo

def after_install():
    custom_field()
    todo()