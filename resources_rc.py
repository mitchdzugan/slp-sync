# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x7f\
i\
mport QtQuick\x0aim\
port QtQuick.Con\
trols\x0a\x0aApplicati\
onWindow {\x0a    i\
d: window\x0a    wi\
dth: 1024\x0a    he\
ight: 600\x0a    vi\
sible: true\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9b\x91}\x97\x91\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
