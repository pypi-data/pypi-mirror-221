import setuptools

# Function to read the requirements from requirements.txt
def parse_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

setuptools.setup(
    name='logassistant',
    version='0.1.1',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=parse_requirements('requirements.txt'),  # Read from requirements.txt
    entry_points={
        'console_scripts': [
            'log_assist_script = main:main',
        ],
    },
)
