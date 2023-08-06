import setuptools
setuptools.setup(
    name='uszipstats',         # How you named your package
    packages=['code_zip'],   # Chose the same as "name"
    version='0.2',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    description='sample package',   # Give a short description about your library
    author='VEDANT RATHI',                   # Type in your name
    author_email='vedrathi10@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/vrathi101/uszipstats.git',
    # I explain this later on
    download_url='https://github.com/vrathi101/uszipstats/archive/refs/tags/v_02.tar.gz',
    keywords=['DATA', 'FUNCTIONS'],   # Keywords that define your package best
    install_requires=[
        'pandas',
        'numpy',
        'requests',
        'matplotlib',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
