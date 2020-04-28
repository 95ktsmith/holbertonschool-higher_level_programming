#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a node in an ordered list
 * @head: Head of the linked list
 * @number: Number to assign the to the new node
 * Return: Address of the new node if successful, NULL in failure.
 */

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
        *head = new_node;
    }
    else if (number <= current->n)
    {
        new_node->next = current;
        *head = new_node;
    }
    else
    {
        while(current->next && number > current->next->n)
            current = current->next;
        new_node->next = current->next;
        current->next = new_node;
    }
    return (new_node);
}