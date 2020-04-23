#!/bin/sh

CURR_DIR=`pwd`
STATIC_DIR=$CURR_DIR/mm_evaluation/static/mm_evaluation
wget --directory-prefix=$STATIC_DIR/js/ https://raw.githubusercontent.com/seiyria/bootstrap-slider/master/dist/bootstrap-slider.js
wget --directory-prefix=$STATIC_DIR/css/ https://raw.githubusercontent.com/seiyria/bootstrap-slider/master/dist/css/bootstrap-slider.css 
