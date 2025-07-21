import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x tmk')
    os.system('./tmk')
elif bit == '32bit':
    os.system('chmod +x tmk32')
    os.system('./tmk32')
else:
    print('device not supported')
