TOX		= tox
RM		= rm -rf

all:	CHANGES.rst test coverage

CHANGES.rst:
	git log --oneline --pretty=format:"* %ad: %s\n" --date=short > CHANGES.rst

test:
	$(TOX) -c tox.ini -e test

coverage:
	$(TOX) -c tox.ini -e coverage

docs:
	cd docs && make html

clean:
	$(RM) docs/_build

.PHONY: all test coverage docs clean

