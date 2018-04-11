from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'mockito'
]

setup(name='mockito_demo',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)
