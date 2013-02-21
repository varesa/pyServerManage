from subprocess import call, Popen, PIPE
import logging, logging.handlers

#log = logging.getLogger("serverAPI")
#log.setLevel(logging.DEBUG)
#log.addHandler(logging.FileHandler("/tmp/serverAPI.log"))

def start(name, path, cmd):
	_create_screen(name)
	_send_cmd(name, "cd " + path + "; exec " + cmd)

def stop(name):
	_send_cmd(name,'stop')
	
def status(name):
	if _does_exist(name):
	    if _is_running(name):
		return 1
	    else:
		return 0
	else:
	    return -1



def _does_exist(name):
	return True # TODO: IMPLEMENT

def _is_running(name):
	screens = Popen(['screen', '-list'],stdout=PIPE).communicate()[0]
	if '.mc_' + name + '\t(' in screens:
	    return True
	else:
	    return False

def _create_screen(name):
	cmd="/usr/bin/screen -dmS mc_"+name
	call(cmd,shell=True)


def _send_cmd(name, command):
	cmd = "/usr/bin/screen -S mc_"+name + ' -p0 -X stuff "' + command + '\n"' + '\n'
	#log.debug(cmd)
	call(cmd,shell=True)

def new_server(name, port, path):
#CREATE DIR
#CREATE CONFIG
#COPY server.jar

    config = """
    #Minecraft server properties
    #Created by server-management tool by Esa Varemo
    allow-nether=true
    level-name=world
    enable-query=false
    allow-flight=false
    server-port={conf_port}
    level-type=DEFAULT
    enable-rcon=false
    level-seed=
    server-ip=
    max-build-height=256
    spawn-npcs=true
    white-list=false
    spawn-animals=true
    online-mode=true
    pvp=true
    difficulty=1
    gamemode=0
    max-players=20
    spawn-monsters=true
    generate-structures=true
    view-distance=10
    motd=A Minecraft Server
    """.format(conf_port=port)

#WRITE CONFIG