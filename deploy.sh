#!/bin/bash

aws s3 sync . s3://www.mariacmorrissey.com --exclude ".git/*" --exclude "deploy.sh"
