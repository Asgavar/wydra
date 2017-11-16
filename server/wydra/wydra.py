from wsgiref.simple_server import make_server

import httputils
import urls


def wydra(environ, start_response):
    """
    WSGI callable.
    """
    http_method = environ['REQUEST_METHOD']
    request_body = environ['wsgi.input']
    resource_name, resource_id = httputils.extract_path(environ['PATH_INFO'])
    if not 'HTTP_AUTHORIZATION' in environ:
        start_response('401 UNAUTHORIZED', [('WWW-Authenticate', 'Basic')])
        return [b'authorization needed']
    try:  # good resource name
        ret = urls.mapping[http_method][resource_name](resource_id, request_body)
        start_response('200 OK', [])
    except KeyError:  # bad resource name
        ret = b'Page not found'
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return [ret]


if __name__ == '__main__':
    make_server(host='localhost', port=8080, app=wydra).serve_forever()
