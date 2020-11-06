/*
 * Various linked list problems.
 */

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct node
{
    struct node* next;
    uint32_t val;
} node_t;

static node_t* makeNode(uint32_t val)
{
    node_t* node = (node_t*) malloc(sizeof(node_t));
    node->next = NULL;
    node->val = val;
    return node;
}

static void listAdd(node_t* head, uint32_t val)
{
    assert(head != NULL);

    node_t* curr = head;
    while (curr->next != NULL)
    {
        curr = curr->next;
    }

    curr->next = makeNode(val);
}

static void listPrint(node_t* head)
{
    node_t* curr = head;
    while (curr != NULL)
    {
        printf("%u\t", curr->val);
        curr = curr->next;
    }

    printf("\r\n");
}

static void listDelete(node_t* head)
{
    node_t* curr = head;
    while (curr != NULL)
    {
        node_t* tmp = curr->next;
        free(curr);
        curr = tmp;
    }
}

static node_t* listReverse(node_t* head)
{
    node_t* prev = NULL;
    node_t* curr = head;

    while (curr != NULL)
    {
        /* Save for later */
        node_t* next = curr->next;

        /* Turn next pointer around */
        curr->next = prev;

        /* Next node */
        prev = curr;
        curr = next;
    }

    return prev;
}

static node_t* listReverseRecursive(node_t* prev, node_t* head)
{
    if (head == NULL)
    {
        return prev;
    }
    else
    {
        node_t* next = head->next;
        head->next = prev;
        return listReverseRecursive(head, next);
    }
}

static node_t* listSort(node_t* head)
{
    if (head == NULL)
    {
        return head;
    }

    /* Bubble sort */
    bool change = true;
    node_t* start = head;
    while (change)
    {
        change = false;
        node_t* prev = NULL;
        node_t* curr = start;
        node_t* next = start->next;
        while (next != NULL)
        {
            if (curr->val > next->val)
            {
                change = true;

                if (prev != NULL)
                {
                    prev->next = next;
                }
                else
                {
                    start = next;
                }

                node_t* tmp = next->next;
                next->next = curr;
                curr->next = tmp;

                prev = next;
                curr = curr;
                next = curr->next;
            }
            else
            {
                prev = curr;
                curr = next;
                next = next->next;
            }
        }
    }

    return start;
}

int main(void)
{
    node_t* head = makeNode(9);
    listAdd(head, 12);
    listAdd(head, 15);
    listAdd(head, 42);

    printf("\r\nInitial list:\r\n");
    listPrint(head);

    printf("\r\nReversed linked list (iterative):\r\n");
    head = listReverse(head);
    listPrint(head);

    printf("\r\nReversed linked list (recursive):\r\n");
    head = listReverseRecursive(NULL, head);
    listPrint(head);

    listDelete(head);

    node_t* head2 = makeNode(10);
    listAdd(head2, 9);
    listAdd(head2, 8);
    listAdd(head2, 20);
    listAdd(head2, 1);
    listAdd(head2, 7);

    printf("\r\nInitial list:\r\n");
    listPrint(head2);

    printf("\r\nSorted linked list:\r\n");
    head2 = listSort(head2);
    listPrint(head2);

    listDelete(head2);

    return 0;
}
