//	@(#)	[MB] cv_re_basic.c	Version 1.1 du 15/10/16 - 
#include  <stdio.h>
#include  <stdlib.h>
#include  <sys/types.h>
#include  <regex.h>

int main(int argc, char *argv[])
{
     char           *_regexp, *_string;
     regex_t         _reg;
     int             _cflags, _eflags;

     if (argc != 3) {
          fprintf(stderr, "Usage: %s expression_reguliere chaine\n",
                  argv[0]);
          exit(1);
     }
     _regexp        = argv[1];
     _string        = argv[2];

     printf("Expression Reguliere = [%s]\n", _regexp);
     printf("Chaine               = [%s]\n", _string);

     _cflags        = 0;
     if (regcomp(&_reg, _regexp, _cflags) != 0) {
          fprintf(stderr, "%s: erreur de compilation de l'expression reguliere !\n",
                  argv[0]);
          exit(2);
     }

     _eflags        = 0;
     if (regexec(&_reg, _string, 0, 0, _eflags) == 0) {
          printf("Correspondance entre \"%s\" et \"%s\"\n", _string, _regexp);
     }
     else {
          printf("Pas de correspondance entre \"%s\" et \"%s\" !\n", _string, _regexp);
     }

     return 0;
}
