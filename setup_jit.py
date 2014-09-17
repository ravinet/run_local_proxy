### RUN sudo sysctl -w net.ipv4.ip_forward=1 ##

import sys
import os



os.system( "sudo apt-get -y update" );

os.system( "sudo apt-get -y install autotools-dev dh-autoreconf iptables protobuf-compiler libprotobuf-dev pkg-config libssl-dev dnsmasq-base apache2-bin ssl-cert phantomjs git" );

os.system( "git clone https://www.github.com/ravinet/mahimahi" );

start_dir = os.getcwd()
mahimahi_dir = start_dir + "/mahimahi"

os.chdir( mahimahi_dir );

os.system( "git checkout send_could_not_finds" );

os.system( "./autogen.sh && ./configure && make -j && sudo make install" );

os.chdir( start_dir );

# COMMENT NEXT BLOCK OUT IF THIS IS NOT TO SET UP LOCAL PROXY (CLIENT) MACHINE #

os.system( "wget 'https://pypi.python.org/packages/source/s/selenium/selenium-2.39.0.tar.gz'" );

os.system( "sudo apt-get -y install python-setuptools python-pip xvfb xserver-xephyr tightvncserver unzip" );

os.system( "tar xvzf selenium-2.39.0.tar.gz" );

selenium_dir = start_dir + "/selenium-2.39.0"

os.chdir( selenium_dir );

os.system( "sudo python setup.py install" );

os.chdir( start_dir );

os.system( "sudo pip install pyvirtualdisplay" );

os.system( "wget 'http://chromedriver.storage.googleapis.com/2.8/chromedriver_linux32.zip' ");

os.system( "unzip chromedriver_linux32.zip" );

os.system( "wget 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb' ");

os.system( "sudo dpkg -i google-chrome-stable_current_i386.deb" );

os.system( "sudo apt-get -f -y install" );
