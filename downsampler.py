import csv
import sys

def downsample(input_file, output_file, factor):
    """
    Downsamples IoT data by taking every N-th sample 
    to reduce storage while keeping trend integrity.
    """
    try:
        with open(input_file, 'r') as fin, open(output_file, 'w', newline='') as fout:
            reader = csv.reader(fin)
            writer = csv.writer(fout)
            
            for i, row in enumerate(reader):
                if i % factor == 0:
                    writer.writerow(row)
        
        print(f"Success! Data reduced by factor of {factor} and saved to {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Usage: python downsampler.py input.csv output.csv factor
    if len(sys.argv) == 4:
        downsample(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
        print("Usage: python downsampler.py <input> <output> <factor>")

