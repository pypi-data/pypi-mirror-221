from setuptools import setup, find_packages

setup(
    name='UNET_MDLE_CASE',
    version='0.2',
    packages=find_packages(),
    install_requires=['opencv-python>=4.7.0', 'numpy>=1.21.5', 'scikit-image>=0.20.0', 'pandas>=2.0.2', 'tqdm>=4.65.0', 'scikit-learn>=0.0.post1', 'matplotlib>=3.3.4', 'seaborn>=0.11.1', 'tensorflow>=2.0.0'],
    author='Zhuldyz Ualikhankyzy, Thomas Ciardi',
    author_email='zxu4@example.com, tgc17@case.edu',
    description='Package that helps to load data for, build, train, test, and visualize the results of UNET CNN',
    url='https://github.com/juldyzmurat/UNET',
    package_data={'UNET_MDLE_CASE': ['examples/*']},
)
