#include <stdio.h>
#include <stdlib.h>

/* Really simple turn scheduler example
 * Author: Craig Burnett
 * 
 * Usage:
 * ./turn_scheduler nm tm nc tc
 * 	nm = number of mice in the game
 * 	tm = number of turns EACH mouse should get
 * 	nc = number of cats in the game
 * 	tc = number of turns EACH cat should get
 * 
 * All command-line arguments are supposed to be positive integers.  No checking is done.
 * 
 */

int parseArgs(int argc, char **argv, int *n_mouse, int *t_mouse, int *n_cat, int *t_cat);
/* makes sure the correct number of c/l args are present, blithely assumes they are positive integers and 
attempts to return them by reference to the caller.  Returns 1 on success, 2 on failure. 
Blithely assumes all pointers are non-null and that each argv[i] is a well-formed positive integer.
*/

void showUsage(char *progname);
/* Prints usage information to stderr */

void move_cat(int which);
/* dummy function to represent an actual move executed by some cat actor */

void move_mouse(int which);
/* dummy function to represent an actual move executed by some mouse actor */

int gcd(int a, int b);
int lcm(int a, int b);


int main(int argc, char **argv) {
	int counter, period, mouse_trigger, cat_trigger;
	int next_mouse = 0, next_cat = 0;
	int 	n_mouse, /* number of mice in the game */
		t_mouse, /* number of turns EACH mouse gets per period */
		n_cat,   /* number of cats in the game */
		t_cat;   /* number of turns EACH cat gets per period */

	if (!parseArgs(argc, argv, &n_mouse, &t_mouse, &n_cat, &t_cat)) {
		showUsage(argv[0]);
		exit(1);
	}

	period = lcm(n_mouse * t_mouse,  n_cat * t_cat);
	mouse_trigger = period/(t_mouse * n_mouse);
	cat_trigger = period/(t_cat * n_cat);

	/* printf("Period = %d\tmouse_trigger = %d\tcat_trigger = %d\n\n", period, mouse_trigger, cat_trigger); */

	for(counter = 0; /* you're going to have to kill this */ ; counter = (counter+1) % period) {
		int printed = 0;
		if (counter % cat_trigger == 0) {
			/* Some cat gets to move. */
			move_cat(next_cat);
			next_cat = (next_cat+1) % n_cat;
			printed = 1;
		}
		if (counter % mouse_trigger == 0) {
			if (printed) printf("and\t");
			move_mouse(next_mouse);
			next_mouse = (next_mouse+1) % n_mouse;
			printed = 1;
		}
		if (printed) {
			printf("\n");
			sleep(1);
		}
	}

	return 0;

}

int parseArgs(int argc, char **argv, int *n_mouse, int *t_mouse, int *n_cat, int *t_cat) {
	if (argc < 5) {
		return 0;
	}
	*n_mouse = atoi(argv[1]);
	*t_mouse = atoi(argv[2]);
	*n_cat = atoi(argv[3]);
	*t_cat = atoi(argv[4]);
	return 1;
}

void showUsage(char *progname) {
	fprintf(stderr, "Usage:\n%s nm tm nc tc\n", progname);
	fprintf(stderr, "\tnm = number of mice in the game\n");
	fprintf(stderr, "\ttm = number of turns EACH mouse should get per period\n");
	fprintf(stderr, "\tnc = number of cats in the game\n");
	fprintf(stderr, "\ttc = number of turns EACH cat should get per period\n\n");
}

void move_cat(int which) {
	printf("Cat[%d] moves\t", which);
}

void move_mouse(int which) {
	printf("Mouse[%d] moves\t", which);
}

int gcd(int a, int b) {
	int r;
	while (b) {
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int lcm(int a, int b) {
	return a*b/gcd(a,b);
}

