# -*- coding: utf-8 -*-

"""."""

# MIT License (see LICENSE)
# Author: Dániel Hagyárossy <d.hagyarossy@sapstar.eu>


import re
from typing import Any, ByteString, List, Optional
from check_jvm.logger import log

RE_ORACLE = re.compile(r".*oracle.*", flags=re.I)
RE_GOOD = re.compile(r"(?:IBM|SAP)", flags=re.I)
RE_PROPS = re.compile(r"^\s+(\S+(?:\.)?\S+)\s+=[ ]+(.*)$", flags=re.M)
RE_VERSION = re.compile(
    r"^.*version\s+\"(?P<version>[0-9\.]+).*\".*$", flags=re.M
)
RE_VERSION_ONLY = re.compile(r"^(?!Property)(\S+.*)$", flags=re.M)


class JavaExecutable:
    """JavaExecutable class is used to contain details of a JAVA executable.

    Methods:
        __init__(self, java_version_out)

    Properties:
        vendor: Vendor of the JAVA executable
        version: Version of the JAVA executable
        properties: Properties of the JAVA executable
        status: Status of the JAVA executable,
            OK if vendor is known and not Oracle
            KO if vendor is Oracle
            ?? if vendor is unknown

    """

    def __init__(self, java_out: Optional[ByteString] = b""):
        """Construct the JavaExecutable class.

        Args:
            rc: Return code of the connection failure
            *args: Other exception arguments

        """
        self.java_out = java_out.decode("utf-8")
        if java_out:
            self.raw_version = RE_VERSION_ONLY.findall(self.java_out)
            self.properties = dict(RE_PROPS.findall(self.java_out))
            if "java.vendor" in self.properties.keys():
                self.vendor = self.properties.get("java.vendor")

            if "java.version" in self.properties.keys():
                self.version = self.properties.get("java.version")
                version_match = re.match(
                    r"^(?P<version>[0-9\.]+).*$", self.version
                )
                if version_match:
                    self.version = version_match.group("version")
            else:
                version_match = RE_VERSION.match(self.raw_version)
                log.debug(self.raw_version)
                log.debug(version_match)
                if version_match:
                    self.version = version_match["version"]

    @property
    def status(self):
        if RE_ORACLE.match(self.vendor):
            return "KO"
        if RE_GOOD.match(self.vendor):
            return "OK"
        return "??"

    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        self._properties = properties

    @property
    def raw_version(self):
        return "\n".join(self._raw_version)

    @raw_version.setter
    def raw_version(self, raw_version):
        self._raw_version = raw_version

    def __repr__(self) -> str:
        """Return text representation of the class.

        Returns:
            Text representation of the java executable object.

        """
        return (
            f"<{self.__class__.__name__}: "
            f"version = '{self.version}', vendor = '{self.vendor}',"
            f" status = '{self.status}', properties = {self.properties}>"
        )

    __str__ = __repr__
