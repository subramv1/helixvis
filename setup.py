from setuptools import setup

with open("README.MD", 'r') as f:
    long_description = f.read()

setup(
   name='helixvis',
   version='1.0.1',
   description='Create 2-dimensional visualizations of alpha-helical peptide sequences',
   license="GPL-3",
   long_description=long_description,
   long_description_content_type= 'text/markdown', 
   classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Chemistry',
      ],
   project_urls={
        'Bug Tracker': "https://github.com/subramv/helixvis/issues",
        'Documentation': "https://github.com/subramv/helixvis/blob/master/DOCUMENTATION.md",
        'Source Code': "https://github.com/subramv/helixvis",
    },
   url = "https://pypi.org/project/helixvis/",
   author='Vigneshwar Subramanian, Raoul Wadhwa, Regina Stevens-Truss',
   maintainer_email='vxs294@case.edu',
   packages=['helixvis'],  
   install_requires=['numpy', 'pandas', 'matplotlib'], 
)