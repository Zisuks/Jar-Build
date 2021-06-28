import requests, json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
nameid = "Zisuks"
repoid = "Jar-Build"
yamlid = "build"
f = open("./README.md", "w")
f.write(f'''

<a href="https://github.com/{nameid}"><h3 align="center"><b>{nameid}</b></h3></a>

<h3 align="center">Have a nice day!</h3>

<p align="center">

  <a href="https://github.com/{nameid}">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username={nameid}&hide=issues&hide_title=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff" />
   </a>
   
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

[![{yamlid}](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml/badge.svg)](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml)

#### Download This code Here:

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{nameid}/{repoid}?style=for-the-badge&label=Download)](https://github.com/{nameid}/{repoid}/releases) 

</p> 

#### About Me :

```bash

{nameid}

```

''')
f.close()
