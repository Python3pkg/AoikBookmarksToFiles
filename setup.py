import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikBookmarksToFiles',

    version='0.1.5',

    description="""Convert a bookmark file in NETSCAPE-Bookmark-file-1 format exported from browsers like Chrome and Firefox into a set of Windows ".url" files or Gnome ".desktop" files.""",
    
    long_description="""`Documentation on Github 
<https://github.com/AoiKuiyuyou/AoikBookmarksToFiles>`_""",

    url='https://github.com/AoiKuiyuyou/AoikBookmarksToFiles',

    author='Aoi.Kuiyuyou',
    
    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='convert browser bookmark file Windows url file Gnome desktop file',

    install_requires=[
        'pyyaml',
        'AoikSixyIO',
        'AoikI18n',
    ],
      
    package_dir={'':'src'},
    
    packages=find_packages('src'),

    package_data={
        'aoikbookmarkstofiles.i18n': [
            '*.yml',
        ],
    },

    entry_points={
        'console_scripts': [
            'aoikbtf=aoikbookmarkstofiles.aoikbtf:main',
        ],
    },
)
