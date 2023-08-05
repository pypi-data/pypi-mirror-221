from setuptools import setup
setup(name='pymolviz',
        version='1.1',
        description='Library to facilitate creation of PyMOL Vizualizations.',
        url='',
        author='Finn Mier',
        license='MIT',
        packages=['pymolviz.meshes', 'pymolviz.volumetric', 'pymolviz.PyMOLobjects', 'pymolviz.util', 'pymolviz'],
        install_requires=[
                'numpy',
                'matplotlib',
                'scipy',
        ],
        long_description='See https://github.com/Finnem/PyMolViz for a detailed documentation.',
        zip_safe=False)
