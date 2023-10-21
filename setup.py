from setuptools import setup

setup(
    name = 'viihdexdl',
    description = 'Command line tool for downloading HLS streams with FFmpeg',
    long_description = 'ViihdexDL is a commmand line tool for downloading HLS streams with multiple audio and subtitle streams using FFmpeg. User can select the audio and subtitle tracks to download using language codes.',
    url = 'https://github.com/Qotscha/viihdexdl',
    version = '0.14',
    packages = ['viihdexdl'],
    package_dir = {'viihdexdl': 'src'},
    install_requires = [
        'requests',
        'langcodes',
        ],
    entry_points = {
        'console_scripts': [
            'viihdexdl = viihdexdl.__main__:main'
            ]
        },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
        ]
    )