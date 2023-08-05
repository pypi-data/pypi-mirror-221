from setuptools import setup

setup(
    name='orcaz',
    version='0.1.0',
    packages=['orcaz'],
    url='',
    license='Apache 2.0',
    author='Zacharias Chalampalakis, PhD, Lalith Kumar Shiyam Sundar, PhD',
    author_email='zacharias.chalampalakis@meduniwien.ac.at, lalith.shiyamsundar@meduniwien.ac.at',
    description='ORCA (Optimized Registration through Conditional Adversarial networks) is a cutting-edge tool designed to '
                ' ',
    install_requires=['pyfiglet~=0.8.post1',
                      'setuptools~=65.5.1',
                      'nibabel',
                      'tqdm',
                      'torch>=0.4.1',
                      'torchvision>=0.2.1',
                      'matplotlib',
                      'tensorboard',
                      'scipy',
                      'SimpleITK',
                      'scikit-learn',
                      'emoji',
                      'rich',
                      'mpire',],
    entry_points={
        'console_scripts': [
            'orcaz = orcaz.orcaz:main',
        ],
    },
)

