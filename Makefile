RM		= rm -rf

all:	CHANGES.rst test coverage

CHANGES.rst:
	git log --oneline --pretty=format:"* %ad: %s\n" --date=short > CHANGES.rst

test:
	nosetests

coverage:
	coverage run uSphinx
	coverage html

docs:
	cd docs && make html

clean:
	$(RM) docs/_build

.PHONY: all test coverage docs clean

