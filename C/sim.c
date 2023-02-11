#include <assert.h>
#include <stdio.h>
#include "lib.h"

int main() {
    assert(3 == sum(1,2));
    printf("seems to work\n");
    return 0;
}