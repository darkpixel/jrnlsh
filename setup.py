from setuptools import setup

setup(name='jrnlsh',
      version='0.1',
      description='A simple shell wrapper for jrnl',
      url='http://github.com/darkpixel/jrnlsh',
      author='Aaron C. de Bruyn',
      author_email='aaron@heyaaron.com',
      license='MIT',
      packages=['jrnlsh'],
      entry_points='''
      [console_scripts]
      jrnlsh=jrnlsh:run_cli
      ''',
      zip_safe=False)
