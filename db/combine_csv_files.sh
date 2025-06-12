#! /bin/sh

# This script combines all *.csv files in a given directory into a single CSV file.
# Usage: ./generate_data_csv.sh <directory_path> <output_file>

#REQUIREMENT: All CSV FILES MUST HAVE THE SAME STRUCTURE !!!!!!

#Parse Command Line Options
show_help() {
  echo "Usage: $0 [-h] [-i input_folder] [-o output_file] [--] [args...]"
  echo
  echo "Options:"
  echo "  -h, --help        Show this help message and exit"
  echo "  -i input_folder   Input Folder containing CSV files"
  echo "  -o output_file    Specify the output file name"
}
OPTIND=1         # Reset in case getopts has been used previously in the shell.

while getopts "i:o:h" opt; do
  case "$opt" in
    h)
      show_help
      exit 0
      ;;
    i)  input_folder=$OPTARG
      ;;
    o)  output_file=$OPTARG
      ;;
  esac
done

# Check for required options
if [ -z "$input_folder" ] || [ -z "$output_file" ]; then
  echo "[ERROR] -i input_folder and -f output_file are required."
  show_help
  exit 1
fi

shift $((OPTIND-1))

[ "${1:-}" = "--" ] && shift

echo "input_folder=$input_folder"
echo "output_file='$output_file"


# Check if input_folder exists and is a directory
if [ ! -d "$input_folder" ]; then
  echo "[ERROR]: Input folder '$input_folder' does not exist or is not a directory."
  exit 2
fi

# Check if input folder contains CSV files
if [ $(ls ${input_folder}/*.csv|wc -l) -eq 0 ]; then
  echo "[ERROR]: No CSV files found in the input folder '$input_folder'."
  exit 2
fi

if [ -f "$output_file" ]; then
  echo "[WARN]: Output file '$output_file' already exists and will be overwritten."
  rm "$output_file"
fi

# Define Column headers
expected_columns="asset_name;asset_category;english_word;german_word;italian_word;image_filename;file_type;image_width;image_height;source;download_url;download_date;license;license_version_date;license_pdf_url;attribution_text;attribution_html;english_audio_filename;german_audio_filename;italian_audio_filename"
echo "$expected_columns" > $output_file

# Iterate over all csv files and combine them into the output file
for file in $(ls ${input_folder}/*.csv); do
  # abort if the csv file is empty
  if [ $(cat $file|wc -l) -eq 0 ]; then
    echo "[ERROR]: $file is empty."
    exit 2
  else
    echo "[OK] Processing file: $file"
    #convert line endings to Unix format
    sed -i 's/\r$//' $file
    #check if csv columns match expected structure
    actual_columns=$(head -n 1 $file| tr -d '\r' | tr -d '\n' )
    
    if [ "$actual_columns" != "$expected_columns" ]; then
      echo "[ERROR]: $file does not match the expected CSV structure."
      echo "EXPECTED: $expected_columns" 
      echo "ACTUAL:   $actual_columns"
      exit 2
    else
      tail -n +2 $file >> $output_file
      echo "[OK] File $file processed successfully."
    fi
  fi
done
