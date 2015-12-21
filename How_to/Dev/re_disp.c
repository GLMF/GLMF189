//	@(#)	[MB] cv_re_disp.c	Version 1.1 du 15/10/16 - 
#include  <stdio.h>
#include  <stdlib.h>

int main(int argc, char *argv[])
{
     char           *_regexp, *_string;

     if (argc != 3) {
          fprintf(stderr, "Usage: %s expression_reguliere chaine\n",
                  argv[0]);
          exit(1);
     }
     _regexp        = argv[1];
     _string        = argv[2];

     printf("Expression Reguliere = [%s]\n", _regexp);
     printf("Chaine               = [%s]\n", _string);

     return 0;
}
