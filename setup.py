from setuptools import setup, find_packages

setup(
    name='dbcreator',
    version='0.0.0',
    author=u'Miguel Branco',
    author_email='miguel@raw-labs.com',
    scripts=['dbcreator'],
    install_requires = [
        'psycopg2==2.5.2',
        'boto==2.27.0'
    ]
)
