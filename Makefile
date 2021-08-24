#vars
IMAGENAME= yeoldprinter
REPO=defilan
IMAGEFULLNAME=${REPO}/${IMAGENAME}

.PHONY: help build run all

help:
	    @echo ""
	    @echo "Makefile commands:"
	    @echo "build"
	    @echo "run"
	    @echo "all"

.DEFAULT_GOAL := all

build:
	    @docker build -t ${IMAGEFULLNAME} .

run:
	    @docker run -it ${IMAGEFULLNAME}

all: build run