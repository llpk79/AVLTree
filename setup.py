import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='lambdataAVLTree',
    version='0.0.13',
    author='Paul Kutrich',
    author_email='pkutrich@gmail.com',
    description='AVL Tree',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/llpk79/AVLTree',
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Operating System :: OS Independent'],
)