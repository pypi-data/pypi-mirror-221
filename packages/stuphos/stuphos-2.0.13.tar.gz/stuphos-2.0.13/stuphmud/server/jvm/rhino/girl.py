from . import getRhinoEngine as _getEngine
def evaluate(frame, script):
	# confine evaluation to namespace attached to frame.task.
	return _getEngine().eval(script)
