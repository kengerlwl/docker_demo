#!/bin/bash
# 强制覆盖本地修改
git fetch --all
git reset --hard origin/master 
git pull