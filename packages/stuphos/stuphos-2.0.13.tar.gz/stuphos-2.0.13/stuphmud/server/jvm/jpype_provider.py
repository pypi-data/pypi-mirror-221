# JVM(JPype) Management Facility
import os
import os.path
import sys

# XXX This implementation requires jvm_path be relative to java_home!
class JPypeProvider:
    ENV_JAVA_HOME = 'JAVA_HOME'
    ENV_JVM_PATH = 'JVM_PATH'
    EXC_JVM_BOOT_MSG = 'Unable to start JVM'
    ENV_CONFIG_NAME = 'JPype::isJVMLoaded'

    JVM_CANDIDATES = ['jre/bin/client/jvm.dll',
                      'bin/client/jvm.dll',
                      'lib/i386/server/libjvm.so',
                      'lib/i386/client/libjvm.so']
                      #'jre7/bin/client/jvm.dll']

    class NotFoundError(Exception):
        pass

    class PackageAccessor(object):
        def __init__(self, jvm):
            self.jvm = jvm
        def __getattr__(self, name):
            return self.jvm.importJPype().JPackage(name)

    def __init__(self, java_home = None, jvm_path = None):
        self.java_home = java_home
        self.jvm_path = jvm_path
        self.boot_errors = []
        self.package = self.PackageAccessor(self)

    def getJavaHome(self):
        return self.java_home or os.environ[self.ENV_JAVA_HOME]

    def getJVMPath(self):
        java_home = self.getJavaHome()
        for jvm in self.getJVMCandidates():
            c = os.path.join(java_home, jvm)
            # c = os.path.normpath(c)
            if os.path.exists(c):
                return c

        # If using getDefaultJVMPath, requires JAVA_HOME be set.
        ##    import jpype
        ##    installJavaHome(self.getJavaHome())
        ##
        ##    jvmPath = jpype.getDefaultJVMPath()
        ##    if os.path.exists(jvmPath):
        ##        return jvmPath

        raise self.NotFoundError()

    def getJVMCandidates(self):
        if self.jvm_path:
            yield self.jvm_path
        else:
            try: yield os.environ[self.ENV_JVM_PATH]
            except KeyError:
                for c in self.JVM_CANDIDATES:
                    yield c

    def installJavaHome(self, javaHome, soft = True):
        if not (soft or self.ENV_JAVA_HOME in os.environ):
            os.environ[self.ENV_JAVA_HOME] = javaHome

    def isJVMBootError(self, e):
        # CreateJVM failed because it already exists?
        # return e.message.startswith(self.EXC_JVM_BOOT_MSG)
        try: return e.args and e.args[0].startswith(self.EXC_JVM_BOOT_MSG)
        except AttributeError: pass

    def getConfigScope(self):
        return sys

    def isJVMLoaded(self):
        return getattr(self.getConfigScope(), self.ENV_CONFIG_NAME, False)

    def setJVMLoaded(self, state = True):
        setattr(self.getConfigScope(), self.ENV_CONFIG_NAME, True)

    def bootJVM(self):
        if not self.isJVMLoaded():
            jpype = self.importJPype()
            try: jpype.startJVM(self.getJVMPath())
            except Exception as e:
                # debugOn()
                if not self.isJVMBootError(e):
                    self.storeBootError(e)
                    from stuphos.etc.tools import reraiseSystemException
                    reraiseSystemException()
            else:
                self.setJVMLoaded()

                from atexit import register
                register(self.unloadJVM)

        return self.isJVMLoaded()

    def unloadJVM(self):
        self.importJPype().shutdownJVM()

    def storeBootError(self, e):
        self.boot_errors.append(e)
    def getBootErrors(self):
        # Copy?
        return self.boot_errors

    def importJPype(self):
        import jpype
        return jpype

    # External accessor.
    def getJPypeItem(self, name):
        if not self.isJVMLoaded():
            raise RuntimeError('JVM not yet loaded')

        return getattr(self.importJPype(), name)

    __getitem__ = getJPypeItem

# Rely on JAVA_HOME.
default = JPypeProvider()
