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
 * is_palindrome - is_palindrome
 * @head: pointer to head of list
 * Return: number of nodes
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int cpTop = 0;
	int *tab;
	int i = 0;
	
	if (*head == NULL)
		return (1);
	cpTop = get_max_node(head) - 1;
	tab = malloc(sizeof(tab) * cpTop);
	while (ptr)
	{
		tab[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	i = 0
	while (cpTop > i)
	{
		if (tab[i] != tab[cpTop])
			return (0);
		cpTop--;
		i++;
	}
	return (1);
}
