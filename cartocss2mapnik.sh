#!/bin/bash

# This script converts CartoCSS style to Mapnik XML
# Assumes CartoCSS parser is installed and known as 'carto'

STYLE_INPUT=$1
STYLE_OUTPUT="${1/mss/xml}"

carto $STYLE_INPUT > $STYLE_OUTPUT