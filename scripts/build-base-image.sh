#!/bin/bash
# scripts/build-base-image.sh

set -e

echo "Building base image for TeamIT services..."
docker build -t teamit/base:latest -f docker/base/Dockerfile .

echo "Base image built successfully."