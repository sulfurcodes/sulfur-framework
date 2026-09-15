#Parses the raw HTTP request into useful components
def parser(request):
    headers = request.split('\n')
    first_header_components = headers[0].split(" ")

    http_method = first_header_components[0]
    path = first_header_components[1]
    http_version = first_header_components[2]
    
    return http_method, path, http_version