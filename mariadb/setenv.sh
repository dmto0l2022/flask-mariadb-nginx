#!/usr/bin/env bash

# Show env vars
grep -v '^#' .env-example

# Export env vars
export $(grep -v '^#' .env | xargs)

