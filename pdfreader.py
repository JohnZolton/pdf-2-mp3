from PyPDF2 import PdfReader
import pyttsx3
import os
import argparse
from tqdm import tqdm


def convert_pdf_to_mp3(input_path, output_path):
    reader = PdfReader(input_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    parts = []
    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        #print(f"{y}: {text}")
        if y < 600:
            parts.append(text)

    counter = 0
    engine = pyttsx3.init()
    for i in tqdm(range(len(reader.pages))):
        text = reader.pages[i].extract_text(visitor_text=visitor_body)
        if i % 30 == 0: 
            #print("".join(parts))
            file_path = os.path.join(output_path, f'{output_path}-{counter}.mp3')
            engine.save_to_file("".join(parts), file_path)
            counter += 1
            engine.runAndWait()
            parts = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a PDF to an MP3')
    parser.add_argument('pdf_file', type=str, help='name of input pdf file')
    parser.add_argument('mp3_file', type=str, help='name of file output')
    args = parser.parse_args()
    
    # Convert PDF to MP3
    convert_pdf_to_mp3(args.pdf_file, args.mp3_file)
    
    # Print success message
    print(f'Successfully converted {args.pdf_file} to {args.mp3_file}')