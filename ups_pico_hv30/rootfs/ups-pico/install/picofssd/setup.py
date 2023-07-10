
"""picofssd: UPSPIco file-safe shutdown daemon

This script is intended for use with the PiModules(R) UPSPIco
uninterruptible power supply for use with a Raspberry Pi computer.
"""

classifiers = """\
Development Status :: 5 - Testing/Beta
Intended Audience :: PiModules UPS PiCo Product developers and partners (change to customers when published)
License :: GNU General Public License Version 3
Programming Language :: Python >= 3
Topic :: PiModules(R)
Topic :: UPS PIco support daemon
Operating System :: Linux (Raspbian)
"""

from distutils.core import setup

doclines = __doc__.split("\n")

setup(name='picofssd',
      version='0.2',
      description=doclines[0],
      long_description = "\n".join(doclines[2:]),
      license='GPL3',
      author='David Pose',
      author_email='pose_b@hotmail.com',
      url='http://pimodules.com',
      platforms=['POSIX'],
      classifiers = filter(None, classifiers.split("\n")),
      scripts=['scripts/picofssd'],
      packages=[]
      )
