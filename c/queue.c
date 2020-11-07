/*
 * Implementation of a simple circular (LIFO) queue.
 */

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define QUEUE_SIZE (5UL)

typedef struct
{
    int newest;
    int num;
    int mem[QUEUE_SIZE];
} queue_t;

static queue_t* create(void)
{
    queue_t* q = (queue_t*) malloc(sizeof(queue_t));
    memset(q->mem, 0, QUEUE_SIZE * sizeof(int));
    q->newest = 0;
    q->num = 0;
    return q;
}

static void delete(queue_t* q)
{
    free(q);
}

static int get_oldest_index(queue_t* q)
{
    int oldest = q->newest - q->num;
    oldest = (oldest < 0) ? QUEUE_SIZE + oldest : oldest;
    return oldest;
}

/* Insert into newest location, overwriting oldest if queue is full */
static void enqueue(queue_t* q, int element)
{
    q->mem[q->newest] = element;
    q->newest = (q->newest + 1) % QUEUE_SIZE;
    q->num = (q->num == QUEUE_SIZE) ? q->num: q->num + 1;
}

/* Remove from oldest location, if there are any elements in the queue */
static int dequeue(queue_t* q)
{
    int element = -1;
    if (q->num != 0)
    {
        int idx = get_oldest_index(q);
        element = q->mem[idx];
        q->num = q->num - 1;
    }

    return element;
}

static void print(queue_t* q)
{
    int oldest = get_oldest_index(q);
    printf("Num = %d, Old = %d, New = %d\r\n", q->num, oldest, q->newest);
    for (int i = 0; i < q->num; i++)
    {
        int idx = (oldest + i) % QUEUE_SIZE;
        printf("\t%d\r\n", q->mem[idx]);
    }

    if (q->num == 0)
    {
        printf("\t(Empty)\r\n");
    }
}

int main(void)
{
    /* Allocate queue */
    queue_t* q = create();

    /* Insert 5 elements */
    enqueue(q, 5);
    enqueue(q, 6);
    enqueue(q, 7);
    enqueue(q, 8);
    enqueue(q, 9);
    print(q);

    /* Insert 4 elements, only element 9 should remain */
    enqueue(q, 1);
    enqueue(q, 2);
    enqueue(q, 3);
    enqueue(q, 4);
    print(q);

    /* In LIFO, oldest elements should be dequeued first */
    assert(dequeue(q) == 9);
    assert(dequeue(q) == 1);
    assert(dequeue(q) == 2);
    assert(dequeue(q) == 3);
    assert(dequeue(q) == 4);
    print(q);

    /* Insert 3 elements */
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    print(q);

    /* Free queue */
    delete(q);

    return 0;
}
