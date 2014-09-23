# -*- coding: utf-8 -*-
'''
Created on 2012/04/12

@author: 0000131307
'''

#packageとmoduleは似てるが、packageの場合はdirectory
#そのdirectoryに__init__.pyは必須

import package1
import package2

#packageのimportする時に__init__の実行をする
package1.mod() #__init__の中にmodのimportはある
package2.mod() #__init__の中にmodのimportはある

#relative importはOK！ check package1\__init__.py
package1.package2.mod()
#これもOK
from package1 import mod
mod()




