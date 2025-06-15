#!/bin/bash

# 设置proot的路径和rootfs目录
PROOT_BIN=$(which proot)
ROOTFS_DIR="$HOME/ubuntu-rootfs"

# 如果rootfs目录不存在，提示用户先下载或安装rootfs
if [ ! -d "$ROOTFS_DIR" ]; then
  echo "Ubuntu rootfs目录不存在，请先下载并解压Ubuntu rootfs到 $ROOTFS_DIR"
  exit 1
fi

# 启动proot环境，挂载必要的系统目录
$PROOT_BIN -R "$ROOTFS_DIR" \
  -b /dev -b /proc -b /sys -b /tmp -b /etc/resolv.conf \
  /bin/bash --login
