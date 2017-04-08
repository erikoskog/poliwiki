
import slate
import os

def main():
    for file in os.listdir(os.getcwd()):
        if file.endswith('Protokoll.pdf'):
            attendees_names = []
            current_page = 0
            doc = slate.PDF(open(file), 'rb')
            folk = attendees(doc, current_page, attendees_names)
            print(file)
            print(folk)
            print(len(folk))


def attendees(doc, current_page, attendees_names):
    max_number_of_beginning_pages = 6
    if current_page < max_number_of_beginning_pages:
        page_text = doc[current_page]
        if 'RVARO' in page_text:
            for line in page_text.split('\n'):
                line = line.rstrip()
                line = line.lstrip()
                if ' ' in line and not hasNumbers(line) and hasLetters(line) and not 'OCH' in line \
                        and hasCapitalLetters(line) and not '=' in line:
                    attendees_names.append(line)
        current_page = current_page + 1
        if current_page == max_number_of_beginning_pages:
            return attendees_names
        else:
            attendees(doc, current_page, attendees_names)
            return attendees_names


def hasLetters(inputString):
    return any(char.isalpha() for char in inputString)


def hasCapitalLetters(inputString):
    return any(char.isupper() for char in inputString)


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


if __name__ == '__main__':
    main()
