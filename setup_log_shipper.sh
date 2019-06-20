# 

# download from 
# https://www.elastic.co/jp/downloads/beats/filebeat

VERSION=7.1.1
curl -k -L -O "https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${VERSION}-amd64.deb"
sudo dpkg -i filebeat-${VERSION}-amd64.deb

