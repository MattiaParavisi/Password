#include<stdio.h>
#include <string.h>


int main(void){
	char alfabeto[26] = {'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	char parola[6] = {};
	char c1,c2,c3,c4,c5;
	int c = 0;
	
	for(int i = 0; i < 26; i++){
		for(int j = 0; j < 26; j++){
			for(int k = 0; k < 26; k++){
				for(int l = 0; l < 26; l++){
					for(int m = 0; m < 26; m++){
						c1 = alfabeto[i];
						c2 = alfabeto[j];
						c3 = alfabeto[k];
						c4 = alfabeto[l];
						c5 = alfabeto[m];
						parola[0] = c1;
						parola[1] = c2;
						parola[2] = c3;
						parola[3] = c4;
						parola[4] = c5;
						parola[5] = '\0';
						c ++; 
						printf("%d \n", c);
						
						/*printf("%s \n", parola);
						if(strcmp(parola, "aaaaz") == 0){
							return 0;
						}*/
					}
				}
			}
		}
	}
	
}
