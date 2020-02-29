#include <stdio.h>
#include <stdlib.h>

void incomment()
{
    int c,d;
    
    c = getchar();
    d = getchar();

    while(c != '*' || d != '/')
    {
        c = d;
        d = getchar();
    }
}

void inquote(int c)
{
    int d;

    putchar(c);

    while((d=getchar())!=c)
        if( d == '\\')
            getchar();
}

void search(int c)
{
    extern int brace,bracket,parente;

    if ( c == '{')
        --brace;
    else if ( c == '}')
        ++brace;
    else if( c == '(')
        --bracket;
    else if( c == ')')
        ++bracket;
    else if( c == '[')
        --parente;
    else if( c == ']')
        ++parente;
}

int main(){

    int brace,bracket,parente;
    void incomment();
    void inquote(int c);
    void search(int c);

   char ch, file_name[25];
   FILE *fp;

   printf("Enter name of a file you wish to see\n");
   gets(file_name);

   fp = fopen(file_name, "r"); // read mode

   if (fp == NULL)
   {
      perror("Error while opening the file.\n");
      exit(EXIT_FAILURE);
   }

   printf("The contents of %s file are:\n", file_name);

   while((ch = fgetc(fp)) != EOF)
      printf("%c", ch);

   //checking
   int c;

   while((c=getchar())!=EOF)
        if( c == '/')
            if((c=getchar())== '*')
                incomment();
            else 
                search(c);
        else if( c == '\'' || c == '"')
            inquote(c);
        else
            search(c);

    if( brace < 0)
    {
        printf("Unmatched Braces\n");
        brace = 0;
    }   
    else if( bracket < 0)
    {
        printf("Unmatched brackets\n");
        bracket = 0;
    }
    else if( parente < 0)
    {
        printf("Unmatched parenthesis\n");
        parente = 0;
    }
    
    if(brace > 0)
        printf("Unmatched braces\n");
    else if(bracket > 0)
        printf("Unmatched brackets\n");
    else if(parente > 0)
        printf("Unmatched parenthesis\n"); 

    fclose(fp);
    
    return 0;

    
}