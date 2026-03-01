MAX_LENGTH = 255


def parse_url(url):
    if len(url) > MAX_LENGTH:
        raise ValueError("URL too long")
    scheme, _, rest = url.partition("://")
    host, _, path = rest.partition("/")
    return {"scheme": scheme, "host": host, "path": "/" + path}


def parse_query(query):
    return dict(pair.split("=", 1) for pair in query.split("&") if "=" in pair)
