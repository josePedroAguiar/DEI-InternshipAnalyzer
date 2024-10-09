def platform_name(request):
    with open('platform.txt', 'r') as file:
        for line in file:
            if not line.startswith('#') and line.startswith('Platform Name'):
                platform_name = line.split('=')[1].strip()
                platform_name = platform_name.replace("'", "").replace('"', '')
                break
    return {'platform_name': platform_name}