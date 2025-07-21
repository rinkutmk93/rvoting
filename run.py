import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x tbg')
    os.system('./tbg')
elif bit == '32bit':
    os.system('chmod +x tbg32')
    os.system('./tbg32')
else:
    print('device not supported')
