#!/bin/bash

OUTPUT_FILENAME=$(date -d 'today' +'%Y%m%d%H%M%S').html

jupyter nbconvert \
--execute \
--to html \
--output export/$OUTPUT_FILENAME \
notebook.ipynb

cp -f export/$OUTPUT_FILENAME export/latest.html