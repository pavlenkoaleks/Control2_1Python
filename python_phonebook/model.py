class Note:
    count_id =1
    
    def __init__(self, comment:str):
        self.comment = comment
        self.uid = Note.count_id
        Note.count_id +=1
    
    def __str__(self):
        return f'{self.uid}. {self.comment}'
    

    def for_search(self):
        return f'{self. comment}'.lower()

class NoteBook:
    def __init__(self,path:str) :
        self.notes:list[Note] = []
        self.path = path



    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8',errors='ignore') as file:
            data = file.readlines()
        for note in data:
            comment = note.strip()
            self.notes.append(Note(comment))
        

    def save_file(self):
        f = open('notes.txt','w', encoding='UTF-8',errors='ignore')
        for note in self.notes:
            f.write(note.comment)
            f.write('\n')
        f.close()



  


    def add_note(self,new: Note):
      
        self.notes.append(new)

    def search(self,word: str) -> list[Note]:
        result =[]
        for note in self.notes:
            
            if word.lower() in note.for_search():
                result.append(note)
                break
        return result

    def change(self,index:int ,new:str):
        for note in self.notes:
            if index==note.uid:
                note.comment = new 
                
                
                


    def delete(self,index:int):
        self.notes.pop(index-1)

    def change_id(self):
        counter=1
        for note in self.notes:
            note.uid = counter     
            counter+=1   

        






