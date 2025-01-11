import PyPDF2

signs = [",", ".", "?", ")", "("]

def pdf_to_txt(pdf_file_path, txt_file_path, max_line_length=79):
    """ Selection of pdf words in a txt file. """

    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:

            for page_num, page in enumerate(pdf_reader.pages, start=1):

                text = page.extract_text()
                text = text.lower()

                if text:
                    
                    for sign in signs:
                        text = text.replace(sign, " ")
                    words = text.split()
                    current_line = ""

                    for word in words:
                        if not word.isalpha() or len(word) < 4:
                            continue

                        if len(current_line) + len(word) + 1 <= max_line_length:
                            if current_line:
                                current_line += " "
                            current_line += word
                        else:

                            txt_file.write(current_line + "\n")
                            current_line = word


                    if current_line:
                        txt_file.write(current_line + "\n")
                                
                print(f"\rProgress {int(page_num / total_pages * 100)}%", end="")

def get_pdf_page_count(pdf_file_path):
    """ Getting the total number of pdf pages. """
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        total_pages = len(pdf_reader.pages)

    return total_pages

if __name__ == "__main__":
    pdf_file_path = 'N. Khare - Docker Cookbook.pdf'
    
    total_pages = get_pdf_page_count(pdf_file_path)
    txt_file_path = 'output.txt'
    pdf_to_txt(pdf_file_path, txt_file_path)
    print(f"\rТекст из '{pdf_file_path}' успешно извлечен в '{txt_file_path}'")
