tar xzvf git-latest.tar.gz
cd git-{date} // edit it
autoconf
./configure --with-curl=/usr/local
make
make install

