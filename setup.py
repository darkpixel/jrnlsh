from setuptools import setup
import os
HERE = os.path.dirname(__file__)
VERSION_FILE = os.path.join(HERE, 'VERSION.txt')

setup(name='jrnlsh',
      version_config = {
          'count_commits_from_version_file': True,
          'template': '{tag}',
          'dev_template': '{tag}.dev.{ccount}',
          'dirty_template': '{tag}.dev.{ccount}',
          'version_file': VERSION_FILE,
      },
      setup_requires=['setuptools-git-versioning'],
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
