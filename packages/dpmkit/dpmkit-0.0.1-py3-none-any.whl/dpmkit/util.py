#	dpmkit - dpmkit/__main__.py
#
#	Copyright (C) 2023 hexaheximal
#	Copyright (C) 2023 JustSoup321
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

import tarfile

def get_kernel_directory(filename):
	print("Figuring out where the kernel directory is in the tarball...")

	t = tarfile.open(filename)
	files = t.getnames()
	t.close()

	root_paths = []

	for path in files:
		root_path = path.split("/")[0]

		if not root_path in root_paths:
			root_paths.append(root_path)
	
	if len(root_paths) == 1:
		return root_paths[0]
	
	return None
