from setuptools import setup, find_packages

VERSION = '1.5.7' 
DESCRIPTION = 'Streamlit Opencv player'
LONG_DESCRIPTION = 'Streamlit Opencv Player is a video player written in python for easy video playback and frames management using OpenCV'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="streamlitopencvplayer", 
        version=VERSION,
        author="Nafaa Bougraine",
        author_email="bougraine.nafaa@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'package'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)