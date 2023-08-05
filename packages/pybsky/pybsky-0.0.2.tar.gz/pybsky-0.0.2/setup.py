from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python Client for bsky social media'
LONG_DESCRIPTION = 'Python Client for bsky social media'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pybsky",
        version=VERSION,
        author="softrebel, ovan",
        author_email="sh.mohammad66@yahoo.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'pybsky','bsky'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Linux :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
