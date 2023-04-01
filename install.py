from pathlib import Path
import os
import shutil

there = Path("C:\\Users\\ExCyber\\.vscode\\extensions\\")
here  = Path('.')

yes = input(f'are you sure you want to copy {here} into {there} (y/n)? ')
if yes == 'y':
    assert(here.is_dir() and there.is_dir())
    shutil.copy(here , there)