#!/usr/bin/env bash

mkdir -p /usr/lib/checkstyle && \
cp checkstyle-8.12-all.jar /usr/lib/checkstyle/checkstyle.jar && \
mkdir -p /usr/lib/checkstyle/standards && \
cp -rf standards/* /usr/lib/checkstyle/standards
