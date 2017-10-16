from wsgiref.simple_server import make_server

import httputils

def wydra(environ, start_response):
    """ WSGI callable. """
    start_response('200 OK', [('Content-Type', 'text/plain')])
    ret = []
    resource_name, resource_id = httputils.extract_path(environ['PATH_INFO'])
    for key in environ:
        ret.append(bytes(f"{key}: {environ[key]}\n", 'utf-8'))
    ret.append(bytes(resource_name, 'utf-8'))
    ret.append(bytes(resource_id, 'utf-8'))
    return ret

if __name__ == '__main__':
    print(httputils.extract_path("/path/1234"))
    make_server(host='localhost', port=8080, app=wydra).serve_forever()
