from setuptools import setup


with open('README.md', 'rb') as f:
    longdesc = f.read().decode().strip()


setup(
    setup_requires=[
        'setuptools_scm',
    ],

    use_scm_version={
        'write_to': 'ezca/__version__.py',
    },

    name='ezca',
    description='aLIGO CDS Python EPICS interface',
    long_description=longdesc,
    long_description_content_type='text/markdown',
    author='Jameson Graef Rollins',
    author_email='jameson.rollins@ligo.org',
    url='https://git.ligo.org/cds/python-ezca',
    license='GPL-3.0-or-later',
    classifiers=[
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    packages=[
        'ezca',
        'ezca.emulators',
    ],

    package_data={
        'ezca.emulators': ['TEST_FILTER.adl'],
    },

    install_requires=[
        'pcaspy',
        'pyepics>=3.4.1',
    ],
)
