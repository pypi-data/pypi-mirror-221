#	dpmkit - dpmkit/__init__.py
#
#	Copyright (C) 2023 hexaheximal
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .util import *
import tarfile
import os

def fetch_kernel(name, kernel_type):
	filename = os.path.realpath(name)

	if not os.path.isdir("kernels"):
		os.mkdir("kernels")

	os.chdir("kernels")

	if not os.path.isfile(filename):
		if not name.startswith("http://") and not name.startswith("https://"):
			print("Invalid kernel path!")
			return
		
		print("Downloading kernel...")

		os.environ["KERNEL_URL"] = name
		os.environ["KERNEL_TYPE"] = kernel_type
		os.system("wget ${KERNEL_URL}")

		filename = os.path.basename(name)
	
	kernel_directory = get_kernel_directory(filename)

	print("Extracting kernel...")

	os.environ["KERNEL_FILENAME"] = filename

	if kernel_directory != None:
		os.system("tar -xvf ${KERNEL_FILENAME}")
	else:
		kernel_directory = os.path.basename(filename).split(".tar.")[0]
		os.environ["KERNEL_DIRECTORY"] = kernel_directory
		os.system("tar -xvf ${KERNEL_FILENAME} -C${KERNEL_DIRECTORY}")
	
	print("Figuring out which kernel version this is...")

	f = open(os.path.join(kernel_directory, "Makefile"), "r")

	version = None
	patchlevel = None
	sublevel = None

	line = ""

	while not line.startswith("NAME = "):
		line = f.readline().strip()
		
		if line.startswith("VERSION = "):
			version = int(line.replace("VERSION = ", ""))
		
		if line.startswith("PATCHLEVEL = "):
			patchlevel = int(line.replace("PATCHLEVEL = ", ""))
		
		if line.startswith("SUBLEVEL = "):
			sublevel = int(line.replace("SUBLEVEL = ", ""))
	
	version_string = f"{version}.{patchlevel}"

	if sublevel != 0:
		version_string += f".{sublevel}"
	
	os.chdir("..")
	
	f = open(f"{kernel_type}-version", "w")
	f.seek(0)
	f.write(version_string)
	f.close()

	print("Creating kernel symlink...")

	os.symlink("kernels/" + kernel_directory, kernel_type)

	print("Finished!")

	if kernel_type == "downstream":
		print(f"Hint: To download the old mainline version equivalent to downstream, run \"dpmkit fetch-oldmainline https://cdn.kernel.org/pub/linux/kernel/v{version}.x/linux-{version_string}.tar.xz\"")

def create_patch():
	if not os.path.isdir("oldmainline") or not os.path.isdir("downstream"):
		print("Failed to find the oldmainline and/or downstream kernel. Please download them first!")
		return
	
	print("Figuring out which files have been changed...")

	os.system("diff -qdr oldmainline downstream | awk '/differ$/{print $2\",\"$4}' > downstream-changes")

	print("Creating patches...")

	if not os.path.isdir("patches"):
		os.mkdir("patches")
	
	f = open("downstream-changes", "r")

	line = f.readline().strip()

	while line != "":
		mainline_file = line.split(",")[0]
		downstream_file = line.split(",")[1]

		os.environ["MAINLINE_FILE"] = mainline_file
		os.environ["DOWNSTREAM_FILE"] = downstream_file
		os.environ["PATCH_NAME"] = "patches/" + mainline_file.replace("oldmainline/", "").replace("/", "_") + ".patch"

		os.system("diff -dupN ${MAINLINE_FILE} ${DOWNSTREAM_FILE} > ${PATCH_NAME}")

		line = f.readline().strip()

def apply_patch():
	if not os.path.isdir("mainline") or not os.path.isdir("patches") or not os.path.isfile("downstream-changes"):
		print("Failed to find the patches. Please create them first!")
		return
	
	print("Applying patches...")

	if not os.path.isdir("patches"):
		os.mkdir("patches")
	
	f = open("downstream-changes", "r")

	line = f.readline().strip()

	while line != "":
		filename = line.split(",")[0].replace("oldmainline", "mainline")
		patch_filename = "patches/" + filename.replace("mainline/", "").replace("/", "_") + ".patch"

		os.environ["FILENAME"] = filename
		os.environ["PATCH_FILENAME"] = patch_filename

		os.system("patch -f -p0 ${FILENAME} ${PATCH_FILENAME} > /dev/null 2>&1")

		if os.path.isfile(filename + ".rej"):
			print(f"Failed to apply the patch for {filename}! Please review the .orig and .rej files and make changes accordingly!")

		line = f.readline().strip()
