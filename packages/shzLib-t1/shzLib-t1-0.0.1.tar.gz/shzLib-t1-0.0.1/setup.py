from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

project_name = 'shzLib-t1'

setup(name=project_name,
    version='0.0.1',
    license='MIT License',
    author='Eliseu Brito',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='eliseubrito776@gmail.com',
    keywords='shz tools shzlib',
    description=u'Personal support tools in the development of varied projects',
    packages=['shzLib'],
    install_requires=['numpy==1.25.1', 'pandas==2.0.3'],)