#!/bin/sh
for img in assets/images/*; do
    echo "Importing image $img"
    ./manage.py images add "$img"
done

for post in assets/news/*; do
    echo "Importing news $post"
    ./manage.py news import "$post"
done

./manage.py templatevar VERSION 2.2.1
./manage.py templatevar BETAVERSION 2.2.2-beta.4
