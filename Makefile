.PHONY : all clean settings help results

include config.mk

DATA=$(wildcard data/*.txt)
RESULTS=$(patsubst data/%.txt,results/%.csv,$(DATA))
SUMMARY=bin/book_summary.sh
MAKEFILE=./Makefile

## all : regenerate all results
# all : $(RESULTS)
all : results/collated.png

## results/collated.png: plot the collated results.
results/collated.png : results/collated.csv
	python $(PLOT) $< --outfile $@

## results/collated.csv : collate all results.
results/collated.csv : $(RESULTS) $(COLLATE)
	python $(COLLATE) $(RESULTS) > $@
	
## results/%.csv : regenerate result for any book.
# 这样能形成一对一的结果: csv-txt
results/%.csv : data/%.txt $(COUNT)
# @bash $(SUMMARY) $< Title
# @bash $(SUMMARY) $< Author
	python $(COUNT) $< > $@

## settings : show variables' values.
settings :
	@echo COUNT: $(COUNT)
	@echo DATA: $(DATA)
	@echo RESULTS: $(RESULTS)
	@echo COLLATE: $(COLLATE)
	@echo PLOT: $(PLOT)
	@echo BASH: $(SUMMARY)

# Remove all generated files.
clean :
	rm -rf $(RESULTS) results/collated.csv results/collated.png

## help : show this message.
help :
	@grep -E '^##' $(MAKEFILE) | sed -e 's/## //g' | column -t -s ':'