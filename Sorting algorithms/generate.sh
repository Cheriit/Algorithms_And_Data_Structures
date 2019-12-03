#!/bin/bash
STEP=10
FILE="./results/$(echo $1 | cut -d'.' -f1).txt"
echo -e "RESULTS $1\n" >> $FILE

for i in {1000..5000..1000}
do
	python generateExamples.py $i $STEP
	echo -e "\nSIZE $i\n$(python $1)" >> $FILE
done
