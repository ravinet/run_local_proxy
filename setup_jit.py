### RUN sudo sysctl -w net.ipv4.ip_forward=1 ##

import sys
import os



os.system( "sudo apt-get -y update" );

start_dir = os.getcwd()

os.system( "wget 'https://pypi.python.org/packages/source/s/selenium/selenium-2.39.0.tar.gz'" );

os.system( "sudo apt-get -y install python-setuptools python-pip xvfb xserver-xephyr tightvncserver unzip" );

os.system( "tar xvzf selenium-2.39.0.tar.gz" );

selenium_dir = start_dir + "/selenium-2.39.0"

os.chdir( selenium_dir );

os.system( "sudo python setup.py install" );

os.chdir( start_dir );

os.system( "sudo pip install pyvirtualdisplay" );

os.system( "wget 'http://chromedriver.storage.googleapis.com/2.8/chromedriver_linux64.zip' ");

os.system( "unzip chromedriver_linux64.zip" );

os.system( "wget 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb' ");

os.system( "sudo dpkg -i google-chrome-stable_current_amd64.deb" );

os.system( "sudo apt-get -f -y install" );
