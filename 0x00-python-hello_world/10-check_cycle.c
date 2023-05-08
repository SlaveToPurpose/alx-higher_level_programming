#include "lists.h"

/**
 * check_cycle - checks if list contains a cycle
 * @list: pointer to head of list
 * Return: 0 if a cycle is not present, 1 if cycle is present
 */


int check_cycle(listint_t *list)
{
	listint_t *current_head;
	listint_t *current_node;


	current_head = list;
	current_node = list;

	while (1)
	{
		current_node = current_node->next;

		if (current_node == NULL)
			return (0);
		if (current_head == current_node)
			return (1);
	}
}
