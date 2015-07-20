#!/usr/bin/python
import subprocess, signal, os
p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():
	if 'python2.6 outlookmail.py' in line:
		pid = int(line.split(None, 1)[0])
		os.kill(pid, signal.SIGKILL)

for line in out.splitlines():
	if './start.sh' in line:
		pid = int(line.split(None, 1)[0])
		os.kill(pid, signal.SIGKILL)
