#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: pointer
 * Return: address of new element
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *first = NULL, *second = *head, *last = NULL;

	while (second != NULL)
	{
		last = second->next;
		second->next = first;
		first = second;
		second = last;
	}
	*head = first;
	return (*head);
}

/**
 * length_list - get the length
 * @head: the head pointer
 * Return: length of linked list
 */

int length_list(listint_t **head)
{
	int j;
	listint_t *first = *head;

	for (j = 0; first != NULL; j++)
		first = first->next;
	return (j);
}

/**
 * is_palindrome - checks whether a linked list is
 * palindrome
 * @head: head node
 * Return: 1 if palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *new_head;
	listint_t *first = *head;
	listint_t *first_new;
	int length = length_list(head);
	int mid_length = length / 2;
	int i;

	new_head = *head;
	for (i = 0; i < mid_length; i++)
		new_head = new_head->next;
	if (length % 2 != 0)
		new_head = new_head->next;
	new_head = reverse_list(&new_head);
	first_new = new_head;
	first = *head;
	while (first_new != NULL)
	{
		if (first_new->n != first->n)
			return (0);
		first_new = first_new->next;
		first = first->next;
	}
	return (1);
}
