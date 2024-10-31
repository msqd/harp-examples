.PHONYU: check

check:
	(cd .check; poetry install; poetry run python -m check)

