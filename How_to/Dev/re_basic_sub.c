//	@(#)	[MB] cv_re_basic_sub.c	Version 1.1 du 15/10/16 - 
#include  <stdio.h>
#include  <stdlib.h>
#include  <sys/types.h>
#include  <regex.h>

#define   SIZE           (1024)

int main(int argc, char *argv[])
{
     char           *_regexp, *_string;
     regex_t         _reg;
     int             _cflags, _eflags, _i, _s, _e;
     size_t          _nmatch;
     regmatch_t      _pmatch[SIZE];

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
     _nmatch        = sizeof(_pmatch) / sizeof(_pmatch[0]);
     if (regexec(&_reg, _string, _nmatch, _pmatch, _eflags) == 0) {
          printf("Correspondance entre \"%s\" et \"%s\"\n", _string, _regexp);

          for (_i = 0; _pmatch[_i].rm_so != -1; _i++) {
               _s   = _pmatch[_i].rm_so;
               _e   = _pmatch[_i].rm_eo - 1;

               printf("Correspondance %2d : debut = %2d, fin = %2d, valeur = [%.*s]\n",
                      _i, _s, _e, _e - _s + 1, _string + _s);
          }
     }
     else {
          printf("Pas de correspondance entre \"%s\" et \"%s\" !\n", _string, _regexp);
     }

     return 0;
}
