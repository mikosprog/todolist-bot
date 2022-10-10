from discord.ext import commands

from main import client


class Todolist:  # Skeleton of 'Todolist' class
    def __init__(self, elements: list[str], num_of_elements: int):
        self.elements = elements
        self.num_of_elements = num_of_elements

    def save_to_file(self):
        return

    def read_from_file(self):
        return


class TodolistCommands(commands.Cog):   # Skeleton of 'TodolistCommands' class
    def __init__(self):
        self.client = client

    @commands.command(name="printList")
    async def print_list(self, ctx):
        return

    @commands.command(name="markAsDone")
    async def mark_as_done(self, ctx):
        return

    @commands.command(name="markAsNotDone")
    async def mark_as_not_done(self, ctx):
        return

    @commands.command(name="createList")
    async def create_list(self, ctx):
        return

    @commands.command(name="removeList")
    async def remove_list(self, ctx):
        return
