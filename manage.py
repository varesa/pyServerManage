from subprocess import call, Popen, PIPE

def start(name):
	startcmd="ls"
	cmd="/usr/bin/screen -dmS " + name + " ; /usr/bin/screen -S " + name + ' -p0 -X stuff "' + startcmd + '"\n'

	call(cmd,shell=True)

def stop(name):
	stopcommand=""
	cmd="/usr/bin/screen -S " + name + ' -p0 -X stuff "' + stopcmd + '"\n'

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
	pass

def _send_cmd(name, cmd):
	pass