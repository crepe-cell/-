#!/bin/bash

echo -e "\e[1;34m=====================================\e[0m"
echo -e "\e[1;32m       System Information\e[0m"
echo -e "\e[1;34m=====================================\e[0m"

# 读取 /etc/os-release 并提取关键字段
if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo -e "\e[1;33mOS:\e[0m $NAME $VERSION"
fi

# 读取 /proc/version 获取内核信息
echo -e "\e[1;33mKernel Version:\e[0m $(cat /proc/version | awk '{print $1, $2, $3}')"

echo -e "\e[1;34m=====================================\e[0m"
