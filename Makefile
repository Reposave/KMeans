install: venv 
		. venv/bin/activate; pip3 install -Ur requirements.txt
venv :
	test -d venv || python3 -m venv venv
 
clean:
	rm -rf venv
	find -iname "*.pyc" -delete
 
run:
	@python3 kmeans.py
	
runtxt:
	@python3 kmeans.py > answers.txt
	
run1:
	@python3 kmeans.py thresh.txt > results.txt
