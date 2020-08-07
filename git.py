import subprocess
m = input('Enter the commit message: ')

repo = 'origin'
branch = 'master'

# subprocess.call(['git', 'pull', repo, branch])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', m])
subprocess.call(['git', 'push', repo, branch])