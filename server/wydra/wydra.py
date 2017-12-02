#!/usr/bin/env python3.6

from wsgiref.simple_server import make_server

import httputils
import urls
import config


def wydra(environ, start_response):
    """
    WSGI callable.
    """
    http_method = environ['REQUEST_METHOD']
    request_body = environ['wsgi.input']
    content_length = environ['CONTENT_LENGTH']
    content_length = int(content_length) if content_length != '' else 0
    request_body = request_body.peek(content_length) if content_length != 0 else ''
    resource_name, resource_id = httputils.extract_path(environ['PATH_INFO'])
    if 'HTTP_AUTHORIZATION' not in environ:
        start_response('401 UNAUTHORIZED', [('WWW-Authenticate', 'Basic')])
        return [b'authorization needed']
    passphrase = httputils.extract_passphrase(environ['HTTP_AUTHORIZATION'])
    if passphrase != config.magic_key:
        start_response('400 BAD REQUEST', [('Content-Type', 'text/plain')])
        return [b'bad password']
    try:  # good resource name
        ret = urls.mapping[http_method][resource_name](resource_id, request_body)
        start_response('200 OK', [])
    except KeyError:  # bad resource name
        ret = b'Page not found'
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return [ret]


if __name__ == '__main__':
    make_server(host='localhost', port=8080, app=wydra).serve_forever()
