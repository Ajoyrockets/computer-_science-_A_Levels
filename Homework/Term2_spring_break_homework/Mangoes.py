"""
Introduction
The mango season has arrived. A market stall purchases mangoes in the morning and sells them throughout the day. Any unsold mangoes are carried over to the next day. The stall owner ensures that older mangoes are sold before newer ones.

A 3-Day Example

Day 1: Buy 10 mangoes, sell 6 mangoes (0 old, 6 fresh). Keep 4 mangoes.
Day 2: Buy 5 mangoes, sell 7 mangoes (4 old, 3 fresh). Keep 2 mangoes.
Day 3: Buy 1 mango, sell 3 mangoes (2 old, 1 fresh).
A total of 6 + 3 + 1 = 10 fresh mangoes were sold during the 3-day period.

Visual representation of the example. (Not required by SVI students.)

Task
Write a program that calculates and outputs the total number of fresh mangoes sold over a specified number of days.
For each day, the input will include the number of mangoes bought and the number of mangoes sold. Fresh mangoes are defined as those sold on the same day they were purchased. The program should sum up the fresh mangoes sold over the entire period and output the result.

Input format
The input consists of multiple lines:

Line 1: An integer, n, representing the number of days (max 7) of mango buying and selling.
Next n lines: Each line contains two integers separated by a space. The first integer represents the number of mangoes bought on that day (max 100), and the second integer represents the number of mangoes sold on that day. (max 100)
Output format
An integer representing the total number of fresh mangoes sold (mangoes sold on the same day they were bought).
"""