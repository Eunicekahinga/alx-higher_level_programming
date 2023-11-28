#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number to a sorted linked list.
 * @head: Pointer to the head node
 * @number: the number to be inserted
 * Return: new node address else NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && number > current->next->n)
			current = current->next;
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
