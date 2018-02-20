#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Application import appCmn
from DatabaseAccess import dbaCmn

if __name__ == '__main__':

    appInfo = {'User': 'TestApp',
               'InterfaceCode': '99',
               'AppCode': '01',
               'AppModeCode': '99'
    }

    dCmn = dbaCmn.dbaCmn(**appInfo)
    aCmn = appCmn.appCmn(dCmn, **appInfo)

    ret = aCmn.StartApp()
    if ret == False:
        print "running"
        sys.exit()

    aCmn.EndApp()

#    aCmn.AbendApp('0009')
