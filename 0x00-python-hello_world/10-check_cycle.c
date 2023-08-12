#include "lists.h"

/**
 * check_cycle - checks for cycle in linked list
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is acycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp, *head;

	if (list == NULL)
		return (0);

	tmp = list;
	head = list;

	while (head->next != NULL && tmp != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		tmp = tmp->next;

		if (head == tmp)
			return (1);
	}

	return (0);
}
