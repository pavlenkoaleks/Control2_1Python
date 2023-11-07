from view import menu,show_notes,print_message,input_return
import model
from view import text
def start():
   pb=model.NoteBook('notes.txt')
   while True:
       choice = menu()
       match choice:
           case 1:
                pb.open_file()
                print_message(text.open_successfull)
           case 2:
             pb.save_file()
           case 3:
                show_notes(pb)
                
           case 4:
             new = input_note(text.input_new_note)
             pb.add_note(new)
             print_message(text.note_saved())
           case 5:
             print_message(text.input_index)
             index = int(input())
             print_message(text.input_change_note)
             new = str(input())
             pb.change(int(index),new)
             print_message(text.note_changed())
             pb.change_id()
           case 6:
             print_message(text.delete_index)
             index = int(input())
             pb.delete(int(index))
             print_message(text.note_deleted())
             pb.change_id()
           case 7:
             break