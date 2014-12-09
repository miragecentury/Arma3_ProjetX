__author__ = 'victorien.vanroye@gmail.com'

from enum import Enum


class AddonBuilderRegistryKey(Enum):
    Arma3Tools = r"Software\Bohemia Interactive\arma 3 tools"


class AddonBuilderToolsExe(Enum):
    AddonBuilderOld = "AddonBuilderOld.exe"