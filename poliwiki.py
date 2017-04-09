from pyPdf import PdfFileReader
import slate

def main():
    # for file in os.listdir(os.getcwd()):
    #     if file.endswith('Protokoll.pdf'):
    #         attendees_names = []
    #         current_page = 0
    #         doc = slate.PDF(open(file), 'rb')
    #         folk = attendees(doc, current_page, attendees_names)
    protocol_path = 'Kf160222Protokoll.pdf'
    kiruna_test = CouncilMeeting(protocol_path)
    this_attendees = kiruna_test.attendees()
    print(len(this_attendees))
    print(this_attendees)
    attending_parties = kiruna_test.attending_parties()
    print(len(attending_parties))
    print(attending_parties)
    # atteding_parties and this_attendees has different length!
    dict_test = dict(zip(this_attendees, attending_parties)) # wrong!
    print(dict_test)




class CouncilMeeting(object):
    # A Kiruna council meeting.
    #
    # Attributes:
    #   protocol_path: A string representing the path to the PDF protocol
    #   current_page: Int representing the current page of the PDF
    #   max_number_of_beginning_pages: Int(constant) of how many beginning pages the protocol contains
    #
    # Methods:
    #   attendees: returns the names of the people who were attending the meeting as a vector
    #   attending_parties: returns a list of which parties was attending the council meeting(with multiples).

    def __init__(self, protocol_path):
        self.max_number_of_beginning_pages = 6
        self.protocol_path = protocol_path
        self.current_page = 0
        self.doc = slate.PDF(open(protocol_path), 'rb')
        self.attendees_names = []
        self.party_affiliation = []
        self.possible_parties = ['MP', 'S', 'V', 'KNEG', 'C', 'M', 'SL', 'FI', 'NS', 'KIP', 'SD', 'KD']

    def attendees(self):
        if self.current_page < self.max_number_of_beginning_pages:
            page_text = self.doc[self.current_page]
            if 'RVARO' in page_text:
                for line in page_text.split('\n'):
                    line = line.rstrip()
                    line = line.lstrip()
                    if( ' ' in line and not
                            has_numbers(line) and
                            has_letters(line) and not
                            'OCH' in line and
                            has_capital_letters(line) and not
                            '=' in line):
                        self.attendees_names.append(line)
            self.current_page = self.current_page + 1
            if self.current_page == self.max_number_of_beginning_pages:
                self.current_page = 0
                return self.attendees_names
            else:
                self.attendees()
                return self.attendees_names

    def attending_parties(self):
        if self.current_page < self.max_number_of_beginning_pages:
            page_text = self.doc[self.current_page]
            if 'RVARO' in page_text:
                for line in page_text.split('\n'):
                    line = line.rstrip()
                    line = line.lstrip()
                    if ((line in self.possible_parties) and
                            has_capital_letters(line) and not
                    has_numbers(line) and not
                    has_lowercase_letters(line)):
                        self.party_affiliation.append(line)
            self.current_page = self.current_page + 1
            if self.current_page == self.max_number_of_beginning_pages:
                self.current_page = 0
                return self.party_affiliation
            else:
                self.attending_parties()
                return self.party_affiliation


def has_letters(inputString):
    #   has_letters: checks if a string contains letters. Returns boolean.
    return any(char.isalpha() for char in inputString)


def has_capital_letters(inputString):
    #   has_capital_letters: checks if string contains capital letters. Returns boolean.
    return any(char.isupper() for char in inputString)

def has_lowercase_letters(inputString):
    #   has_lowercase_letters: checks if string contains lowercase letters. Returns boolean.
    return any(char.islower() for char in inputString)

def has_numbers(inputString):
    #   has_numbers: checks if string contains numbers. Returns boolean
    return any(char.isdigit() for char in inputString)


def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def get_number_of_pages(path):
    #   get_number_of_pages: takes path as input and returns number of pages of protocol
    pdf = PdfFileReader(open(path, 'rb'))
    number_of_pages = pdf.getNumPages()
    return number_of_pages


def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""


if __name__ == '__main__':
    main()
