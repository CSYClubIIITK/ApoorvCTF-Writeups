#include <stdio.h>
#include <string.h>

#define PASSWORD "letmein"
#define MAX_PASSWORD_LENGTH 22
#define XOR_KEY 0x7f

void decrypt_file(const char* boxname, const char* big_boxname) {
    FILE* box = fopen(boxname, "r");
    FILE* big_box = fopen(big_boxname, "w");
    if (box == NULL || big_box == NULL) {
        printf("Nothing to see here\n");
        return;
    }
    
    int ch;
    while ((ch = fgetc(box)) != EOF) {
        ch ^= XOR_KEY; 
        fputc(ch, big_box);
    }
    
    fclose(box);
    fclose(big_box);
}

void check_password(char *password) {
    char buffer[MAX_PASSWORD_LENGTH + 1];
    int authenticated = 0;
    
    if (strlen(password) > MAX_PASSWORD_LENGTH) {
        decrypt_file("flag.enc", "flag.txt"); 
        printf("Revelio......Decrypted flag.enc to flag.txt.\n");
        printf("This way master ......\n");
    }
    
    strncpy(buffer, password, MAX_PASSWORD_LENGTH);
    buffer[MAX_PASSWORD_LENGTH] = '\0';
    
   /* if (strcmp(buffer, PASSWORD) == 0) {
        authenticated = 1;
    }
    
    if (authenticated) {
        printf("YOU SHALL NOT PASS !!!!\n"); */
    
}

int main() {
    char name[32];
    printf("And who are you that dare to cross,asked the genie : \n");
    fgets(name, 32, stdin);
    check_password(name);
    
    return 0;
}
