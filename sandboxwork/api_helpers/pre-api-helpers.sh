#!/bin/bash

echo "Executing Pre-API Helpers"

echo "Creating VPC"

python ./$CUSTOMIZATION/api_helpers/python/vpc.py
