/*
I am making this change to this program
I added a statement that tells the size of the array (variable called "length".
Next I added it to replace the number so that it is more generalied.
Finally I printed this length

-Mukesh Taank
*/

#include <stdio.h>
#include "average.h"

int main() {
    int length;
    double arr[] = {1.0, 2.0, 3.0, 4.0};
    
    length = sizeof(arr)/sizeof(arr[0]);
    printf("The amount of elements in the array is: %d\n", length);

    double result = average(length, arr);
	
    printf("The average of 1, 2, 3 and 4 is: %.4f!!!\n", result);
    return 0;    
}

