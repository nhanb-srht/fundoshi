from requests import get


def fake_user_agent(func):
    def func_wrapper(*args, **kwargs):
        headers = kwargs.get('headers', {})
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        })
        kwargs['headers'] = headers
        return func(*args, **kwargs)
    return func_wrapper


# Skeleton site. If a site requires special requests (custom headers, etc.)
# then the site implementation should override these methods.
class BaseSite(object):

    get_manga_seed_page = get
    get_chapter_seed_page = get
    get_page_image = get

    def search_by_author(self, author):
        return []
