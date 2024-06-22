def insert_word_between_lines(input_file, output_file, word):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for i in range(len(lines)-1):
            file.write(word + '\n' + lines[i].strip() + '\n')
        file.write(word + '\n' + lines[-1].strip())
                            
        


input_file = '../givens/Candidate passwords.txt'
output_file = 'customPasswordList.txt'
word = 'peter' #my valid account password

insert_word_between_lines(input_file, output_file, word)
