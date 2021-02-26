#! /bin/sh 
ROUND=10000
POPULATION=4
echo "Zip sources"

zip -r project.zip *.py evolutionary/
echo "\n-- Run a --\n"
time python3 main.py -i assets/a.txt -o out_a.txt
echo "\n-- Run b --\n"
time python3 main.py -i assets/b.txt -o out_b.txt
echo "\n-- Run c --\n"
time python3 main.py -i assets/c.txt -o out_c.txt
echo "\n-- Run d --\n"
time python3 main.py -i assets/d.txt -o out_d.txt
echo "\n-- Run e --\n"
time python3 main.py -i assets/e.txt -o out_e.txt
echo "\n-- Run f --\n"
time python3 main.py -i assets/f.txt -o out_f.txt