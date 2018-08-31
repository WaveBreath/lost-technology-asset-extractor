# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:06:09 2018

@author: yiyuezhuo
"""

import os

'''
with open('adelina.png', 'rb') as f:
    data = f.read()
    
head = data[:4]
body = data[4:-0x64]
tail = data[-0x64:]

with open('adelina-decodeed.png', 'wb') as f:
    f.write(tail)
    f.write(body)
'''

def decode(source, dest):
    with open(source, 'rb') as f:
        data = f.read()
        
    head = data[:4]
    body = data[4:-0x64]
    tail = data[-0x64:]
    
    with open(dest, 'wb') as f:
        f.write(tail)
        f.write(body)
        
def decode_map(source_dir, dest_dir, relative_dir=None, verbose=True):
    if relative_dir is None:
        source_root = source_dir
        dest_root = dest_dir
    else:
        source_root = os.path.join(source_dir, relative_dir)
        dest_root = os.path.join(dest_dir, relative_dir)
    is_decode_any = False
    for name in os.listdir(source_root):
        source_path = os.path.join(source_root, name)
        dest_path = os.path.join(dest_root, name)
        if os.path.isdir(source_path):
            os.makedirs(dest_path, exist_ok=True)
            if relative_dir is None:
                res = decode_map(source_dir, dest_dir, name)
            else:
                res = decode_map(source_dir, dest_dir, os.path.join(relative_dir,name))
            if not res:
                os.rmdir(dest_path)
        elif name.endswith('.png'):
            decode(source_path, dest_path)
            is_decode_any = True
            if verbose:
                print(f'{source_path} -> {dest_path}')
    return is_decode_any