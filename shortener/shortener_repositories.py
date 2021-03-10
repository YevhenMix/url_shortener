import string
from random import choices

import clipboard

from .models import Link


def create_short_link():
    chars = string.digits + string.ascii_letters
    short_link = ''.join(choices(chars, k=6))

    full_link = Link.objects.filter(short_link=short_link)

    if full_link:
        short_link = create_short_link()

    return short_link


def create_short_link_with_save_in_db(request, full_link, designed_link=None) -> str:
    """
    Created short link and save it into database
    return: short link for view template
    """
    domain_name = request.headers['Referer']

    check_link = Link.objects.filter(full_link=full_link).first()

    if check_link:
        designed_link = check_link.designed_link
        short_link = check_link.short_link
        return domain_name + (designed_link or short_link)

    if designed_link:
        short_link = designed_link
        create_link_in_db = Link(full_link=full_link, designed_link=short_link)
        create_link_in_db.save()
    else:
        short_link = create_short_link()
        create_link_in_db = Link(full_link=full_link, short_link=short_link)
        create_link_in_db.save()
    full_short_link = domain_name + short_link
    return full_short_link


def copied_text(url):
    clipboard.copy(url)
