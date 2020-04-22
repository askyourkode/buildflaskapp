def print_manual():
    print('Usage: build-flask-app [app_name] -[arguments]\n')

    print('Options and arguments available for creating flask apps:')
    print('  -d or --debugger \n\t Enables debugger mode on')
    print('  -cj or --css-js \n\t Import stylesheet and script tag')
    print('  -bs or --bootstrap \n\t Import bootstrap')
    print('  -jq or --jQuery \n\t Import jQuery')
    print('  -gsap or --gsap \n\tImport Gsap')
    print('  -fa or --font-awesome \n\tImport Font awesome')
    print('  -dc or --docker-container \n\t Generate Dockerfile and docker-compose.yml\n')
    print('  -h or --help \n\t Print help')
    print('  -v or --version \n\t Print version\n')
    print('Example: build-flask-app hello-world -d -bs\n')