#!/bin/bash
set -e
coverage3 run -m unittest discover tests/
coverage3 report -m
