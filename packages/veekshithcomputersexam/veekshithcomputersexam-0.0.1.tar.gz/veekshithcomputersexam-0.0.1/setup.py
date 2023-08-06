from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='veekshithcomputersexam',
  version='0.0.1',
  description='basic opencv function automation library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Veekshith Rao',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='opencv, opencv2, cv2, opencv_python', 
  packages=find_packages(),
  install_requires=[''] 
)