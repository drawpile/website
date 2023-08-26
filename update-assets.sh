#!/bin/bash

for img in assets/images/*
do
	./manage.py images add "$img"
done

for post in assets/news/*
do
	./manage.py news import "$post"
done

./manage.py templatevar VERSION 2.1.20
./manage.py templatevar BETAVERSION 2.2.0-beta.7

