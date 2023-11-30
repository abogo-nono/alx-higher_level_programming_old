#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert an element in sorted list
 * @head: the list
 * @number: element to add
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next != NULL)
	{
		if (current->next->n >= new->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}

		current = current->next;
	}

	current->next = new;
	new->next = NULL;

	return (new);
}
