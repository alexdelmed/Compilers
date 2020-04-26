#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/***************************
Example:
abbbbbc
abbbb
abc
abcbcbcc
ac
Grammar:
S -> aBc
B -> bc | b
Graphiz web page: 
http://www.webgraphviz.com/
***************************/

void S();
void B();

char buff[255];
int i, error;
int j = 0;

int main(){
	printf("This is the input of tokens.txt\n")
	
	FILE *fp;
	
	FILE *f;
    f=fopen("tokens.txt", "rt");

    while((buff[j]=fgetc(f))!=EOF){
        printf("%c",buff[j]);
        j++;
    }

    fclose(f);
    return 0;
	
	S();
	
	if(i==strlen(buff)&&error==0){
		printf("String is Accepted\n");
		printf("Now take your string, and put it in Graphviz\n");
		printf("String:\n");
		printf("digraph G {\n");
		printf(""S" -> "a"\n");
		printf(""S" -> "B"\n");
		printf(""B" -> "bc"\n");
		printf(""S" -> "c"\n");
		printf(""B" -> "c"\n");
		printf("}\n");s
		
	}
	else{
		printf("String is not Accepted\n");
	}
}

void S(){
	B();
	if(buff[i]=="a"){
		i++
		if(buff[i]=="B"){
			void B();
		}
	}
	if(buff[i]=="c"){
		i++
	}
	
}

void B(){
	
	if(buff[i]=="b"){
		i++;
		if(buff[i]=="c"){
			i++
		}
	}
}



