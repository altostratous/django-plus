from django_plus.fa import fa_timedelta
from ._generator_ import admin_field_generator


def timedelta(verbose_name="", path_to_field=None, wrap_white_space=True):

    def function_changer(func, admin, instance):

        result_timedelta = func(admin, instance)
        if result_timedelta:
            return fa_timedelta(result_timedelta)
        else:
            return ""

    return admin_field_generator(
        verbose_name=verbose_name,
        path_to_field=path_to_field,
        function_changer=function_changer,
        wrap_white_space=wrap_white_space
    )

