#!/usr/bin/env python

from pathlib import Path
import subprocess
import sys

package_list = str(Path(Path.cwd() / 'requirements.txt'))

# Upgrades pip
def upgrade_pip():
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])


# Calls pip to install a package referred using package_name.
def install_package(package_name:str):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])


upgrade_pip()

# Install packages using the file packages.txt
package_names = open(package_list, 'r').readlines()

for package in package_names:
    install_package(package)
