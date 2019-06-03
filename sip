https://www.riverbankcomputing.com/static/Downloads/sip/4.19.17/sip-4.19.17.tar.gz



https://sourceforge.net/projects/libpng/files/zlib/1.2.9/zlib-1.2.9.tar.gz/download
tar -xvf ~/Downloads/zlib-1.2.9.tar.gz
cd zlib-1.2.9
sudo -s
./configure; make; make install
cd /lib/x86_64-linux-gnu
ln -s -f /usr/local/lib/libz.so.1.2.9/lib libz.so.1
cd ~
rm -rf zlib-1.2.9
