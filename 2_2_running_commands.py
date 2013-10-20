import subprocess
subprocess.call(["ls", "-l"])

subprocess.call(['softwareupdate', '-l'])

command = ['/usr/sbin/softwareupdate', '-l']
proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error_output) = proc.communicate()
print "Output:", output
print "Error output:", error_output
print "Return code:", proc.returncode

# don't run this one!
subprocess.call(['/sbin/shutdown', '-r', 'now'])
