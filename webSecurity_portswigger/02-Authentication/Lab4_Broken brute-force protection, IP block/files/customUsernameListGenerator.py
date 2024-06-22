def insert_word_between_lines(input_file, output_file, word):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for i in range(len(lines)-1):
            file.write(word + '\n' + 'carlos' + '\n')
        file.write(word+ '\n' + 'carlos' )

input_file = '../givens/Candidate passwords.txt' # to generate list have same words as passwords list
output_file = 'customUsernameList.txt'
word = 'wiener' #my valid account username

insert_word_between_lines(input_file, output_file, word)
