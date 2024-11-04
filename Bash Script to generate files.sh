#!/bin/bash
read -p "What's your name?" NAME

# Initialize max file to 0
mfn=0

# Find the maximum file number already in use
for file in ${NAME}[0-9]*; do
   # Extract the number part from the filename
   num=${file#${NAME}}
   # Check if the extracted part is numeric and greater than the current max
   if [[ $num =~ ^[0-9]+$ ]] && [[ $num -gt $max ]]; then
      max=$num
   fi
done
echo "The maximum file number found is: $max"

# Create 25 files starting from max+1
for ((i=1; i<=25; i++)); do
    touch "${NAME}$((max+i))"
done
# Use natural sorting to display the created files
ls -lv
