# run this to create lists.py from input.txt

echo "in1 = []"
echo "in2 = []"

awk 'NR % 3 == 1 {print "in1.append("$0")"} NR % 3 == 2 {print "in2.append("$0")"} ' input.txt