import os
import time

# source列表中: 1所要复制的文件夹,单引号下用双引号括住(在解析为字符串时用)， 2所在目录
source = ['"C:\\data\\db"', 'C:\\data']
target_dir = 'C:\\backup'

# os.sep根据操作系统给出路径分割符，时间的格式大小写是固定的
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# -qr快速执行，并包含子目录 后面跟上文件 + 目录
# join方法的目的是将列表转为字符串
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')
