# dpmkit

A simple tool for creating DPMKs.

## Usage

First of all, you will need to find the downstream kernel. If you don't have the source tree, this tool is useless.  

Once you find the source tree, download it with dpmkit (replace the URL here with the one for your source tree):

`python3 -m dpmkit fetch-downstream https://github.com/lowendlibre/mt8168-linux-merged/archive/refs/tags/4.14.186-20230124.tar.gz`

Once you fetch the downstream kernel, dpmkit will suggest a command to download the matching mainline version (referred to as `oldmainline`), which you will need to run.

Then, download the latest mainline version:

`python3 -m dpmkit fetch-mainline https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.4.3.tar.xz`

Once you have downloaded all of the kernels needed, you can then create the patch:

`python3 -m dpmkit patch`

And finally, to apply the patch to mainline:

`python3 -m dpmkit apply`

You will quickly notice **a lot** of changes that can't be applied. You will need to fix those manually.

## What is a DPMK?

A downstream patched mainline kernel, or DPMK, is a mainline kernel that has downstream vendor patches applied to it.

## Why should I use a DPMK?

Normally, you shouldn't. If your device has good enough mainline support, you should just use the mainline kernel.

However, for devices which use an outdated kernel version for their downstream branch and do not have proper mainline support, creating a DPMK would be the easiest way to get the latest security updates.

DPMKs are also a useful starting point for mainlining.

## Why don't you just use git to merge the kernel branches?

Device vendors rarely publish their git branches, so this quickly becomes a painful task since you have to create commits with the correct parent commit to avoid conflicts.

On the other hand, dpmkit is specifically designed for this task.
