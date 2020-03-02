import os

print(dir(os))

print(os.getcwd())
os.chdir('C:\\Users\\one-mapo\\Desktop')
print(os.getcwd())
print(os.listdir())
# os.mkdir('test_dir_mkdir')
# os.mkdir('test_dir_mkdir\\test_sub_dir')
# os.makedirs('test_dir_make\\test_sub_dir')
# os.rmdir('test_dir_mkdir\\test_sub_dir')
# os.removedirs('test_dir_make\\test_sub_dir')
# os.rename('drk.txt', 'drk_renamed.txt')

os.stat('drk.txt')
print(os.stat('drk.txt').st_size)

from datetime import datetime
modified_time = os.stat('drk.txt').st_mtime
print(datetime.fromtimestamp(modified_time))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print('path: ', dirpath)
#     print('dirs: ', dirnames)
#     print('files: ', filenames)
#     print()

home_path = os.environ.get('HOMEPATH')
file_name = 'test.txt'
print(os.path.join(home_path, file_name))

print(os.path.basename('lala/haha/test.txt'))
print(os.path.basename('lala\\haha\\test.txt'))
print(os.path.dirname('lala/haha/test.txt'))
print(os.path.split('lala/haha/test.txt'))
print(os.path.exists('lala/haha/test.txt'))
print(os.path.exists('C:\\Users\\one-mapo'))
print(os.path.isdir('C:\\Users\\one-mapo'))
print(os.path.isfile('C:\\Users\\one-mapo'))
print(os.path.splitext('C:\\Users\\one-mapo\\test.txt'))

print(dir(os.path))