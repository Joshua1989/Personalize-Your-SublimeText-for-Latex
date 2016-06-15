# ST2/ST3 compat
from __future__ import print_function
import sublime
if sublime.version() < '3000':
	_ST3 = False
	# we are on ST2 and Python 2.X
	import getTeXRoot

	from latextools_utils import cache, get_setting
else:
	_ST3 = True
	from . import getTeXRoot
	from .latextools_utils import cache, get_setting


import sublime_plugin
import os

import traceback


class ClearLocalLatexCacheCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.active_view()

		tex_root = getTeXRoot.get_tex_root(view)
		if tex_root:
			try:
				cache.delete_local_cache(tex_root)
			except:
				print('Error while trying to delete local cache')
				traceback.print_exc()


class DeleteTempFilesCommand(sublime_plugin.WindowCommand):
	def run(self):
		# Retrieve root file and dirname.
		view = self.window.active_view()

		root_file = getTeXRoot.get_tex_root(view)
		if root_file is None:
			sublime.status_message('Could not find TEX root. Please ensure that either you have configured a TEX root in your project settings or have a LaTeX document open.')
			print('Could not find TEX root. Please ensure that either you have configured a TEX root in your project settings or have a LaTeX document open.')
			return

		if not os.path.isfile(root_file):
			message = "Could not find TEX root {0}.".format(root_file)
			sublime.status_message(message)
			print(message)
			return

		# clear the cache
		try:
			cache.delete_local_cache(root_file)
		except:
			print('Error while trying to delete local cache')
			traceback.print_exc()

		path = os.path.dirname(root_file)

		# Load the files to delete from the settings
		temp_files_exts = get_setting('temp_files_exts',
			['.blg', '.bbl', '.aux', '.log', '.brf', '.nlo', '.out', '.dvi',
			 '.ps', '.lof', '.toc', '.fls', '.fdb_latexmk', '.pdfsync',
			 '.synctex.gz', '.ind', '.ilg', '.idx'])

		ignored_folders = get_setting('temp_files_ignored_folders',
			['.git', '.svn', '.hg'])
		ignored_folders = set(ignored_folders)

		for dir_path, dir_names, file_names in os.walk(path):
			dir_names[:] = [d for d in dir_names if d not in ignored_folders]
			for file_name in file_names:
				for ext in temp_files_exts:
					if file_name.endswith(ext):
						file_name_to_del = os.path.join(dir_path, file_name)
						if os.path.exists(file_name_to_del):
							try:
								os.remove(file_name_to_del)
							except OSError:
								# basically here for locked files in Windows,
								# but who knows what we might find?
								print('Error while trying to delete {0}'.format(file_name_to_del))
								traceback.print_exc()
						# exit extension
						break

		sublime.status_message("Deleted temp files")
