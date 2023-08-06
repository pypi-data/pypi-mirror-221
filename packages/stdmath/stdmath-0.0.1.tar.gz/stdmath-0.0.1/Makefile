upload: build
	py -m pip install --upgrade twine
	py -m twine upload dist/*
build:
	py -m pip install --upgrade build
	py -m build
clean: upload
	Remove-Item -Path dist -Recurse