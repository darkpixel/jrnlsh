from setuptools import setup

setup(name='jrnlsh',
      version_config = {
          "template": "{tag}",
          "dev_template": "{tag}.{branch}+git.{sha}",
          "dirty_template": "{tag}.{branch}+git.{sha}.dirty",
          "version_file": VERSION_FILE,
      },
      setup_requires=["setuptools-git-versioning"],
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
