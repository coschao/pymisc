#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#

import datetime
import json
import os
import psutil
import random
import time
from itertools import zip_longest
import base64
 
# Encode string data
def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))
 
def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')
 
# Encode binary file data
def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode('utf-8')

def string_to_img(s, filename):
    ''' base64로 인코딩된 문자열(s)과 파일명(filename)을 입력으로 받아 문자열을 파일로 저장한다. '''
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(s))

def binfile_to_b64strfile(srcfilepath):
    if not os.path.exists(srcfilepath):
        raise FileNotFoundError("The file '%s' is NOT found!" %(srcfilepath,))
    if not os.path.isfile(srcfilepath):
        raise FileNotFoundError("The file '%s' is NOT file!" %(srcfilepath,))
    
    sf_dirname = os.path.dirname(srcfilepath)
    print(" The dir. of source file is '%s'." %(sf_dirname,))
    sf_basename = os.path.basename(srcfilepath)
    print(" The basename of source file is '%s'." %(sf_basename,))
    sf_ext = os.path.splitext(srcfilepath)
    print(" The ext[0] of source file is '%s'." %(sf_ext[0],))
    print(" The ext[1] of source file is '%s'." %(sf_ext[1],))

    targetfilepath = srcfilepath + ".b64.txt"
    print(" The target file path : '%s'" %(targetfilepath,))
    
    with open(srcfilepath, 'rb') as sf:
        sb = sf.read()
        b64_sb = base64.b64encode(sb).decode()
     
        with open(targetfilepath, 'wt+') as tf:
            tf.write(b64_sb)
    """
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print(" The output directory '%s' is created." %(outdir,))
    """

def binfile_to_b64strfiles(srcfilepath, chunksize=1024*1024*5):
    if not os.path.exists(srcfilepath):
        raise FileNotFoundError("The file '%s' is NOT found!" %(srcfilepath,))
    if not os.path.isfile(srcfilepath):
        raise FileNotFoundError("The file '%s' is NOT file!" %(srcfilepath,))
    
    sf_dirname = os.path.dirname(srcfilepath)
    print(" The dir. of source file is '%s'." %(sf_dirname,))
    sf_basename = os.path.basename(srcfilepath)
    print(" The basename of source file is '%s'." %(sf_basename,))
    sf_ext = os.path.splitext(srcfilepath)
    print(" The ext[0] of source file is '%s'." %(sf_ext[0],))
    print(" The ext[1] of source file is '%s'." %(sf_ext[1],))

    #targetfilepath = srcfilepath + ".b64.txt"
    #print(" The target file path : '%s'" %(targetfilepath,))
    
    chunkindex = 0
    with open(srcfilepath, 'rb') as sf:
        while True:
            """
            block = file.read(150)
            if not block:
                break
            stream += [block]
            """
            sb = sf.read(chunksize)
            if not sb:
                break
            b64_sb = base64.b64encode(sb).decode()
            
            targetfilepath = f'{srcfilepath}_{chunkindex}.b64.txt'
            print(" The target file path : '%s'" %(targetfilepath,))

            with open(targetfilepath, 'wt+') as tf:
                tf.write(b64_sb)
            chunkindex += 1
    """
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print(" The output directory '%s' is created." %(outdir,))
    """


"""
def grouper(n, iterable, fillvalue=None):
    #"Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def split_bigfile(bigfilepath, outdir=".", outfilenameformat=None):
    if not os.path.exists(bigfilepath):
        raise FileNotFoundError("The file '%s' is NOT found!" %(bigfilepath,))
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print(" The output directory '%s' is created." %(outdir,))

    fn = os.path.basename(bigfilepath)
    ofn_format = outfilenameformat if not outfilenameformat and ""!=outfilenameformat else fn + ".splitted_ln_{0}"

    with open(bigfilepath, 'r') as f:
        for i, g in enumerate(grouper(LINE_PER_FILE, f, fillvalue=''), 1):
            outfilepath = os.path.join(outdir, ofn_format.format(i * LINE_PER_FILE))
            with open(outfilepath, 'w') as fout:
                fout.writelines(g)
            print(" The splitted file is created. %d : '%s'" %(i, outfilepath,))
"""


'''
    MAIN
'''
if __name__ == '__main__':
    srcfilepath = "/wspy/tmp/ChromeStandaloneSetup64.exe"
    #srcfilepath = "C:\\wspy\\tmp\\ChromeSetup.exe"
    #binfile_to_b64strfile(srcfilepath)
    binfile_to_b64strfiles(srcfilepath, 1024*1024*5)

    print("--"*30)
#fi __main__
#http://raw.githubusercontent.com/codenrg/sator-square/master/words-en.txt
