#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: double pointer to head node
 * @number: number to be inserted
 * Return: address of new nod on success, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *hold;

	if (head == NULL)
		return (NULL);
	hold = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (hold->n > number)
	{
		*head = new;
		new->next = hold;
		return (new);
	}
	while (hold->next != NULL)
	{
		if (hold->next->n > number)
		{
			new->next = hold->next;
			hold->next = new;
			return (new);
		}
		hold = hold->next;
	}
	hold->next = new;
	return (new);
}
