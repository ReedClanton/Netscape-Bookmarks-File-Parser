from setuptools import setup

__author__ = 'FlyingWolFox'
__email__ = 'lips.pissaia@gmail.com'
__version__ = '1.0'

long_description = 'This is a Parser and a creator for the Netscape Bookmarks' \
                   ' file format, generated by browser when exporting bookmarks' \
                   ' to html. It parses the file and deliver you an object' \
                   ' representing the file with the bookmark structure of folders' \
                   ' and shortcuts as objects too. The folder tree can be navigated' \
                   ' by the "." notation. '

setup(
    name='netscape-bookmarks-file-parser',
    version=__version__,
    packages=['NetscapeBookmarksFileParser'],
    url='https://github.com/FlyingWolFox/Netscape-Bookmarks-File-Parser',
    license='MIT',
    author=__author__,
    author_email=__email__,
    description='Parser and creator for the Netscape Bookmarks file format',
    long_description=long_description,
    keywords='parse-netscape-bookmarks-file-1 parse-netscape-bookmarks-file '
             'parse-netscape parse-bookmarks parser bookmarks netscape browser'
             'create-netscape-bookmarks-file-1 create-netscape-bookmarks-file '
             'create-netscape create-bookmarks create '
             'generate-netscape-bookmarks-file-1 generate-netscape-bookmarks-file '
             'generate-netscape generate-bookmarks generate',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
