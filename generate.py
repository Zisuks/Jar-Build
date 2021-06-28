import json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
nameid = "Zisuks"
repoid = "Jar-Build"
yamlid = "build"
f = open("./README.md", "w")
f.write(f'''
   
#### This Page Create at:

```bash

{timestr}

```

#### Create By Machine:

```bash

Host Name : {socket.gethostname()}

platform  : {platform.platform()}

Ip Local  : {socket.gethostbyname(socket.gethostname())}

```

#### Download This code Here:

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{nameid}/{repoid}?style=for-the-badge&label=Download)](https://github.com/{nameid}/{repoid}/releases) 

</p> 

#### About Me :

[![{yamlid}](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml/badge.svg)](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml)

```bash

{nameid}

```

''')
f.close()
