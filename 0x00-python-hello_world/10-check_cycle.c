#include "lists.h"

/**
 * check_cycle - check for cycle
 * Description: Checks a singly linked list for a cycle.
 * @list: Head of the list
 * Return: 1 if a cycle is found, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr_1 = list;
	listint_t *ptr_2 = list;

	if (list == NULL)
		return (0);

	if (list->next == NULL)
		return (0);

	ptr_1 = list->next;
	if (ptr_1->next == NULL)
		return (0);
	ptr_2 = ptr_1->next;
	while (1)
	{
		if (ptr_1 == ptr_2)
			return (1);
		if (ptr_1->next == NULL || ptr_2->next == NULL)
			return (0);
		ptr_1 = ptr_1->next;
		ptr_2 = ptr_2->next;
		if (ptr_2->next == NULL)
			return (0);
		ptr_2 = ptr_2->next;
	}
}
