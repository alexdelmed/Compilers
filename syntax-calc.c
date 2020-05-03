%{
#include <stdio.h>
FILE *yyin;
int regs[26];
int base;
/*  la regla
S -> aBc
B -> bc | b
*/
%}
%start list 
%token TA TB TC TCE
%%                   /* inicia of rules*/
list:                       
         |
        list S '\n'
         |
        list error '\n'
         {
           yyerrok;
         }
         ;

S : TA B TCE   { printf("Parsing Successful\n"); exit(1);}
  | TA TB TCE  { printf("Parsing Successful\n"); exit(1);}
;

B : TB TC 
;
%%

void main(){
    return(yyparse());
}

yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}
yywrap()
{
  return(1);
}
