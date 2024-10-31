from . import __path__
from glob import glob
import os
import tomllib
import subprocess

ROOT_DIR = os.path.realpath(os.path.join(__path__[0], '../..'))
HARP_EXPECTED_VERSION =  '^0.7.4'
CAPTURE_OUTPUT = True


def main():
    for x in glob('*', root_dir=ROOT_DIR):
        example_dir = os.path.join(ROOT_DIR, x)
        if not  os.path.isdir(example_dir):
            continue    

        print(f"=== {x} ({example_dir}) ===")

        with open(os.path.join(example_dir, 'pyproject.toml'), 'rb') as f:
            conf = tomllib.load(f)
        try:
            version = conf['tool']['poetry']['dependencies']['harp-proxy']
        except KeyError:
            print ('   ⚠️ No dependeny to harp found.')

        if version !=HARP_EXPECTED_VERSION:
            print ('   ⚠️ Erroneous version: found {}, expected {}.'.format(version, HARP_EXPECTED_VERSION))

        try:
            subprocess.run("poetry lock", shell=True, check=True, cwd=example_dir, capture_output=CAPTURE_OUTPUT)
        except subprocess.CalledProcessError:
            print ('   ⚠️ Error while running poetry lock.')

        try:
            subprocess.run("make install", shell=True, check=True, cwd=example_dir, capture_output=CAPTURE_OUTPUT)
        except subprocess.CalledProcessError:
            print ('   ⚠️ Error while running make install.')

        try:
            subprocess.run("make test", shell=True, check=True, cwd=example_dir, capture_output=CAPTURE_OUTPUT)
        except subprocess.CalledProcessError:
            print ('   ⚠️ Error while running make test.')


        #from pprint import pprint
        #pprint(conf) 

if __name__ == '__main__':
    main()