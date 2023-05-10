#include "lists.h"

/**
 * insert_node - insert node into list
 * @head: pointer to head of list
 * @number: number to be entered into  node
 * Return: the address of the new_node node on success else NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current_node;
    

    current_node = *head;
    /*allocate space for new_node node*/
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    /*save given number in n of new_node node*/
    new_node->n = number;
    /*check for empty list*/
    while (current_node == NULL)
    {
        *head = new_node;
        new_node->next = NULL;
        return (new_node);
    }
    /*add node to front of list if smaller than head*/
    while (current_node->n > number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }
    while (current_node->next != NULL)
    {
        if ((current_node->next)->n >= number)
        {
            new_node->next = current_node->next;
            current_node->next = new_node;
            return (new_node);
        }
        current_node = current_node->next;
    }
    /*else add node to end*/
    new_node->next = NULL;
    current_node->next = new_node;
    return (new_node);
}