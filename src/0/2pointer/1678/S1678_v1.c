char * interpret(char * command){
    int i = 0, j = 0;
    while (i < strlen(command)) {
        if (command[i] == '(') {
            if (command[i+1] == ')') {
                i += 2;
                command[j++] = 'o';
            } else {
                i += 4;
                command[j++] = 'a';
                command[j++] = 'l';
            }
        } else {
            i++;
            command[j++] = 'G';
        }
    }
    command[j] = 0;
    return command;
}
