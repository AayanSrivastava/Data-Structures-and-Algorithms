#include<stdio.h>
void hangman(char [], char []);
int main()
{
	char word[20]={'l','i','o','n'};
	char guessed[20];
	hangman(word,guessed);
	getch();
	return 0;
}
void hangman(char answer[],char guess[])
{
	int c=0,x=0,n=6;
	char letter;
	while(x<6)
	{
		printf("Guess the letters\n");
		scanf(" %c",&letter);
		n--;
		c++;
		if(letter==answer[x])
		{
			guess[x]=letter;
			printf("Keep going\n");
			printf("You have %d chances left\n",n);
			if(c==4)
			{
			printf("Congrats! You Won\n");
			break;
			}
		}
			else
			{
			printf("Wrong input\n",n);	
			printf("You have %d chances left\n",n);
			}
		++x;
		if(c==6)
		printf("Game Over! Try Again\n");
	}
}
