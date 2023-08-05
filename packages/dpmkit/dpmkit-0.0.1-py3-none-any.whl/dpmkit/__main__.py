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

from . import *
import sys

def main():
	args = []
	options = {}

	for arg in sys.argv[1:]:
		if arg.startswith("--"):
			option = arg[2:]

			if "=" in arg:
				split_at = option.index("=")
				options[option[0:split_at]] = option[split_at+1:]
				continue
			
			options[option] = True

			continue

		args.append(arg)
	
	if len(args) == 0:
		print("No subcommand specified!")
		return
	
	subcommand = args[0]
	
	if subcommand == "fetch-mainline":
		if len(args) != 2:
			print("Invalid number of arguments.")
			return
		
		fetch_kernel(args[1], "mainline")
		return
	
	if subcommand == "fetch-oldmainline":
		if len(args) != 2:
			print("Invalid number of arguments.")
			return
		
		fetch_kernel(args[1], "oldmainline")
		return
	
	if subcommand == "fetch-downstream":
		if len(args) != 2:
			print("Invalid number of arguments.")
			return
		
		fetch_kernel(args[1], "downstream")
		return
	
	if subcommand == "patch":
		create_patch()
		return
	
	if subcommand == "apply":
		apply_patch()
		return
	
	print(f"The subcommand {subcommand} does not exist.")
	exit(1)
	
if __name__ == "__main__":
	main()
