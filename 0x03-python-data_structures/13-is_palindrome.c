#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer that points to the head of a singly linked list
 *
 * Return: results
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *next = slow->next;

		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
