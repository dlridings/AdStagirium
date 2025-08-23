#!/bin/bash

cp variant-template.md $1
git add $1

echo "Copied and added $1 to git. Please edit the file as needed."