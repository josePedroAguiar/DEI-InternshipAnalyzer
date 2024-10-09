def platform_info(request):
    links = {}
    platform_name = None
    with open('platform.txt', 'r') as file:
        for line in file:
            if not line.startswith('#'):
                key, value = line.split('=')
                key = key.strip()
                value = value.strip().replace("'", "").replace('"', '')
                if key == 'Platform Name':
                    platform_name = value
                elif key.endswith('Link'):

                    links[ key.split(' ')[0].lower()] = value
    return {'platform_name': platform_name, 'links': links}
