from setuptools import setup, find_packages

setup(
    name='Falmark',
    version='1.0',
    packages=['Falmark'],  # Manually specify the package containing Python modules
    py_modules=['falmark4'],  # Include the script file directly (no need for path)
    install_requires=[
        'psycopg2',
    ],
    entry_points={
        'console_scripts': [
            'Falmark = falmark4:main',  # Update the script entry point
        ]
    },
)

