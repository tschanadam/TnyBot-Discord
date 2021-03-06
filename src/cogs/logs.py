import os

from discord import Channel

from src.cogs import BaseCog


class Logs(BaseCog):
    _logs_dir = "res/logs"

    async def on_message(self, message):
        # If you thought I would log this you're crazy...
        pass

    async def on_message_delete(self, message):
        channel = message.channel
        author = message.author
        log_msg = "deleted: '{1}' from: {0} in #{2}".format(author.name, message.content, channel.name)
        self.log(log_msg, channel)
        pass

    async def on_message_edit(self, before, after):
        pass

    async def on_channel_delete(self, channel):
        pass

    async def on_channel_create(self, channel):
        pass

    async def on_channel_update(self, before, after):
        pass

    async def on_member_join(self, member):
        pass

    async def on_member_remove(self, member):
        pass

    async def on_member_update(self, before, after):
        pass

    async def on_server_update(self, before, after):
        pass

    async def on_server_role_create(self, role):
        pass

    async def on_server_role_delete(self, role):
        pass

    async def on_server_role_update(self, before, after):
        pass

    async def on_server_emojis_update(self, before, after):
        pass

    async def on_member_ban(self, member):
        pass

    async def on_member_unban(self, server, user):
        pass

    async def on_pin_add(self, message):
        pass

    async def on_pin_remove(self, message):
        pass

    def log(self, message: str, channel: Channel):
        path = self._get_channel_log(channel)
        with open(path, "a+") as f:
            f.write(message + "\n")

    def _get_channel_log(self, channel: Channel):
        server_dir = channel.server.name
        server_dir = server_dir.strip(".")
        channel = channel.name
        path = self._logs_dir + "/" + server_dir
        if not os.path.exists(path):
            os.makedirs(path)
        return path + "/" + channel + ".log"


def setup(bot, kwargs):
    bot.add_cog(Logs(bot))
