import sys
import subprocess

import argparse
from modulefinder import ModuleFinder

def main(filename):

    # 'filename' is Namespace type, find its string
    filename = args.f

    finder = ModuleFinder()
    finder.run_script(filename)
    # find uninstalled modules
    uninstalled_libs = [l for l in finder.badmodules.keys()]
    print(f'Packages {uninstalled_libs} are missing.')

    # install each lib
    for i in uninstalled_libs:
        # implement pip as a subprocess:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
        
        # process output with an API in the subprocess module:
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_libs = [r.decode().split('==')[0] for r in reqs.split()]
        
        print(f'Successfully installed: {installed_libs}.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filename")
    parser.add_argument("-f", help="Filename")
    args = parser.parse_args()
    
    main(args)    