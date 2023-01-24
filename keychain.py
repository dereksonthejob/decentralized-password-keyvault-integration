from Foundation import NSData
from PyObjCTools import AppHelper
from objc import *

class Keychain:
    def __init__(self):
        self.keychain = ObjCClass('Keychain
