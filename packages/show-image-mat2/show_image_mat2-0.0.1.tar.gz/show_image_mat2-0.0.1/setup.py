from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='show_image_mat2',
    version='0.0.1',
    license='MIT License',
    author='Marcelo Torres',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='marcelotores21@gmail.com',
    keywords='matplotlib',
    description=u'Um repositório não oficial para exibir imagens',
    packages=['show_image_matp2'],
    install_requires=['matplotlib'],)