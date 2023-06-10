#!/bin/bash
# 强制覆盖本地修改
git fetch --all
git reset --hard main # 这里接的是分支名字，main
git pull