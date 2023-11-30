#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a list has a circle
 * @list: the list
 * Return: bool
*/
int check_cycle(listint_t *list)
{
	const listint_t *fast = list, *slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
		}

	return (0);
}
