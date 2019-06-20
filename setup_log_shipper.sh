# 

# download from 
# https://www.elastic.co/jp/downloads/beats/filebeat

VERSION=7.1.1
curl -k -L -O "https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${VERSION}-amd64.deb"
sudo dpkg -i filebeat-${VERSION}-amd64.deb

# reference:
# https://qiita.com/suzuki_y/items/f40fe4fc30b9790965db
# filebeat.prospectors:

# # 参照する指定場所を記載します
# - input_type: log
#   paths:
#     - /home/demo/filebeat/*.log
#     #- c:\programdata\elasticsearch\logs\*

# #----------------------------- Logstash output --------------------------------
# # 出力先のログスタッシュを指定します
# output.logstash:
#   hosts: ["localhost:5044"]
