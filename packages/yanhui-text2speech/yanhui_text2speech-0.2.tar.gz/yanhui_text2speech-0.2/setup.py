from setuptools import setup, find_packages

setup(
    name='yanhui_text2speech', 
    version='0.2',
    description='Convert text to speech',
  
    packages=find_packages(),
  
    install_requires=['requests','pydub'], 
  
    author='yanhui ',
    author_email='yanhui@csdn.net'
)