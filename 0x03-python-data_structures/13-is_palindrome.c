#include "lists.h"
/**
 * get_max_node - get_max_node
 * @head: pointer to head of list
 * Return: number of nodes
 */

int get_max_node(listint_t **head)
{
	listint_t *ptr = *head;
	int i = 0;

	while (ptr)
	{
		ptr = ptr->next;
		i++;
	}
	return (i);
}

/**
 * get_node_index - get_node_index
 * @head: pointer to head of list
 * @index: index
 * Return: number of nodes
 */

int get_node_index(listint_t *head, int index)
{
	listint_t *ptr = head;
	int i = 0;

	while (i < index)
	{
		ptr = ptr->next;
		i++;
	}
	if (ptr)
		return (ptr->n);
	else
		return (-1);
}

/**
 * is_palindrome - is_palindrome
 * @head: pointer to head of list
 * Return: number of nodes
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptrTop = *head;
	listint_t *ptrBot = *head;
	int i = 0;
	int cpTop = 0;
	int cpBot = 0;

	cpTop = get_max_node(head) - 1;
	while (cpTop > cpBot)
	{
		if (get_node_index(ptrTop, cpTop) != get_node_index(ptrBot, cpBot))
			return (-1);
		cpTop--;
		cpBot++;
	}
	return (1);
}
