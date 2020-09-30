import subprocess, socket
if socket.gethostbyname(socket.gethostname()) != '127.0.0.1':
    m, r, b = input('Enter the commit message: '), 'origin', 'master'

    subprocess.call(['git', 'pull', r, b])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', m])
    subprocess.call(['git', 'push', r, b])