
if [ -n "$(which apt-get)" ] ; then
    echo "debian system. using apt..."
    sudo apt-get update
else [ -n "$(which yum)" ]
    echo "redhat system. using yum"
    sudo yum update
fi
