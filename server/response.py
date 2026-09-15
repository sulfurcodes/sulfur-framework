from httpparser import parser

#Builds HTTP responses based on the parsed request
def response(request):
    http_method, path, http_version = parser(request)

    if http_method == 'GET':
        if path == '/':
            file = open('server/1_index.html')
            content = file.read()
            file.close()
            return 'HTTP/1.1 200 OK \n\n' + content
        return 'HTTP/1.1 404 Method Not Found\n\n404 Not Found'
    return 'HTTP/1.1 405 Method Not Allowed\n\nMethod Not Allowed'
            
