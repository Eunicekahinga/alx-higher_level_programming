#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks for a cycle in single-linked lists.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0 else 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tee, *jey;

	if (list == NULL || list->next == NULL)
		return (0);

	tee = list->next;
	jey = list->next->next;

	while (tee && jey && jey->next)
	{
		if (tee == jey)
			return (1);

		tee = tee->next;
		jey = jey->next->next;
	}

	return (0);
}
