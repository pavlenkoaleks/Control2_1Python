from .text import *
from model import NoteBook, Note

def menu() -> int :
    print(main_menu)
    while True:
       choice = input(menu_choice)
       if choice.isdigit() and 0 <int(choice)<9:
            return int(choice)
       print(input_error)

def print_message(message: str):
    length = len(message)
    print('\n'+ '='*length)
    print(message)
    print('='*length + '\n')


def show_notes(book: NoteBook):
    if book.notes: 
        #print('\n'+ '='*67)
        for note in book.notes:
            
            print(note.uid, ".",note.comment)
        #print('='*67 + '\n')
    else:
        print(book_error)

#def input_note(message: str) -> dict[str,str]:
   # print(message)
   # new = Note (input(new_note))
    #return new

def input_return(message:str) ->str:
  
    return input(message)