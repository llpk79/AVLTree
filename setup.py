import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='AVLTree',
    version='0.0.1',
    author='Paul Kutrich',
    author_email='pkutrich@gmail.com',
    description='AVL Tree',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/llpk79/AVLTree',
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 2, 3',
                 'license :: OSI Approved :: GNU GPLv3',
                 'Operating System :: OS Independent'],
)