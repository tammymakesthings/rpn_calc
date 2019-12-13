from setuptools import setup, find_packages
from rpn_calc import calc_version

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name = 'rpn_calc',
    version = RPN_CALC_VERSION,
    description = 'Simple RPN Calculator using the sly lexer',
    author = 'Tammy Cravit',
    author_email = 'tammymakesthings@gmail.com',
    url = 'https://github.com/tammymakesthings/rpn_calc',
    license = 'MIT',
    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Math :: Calculators',
      ],

    packages=find_packages(),

    setup_requires = [
        'pytest-runner'
    ],
    tests_require = [
        'pytest'
    ],
    install_requires = [
        'sly',
        'pyyaml'
    ],

    entry_points = {
        'console_scripts': ['rpn_calc=rpn_calc.CalcRepl:shell'],
    }.
)