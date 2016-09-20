from wta_app import db


def add_then_commit(*args):
	""" Adds arbitrary amount and saves to db

	Args:
		*args: Value of objects to add & save.
	"""
	for arg in args:
		db.session.add(arg)
	db.session.commit()


PIE_COLORS = [
	'#4bb3d2',
	'#d94d4d',
	'#eba538',
	'#87ab66',
	'#3e3e3d',
	'#c3c1b5'
]
