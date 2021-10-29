from redbot.core import data_manager

from .randomwork import RandomWork


def setup(bot):
    plant = RandomWork(bot)
    data_manager.bundled_data_path(plant)
    bot.add_cog(plant)
