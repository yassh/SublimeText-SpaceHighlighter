import sublime, sublime_plugin

class SpaceHighlighter(sublime_plugin.EventListener):
	def highlight(self, view):
		view.add_regions(
			key = 'spacehighlighter_tabs',
			regions = view.find_all(r'\t'),
			scope = "comment",
			flags = sublime.DRAW_NO_FILL + sublime.DRAW_NO_OUTLINE + sublime.DRAW_STIPPLED_UNDERLINE,
		)
		
		view.add_regions(
			key = 'spacehighlighter_ideographicspaces',
			regions = view.find_all(r'　'),
			scope = "comment",
			flags = sublime.DRAW_NO_FILL,
		)
		
		view.add_regions(
			key = 'spacehighlighter_trailingspaces',
			regions = view.find_all(r'[ ]*((?=\n)|$)'),
			scope = "comment",
			flags = sublime.DRAW_NO_OUTLINE,
		)
	
	# Called after changes have been made to a view.
	# @override
	def on_modified(self, view):
		self.highlight(view)
	
	# Called when a view gains input focus.
	# @override
	def on_activated(self, view):
		self.highlight(view)
	
	# Called when the file is finished loading.
	# @override
	def on_load(self, view):
		self.highlight(view)
