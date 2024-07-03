# -*- coding: utf-8 -*-
#

import os

dir_local = ''
with os.scandir(".") as entries:
    for entry in entries:
        dir_local += f'{entry.name} size {entry.stat().st_size} byte\n'
print(dir_local)