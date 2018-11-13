# -*- coding: utf-8 -*-

#폴더 내 각각의 .json파일에 대괄호로 묶기.
import os
import glob

path = '/Users/ck/Desktop/aaa/'
extension = 'json'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]

for file in result:
    open_file = open(file,'r')
    read_file = open_file.read()
    new_content = "[" + read_file + "]"
    write_file = open(file,'w')
    write_file.write(new_content)
    write_file.close()