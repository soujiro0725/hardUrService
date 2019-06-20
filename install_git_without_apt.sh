unzip ./git-latest.zip
cd git-master
autoconf
./configure --with-curl=/usr/local
make
sudo make install

