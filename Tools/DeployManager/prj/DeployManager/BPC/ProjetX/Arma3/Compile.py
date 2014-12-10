__author__ = 'victorien.vanroye@gmail.com'

import subprocess
import winreg

from BPC.ProjetX.Arma3 import AddonBuilderRegistryKey
from BPC.ProjetX.Arma3 import AddonBuilderToolsExe


class AddonBuilder():
    def __init__(self, pathToExe=None):

        self.pathToExe = pathToExe
        self.pathToSign = None
        self.pathToTmp = None
        self.checkInit()

    def checkInit(self):
        if self.pathToExe is None:
            self.findAddonBuilderExe()


    def findAddonBuilderExe(self):
        try:
            areg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(areg, AddonBuilderRegistryKey.Arma3Tools)
            self.pathToExe = winreg.QueryValueEx(key, "path")[0]
        except Exception:
            print("ERROR")

    def setTmp(self, pathToTmp):
        self.pathToTmp = pathToTmp

    def setSign(self, pathToSign):
        self.pathToSign = pathToSign

    def compile(self, pathToSource, pathToTarget, include="*", pathToKeystore=None):
        if self.pathToExe is not None:
            exe = self.pathToExe + "\\" + AddonBuilderToolsExe.AddonBuilderOld.value
            exe = exe + " \"" + pathToSource + "\" \"" + pathToTarget + "\""
            if self.pathToSign is not None:
                exe = exe + " -sign=\"" + self.pathToSign + "\""
            if include is not None:
                exe = exe + " -include=\"" + include + "\""
            if self.pathToTmp is not None:
                exe = exe + " -tmp=\"" + self.pathToTmp + "\""
            subprocess.call(exe)
        else:
            print("ERROR")