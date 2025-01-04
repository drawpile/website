#!/bin/sh
for img in assets/images/*; do
    set -x
    ./manage.py images add "$img"
    set +x
done

for post in assets/news/*; do
    set -x
    ./manage.py news import "$post"
    set +x
done

./manage.py templatevar VERSION 2.2.1
./manage.py templatevar BETAVERSION 2.2.2-beta.4
