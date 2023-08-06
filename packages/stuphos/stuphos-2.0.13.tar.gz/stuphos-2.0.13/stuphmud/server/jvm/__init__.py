# Coordinates JPype access to the Java Virtual Machine
# inside StuphMUD using Extension Core.
#
# Use jpype_provider.JPypeProvider for jvm-ready methods.
#
# Todo: Utilize the SecuritySupport of Context:
#    org.mozilla.javascript.resources.Security:
#       security.requireSecurityDomain = true

# Build facility.
from stuphos.runtime.facilities import Facility
from stuphos.runtime.registry import getObject

# Configure access.
def _createJavaVM():
    from .jpype_provider import JPypeProvider
    from stuphos import getConfig
    # todo: alternatively, jvm-path
    return JPypeProvider(getConfig('java-home'))

JVM_GATEWAY_OBJECT = 'JVM::Gateway'
def getJavaVM():
    return getObject(JVM_GATEWAY_OBJECT,
                     create = _createJavaVM)

def getJavaVMPackage(package):
    return getJavaVM()[package]

class JavaManager(Facility):
    # Todo: allow commands for rhino-entities test harness.
    NAME = 'JVM::Manager'

    class Manager(Facility.Manager):
        VERB_NAME = 'jvm*-manage'
        MINIMUM_LEVEL = Facility.Manager.IMPLEMENTOR

    @classmethod
    def create(self):
        # Boot JVM dynamically on command.
        if not getJavaVM().bootJVM():
            raise SystemError('Unable to boot JVM')

        installSubServices()
        return self()

    def __str__(self):
        return '{%s: %s}' % (self.__class__.__name__,
                             getJavaVM().getJavaHome())

# Install.
JavaManager.manage()

def installSubServices():
    # Todo: install rhino and js-commands.
    from .rhino import installRhinoController
    installRhinoController()
