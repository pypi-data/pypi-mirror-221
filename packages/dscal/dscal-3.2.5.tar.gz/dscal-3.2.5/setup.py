from setuptools import setup,find_packages

setup(
    name='dscal',
    version='3.2.5',
    description='Quick solutions to calculus and mathematical operations.',
    long_description=open('README.txt').read()+'\n\n\n\n'+open('CHANGELOG.txt').read(),
    author='Dhruv Sehwal',
    author_email='zarexdhruv@gmail.com',
    url='https://sites.google.com/view/dscal3/home',
    license='MIT',
    packages=find_packages(),
    install_requires=['matplotlib','numexpr','sympy']
    )
