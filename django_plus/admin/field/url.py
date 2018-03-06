from ._generator_ import admin_field_generator
from django_plus.admin.html_tags import anchor_tag


def url(verbose_name="", title=None, path_to_field=None, limit=-1, wrap_white_space=True):
    """
    Function should return a url link
    :param verbose_name:
    :param title: url title. if not presented we use the link as title as well
    :param path_to_field:
    """
    def function_changer(func, admin, instance):
        link = func(admin, instance)

        if not link.startswith('http://') and not link.startswith('https://'):
            link = 'http://' + link

        if title is None:
            url_title = link.replace('https://', '').replace('http://', '')
            if url_title.endswith('/'):
                url_title = url_title[:-1]
        else:
            url_title = title

        if limit >= 0 and len(url_title) > limit:
            url_title = url_title[:limit] + '...'

        return anchor_tag(url_title, link, target='_blank')

    return admin_field_generator(
        verbose_name=verbose_name,
        html=True,
        boolean=False,
        path_to_field=path_to_field,
        function_changer=function_changer,
        wrap_white_space=wrap_white_space
    )
