#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check is list linked is a cycle
 * @list: ptr to the list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast = slow)
			return (1);
	}
	return (0);
}
