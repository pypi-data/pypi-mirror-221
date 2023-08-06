from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Convert your code screenshot into textual code'
LONG_DESCRIPTION = 'Convert your code screenshot into textual, properly formatted and indented code through computer vision'

# Setting up
setup(
    name="screenshot2code",
    version=VERSION,
    author="Seth Harding",
    author_email="seth@tokai.app",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['shutil', 'typing', 'pandas', 'pytesseract', 'guesslang', 'PIL'],
    keywords=['python', 'screenshot', 'screenshots', 'code', 'convert', 'computer vision', 'cv'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
