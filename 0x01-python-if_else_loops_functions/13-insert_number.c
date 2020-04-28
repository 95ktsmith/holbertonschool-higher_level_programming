#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current = *head;

    if (head == NULL)
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;

    if (current == NULL)
    {
        new_node->next = NULL;
        current = new_node;
    }
    else
    {
        while(current && current->next && number > current->next->n)
            current = current->next;
        new_node->next = current->next;
        current->next = new_node;
    }
    return (new_node);
}