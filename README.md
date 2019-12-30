## Flask App Generator

A script that generates a hello world app in Python's flask with proper directory structure that you can modify to build your app.

### How to use
1. $ python3 create-flask-app.py {app_name}
2. cd {app_name}
3. python3 app.py
4. open up http://localhost:5000 :)
Ensure that you have flask installed, or else it will not work! You can install flask using _pip install flask_.

![](create-flask-app.gif)

### Add to path(Optional)
1. cp create-flask-app.py /usr/local/bin/
2. chmod +x /usr/local/bin/create-flask-app.py
3. You should now be able to run create-flask-app.py from any directory :)

### Options to pass as Arguments
- python3 create-flask-app.py {app_name} **-dB** --> enable debug mode on app.py
- python3 create-flask-app.py {app_name} **-sS** --> import style.css and app.js automatically
- python3 create-flask-app.py {app_name} **-dC** --> docker-compose up -d

### Coming features
- [ ] Manual(man create-flask-app)
- [x] Debug option on (-dB)
- [x] Include Stylesheet and Script (-Ss)
- [x] Push app to docker container (-dC)
