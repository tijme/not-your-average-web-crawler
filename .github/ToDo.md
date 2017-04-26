# 1.4.0
* Use hash table as queue
* Fix unit-tests

# 1.4.1
* Option to include or exclude location.hash
* Scrapers
        - CSS
		- JavaScript
		- JSON
		- SVG
		- XHR

	
# Backlog
* Scrapers
		- XHR
* Optimize time complexity of several methods.
* Support rate limiting.
* Refactor for single responsibility.
* Use random user agent by default.

# Creating new release
* git checkout master
* git merge develop
* git push origin master
* python setup.py sdist
* twine upload dist/*
* Update version
