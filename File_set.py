'''
    Objective: To Demonstrate Powerful File Handling in Python
    Author: Parag Raut
    Date Created: 27-1-2015
'''
def show_input_path(path_in):
    """To show the input path"""
    print 'File path provided is: ',path_in

def open_file_in_read_mode(path_in):
    """To show the contents of file"""
    f=open(path_in,'r')
    print 'Contents of file are: ',f.read()
    f.close()

def read_by_line(path_in):
    """To read contents of file by line"""
    f=open(path_in,'r')
    contents=f.readlines()
    print 'Contents of file are: '
    for line in contents:
        print line

def delete_contents_of_file(path_in):
    """To delete contents of file"""
    f=open(path_in,'w')
    print'File contents are deleted'
    f.close()

def write_new_text(path_in):
    """To write fresh file"""
    f=open(path_in,'w')
    new_text=raw_input('Enter your text here:>>> ')
    f.write(new_text)
    f.close()
    

def open_file_in_append_mode(path_in):
    """To perform append operation"""
    f=open(path_in,'a')
    user_input=raw_input('Enter your text here:>>> ')
    f.write(' ')
    f.write(user_input)
    f.close()

def count_length(path_in):
    """To count the letters in file"""
    f=open(path_in,'r')
    total_length=f.read()
    print'Total number of letters in file are: ',len(total_length)
    f.close()

def count_words(path_in):
    """To count the words"""
    f=open(path_in,'r')
    total_length=f.read()
    word_length=total_length.split()
    print'Total number of words in file are: ',len(word_length)
    f.close()

def cursor_position(path_in):
    """To show the cursor position in file"""
    f=open(path_in,'r')
    print 'Cursor position is at: ',f.tell()
    f.close()

def find_word(path_in):
    """To find the word in file"""
    f=open(path_in,'r')
    word_input=raw_input('Enter the search term: ')
    find_it=f.read()
    if word_input in find_it:
        print'Yes the word %s is in the mentioned file'%(word_input)
    else:
            print'Word %s is not present in mentioned file'%(word_input)
    f.close()

def find_with_cur_pos(path_in):
    """To find cursor position"""
    f=open(path_in,'r')
    word_input=raw_input('Enter the search term: ')
    find_it=f.read()
    if word_input in find_it:
        print'Yes the word %s is in the mentioned file'%(word_input)
        print'With cursor position: ',find_it.find(word_input)
    else:
            print'Word %s is not present in mentioned file'%(word_input)
    f.close()

def read_occurances(path_in):
    """To find occurances of word or letter"""
    f=open(path_in,'r')
    word_input=raw_input('Enter the search term: ')
    find_it=f.read()
    print 'The word "%s" is occured %d times in mentioned file'%(word_input,find_it.count(word_input))
    f.close()


    

if __name__=='__main__':
    print'------------------ Welcome To The File Handling Program ------------------ \n'
    print'################## Please Provide The Location Of File ################ \n'
    path_input=raw_input('Paste file link here:->>>')
    show_input_path(path_input)
    print'-----------------------------MENU-----------------------------'
    print'''
    1)Count the letters in text file
    2)Count the words in the file
    3)Tell the cursor position
    4)Find the word if its their in file or not
    5)Find the word and tell the cursor position
    6)Add something to file
    7)Delete the entire file and write new text
    8)Read the whole file
    9)Read file by line
    10)To count the number of occurances of word in file
    '''

    user_choice=int(raw_input('Enter your choice: '))
    if user_choice==1:
        count_length(path_input)
    
    elif user_choice==2:

        count_words(path_input)
    elif user_choice==3:
        cursor_position(path_input)
    elif user_choice==4:
        find_word(path_input)
    elif user_choice==5:
        find_with_cur_pos(path_input)
    elif user_choice==6:
        open_file_in_append_mode(path_input)
    elif user_choice==7:
        delete_contents_of_file(path_input)
        write_new_text(path_input)
    elif user_choice==8:
        open_file_in_read_mode(path_input)
    elif user_choice==9:
        read_by_line(path_input)
    elif user_choice==10:
        read_occurances(path_input)
    else:
        print'Please Provide Correct Input'
print __doc__
print'>>>By Parag Raut'
