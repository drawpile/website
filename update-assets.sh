#!/bin/bash

for img in assets/images/*
do
	./manage.py images add "$img"
done

for post in assets/news/*
do
	./manage.py news import "$post"
done

./manage.py templatevar VERSION 2.0.8 --no-overwrite

