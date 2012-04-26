from subprocess import call, Popen, PIPE

def start(name):
	startcmd="ls"
	_create_screen(name)
	_send_cmd(name, startcmd)

def stop(name):
	stopcmd=""
	_send_command(name,stopcmd)
	
def status(name):
	if _does_exist(name):
	    if _is_running(name):
		return 1
	    else:
		return 0
	else:
	    return -1



def _does_exist(name):
	pass

def _is_running(name):
	screens = Popen(['screen', '-list'],stdout=PIPE).communicate()[0]
	if '.' + name + '\t(' in screens:
	    return True
	else:
	    return False

def _create_screen(name):
	cmd="/usr/bin/screen -dmS " + name
	call(cmd,shell=True)


def _send_cmd(name, command):
	cmd = "/usr/bin/screen -S " + name + ' -p0 -X stuff "' + command + '"\n'
	call(cmd,shell=True)