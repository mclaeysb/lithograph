#!/bin/bash

# This script downloads OSM data and loads it into a local PostGIS database
# Assumes PostGRES is running locally

# Bounding boxes
BBOX_DdlG="3.6,51.0,3.8,51.1" # Gand XXII / 1 map DdlG (NGI Belgium) "3.626658931,51.0919539,3.742047162,51.00140605"
BBOX_Ghent="3.5,50.8,3.8,51.2" # Ghent, Belgium

if [ ! -f data.osm ]; then
	wget -O data.osm "http://www.overpass-api.de/api/xapi_meta?*[bbox=$BBOX_DdlG]"
fi

DBNAME=lithographdb
dropdb $DBNAME
createdb $DBNAME

psql $DBNAME << EOF
CREATE EXTENSION postgis;
CREATE EXTENSION hstore;
EOF

# osm2psql
osm2pgsql --database $DBNAME --slim --hstore data.osm

# rm data.osm