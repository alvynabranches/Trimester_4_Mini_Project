import subprocess
m = input('Enter the commit message: ')

r = 'origin'
b = 'master'

subprocess.call(['git', 'pull', r, b])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', m])
subprocess.call(['git', 'push', r, b])