import os
import time

source_url = input('enter a source_url here:')
source = [source_url]

target_dir = input('enter a target dir here:')

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('enter a comment here:')
if len(comment) == 0:   # 如果没有添加备注时，默认
    target = today + os.sep + now + '.zip'
else:                   # 添加备注的话，在文件名中加入备注信息
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created dict')
else:
    print(today, 'had presented')

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('successfully backup to', target)
else:
    print('backup failed')

