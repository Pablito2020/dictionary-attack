all: assignment

assignment: 
	xelatex -shell-escape assignment.tex
	biber assignment
	xelatex -shell-escape assignment.tex

clean:
	rm -rf *.aux *.toc *.log *.out *.lof *.lot *.nav *.snm *.bbl *.bcf *.blg *.run.xml

