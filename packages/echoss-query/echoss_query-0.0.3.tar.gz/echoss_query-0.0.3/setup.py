from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()
print(long_description)
setup(
    name='echoss_query',
    version='0.0.3',
    packages=['echoss_query'],
    url='',
    requires=['pandas','pymongo','PyMySQL','PyYAML','opensearch'],
    license='',
    author='incheolshin',
    author_email='incheolshin@12cm.co.kr',
    description='echoss AI Bigdata Solution - Query Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={},
    python_requires= '>3.7',
)