import disco
import gevent
from rowboat.plugins import RowboatPlugin as Plugin, CommandFail, CommandSuccess
from disco.bot import CommandLevels
from rowboat.types.plugin import PluginConfig
from rowboat.redis import rdb
from disco.types.user import User as DiscoUser
from disco.types.message import MessageTable, MessageEmbed
from rowboat.types import Field, DictField, ListField, snowflake, SlottedModel, snowflake
from gevent.pool import Pool
from rowboat.util.gevent import wait_many


class MemesConfig(PluginConfig):
    #auto-reply to meesux
    hate_meesux = Field(bool, default=False)
@Plugin.with_config(MemesConfig)
class MemesPlugin(Plugin):
    def load(self, ctx):
        super(MemesPlugin, self).load(ctx)
    
    @Plugin.listen('MessageCreate')
    def alexa_play_despacito_listener(self, event):
        if "hey alexa" in event.content and event.author.id == 191793155685744640:
            msg = event.channel.send_message('<a:hey_alexa:473213508171989023>')
            try:
                alexa_event = self.wait_for_event(
                    'MessageCreate',
                    conditional=lambda e: (
                        e.author.id == event.author.id
                    )).get(timeout=10)
                #  despacito
                if "play despacito" in alexa_event.content:
                    msg.delete()
                    event.channel.send_message('Ok, playing Despacito on <:spotify:473223054831517727>')
                    def g():
                        event.channel.send_message('des')
                        gevent.sleep(.5)
                        event.channel.send_message('pa')
                        gevent.sleep(.5)
                        event.channel.send_message('cito')
                    gevent.spawn(g)

                # timer
                # if "set a timer for" in alexa_event.content.lower():
                #     msg.delete()

            except gevent.Timeout:
                msg.delete()
                return
            


    @Plugin.listen('MessageCreate')
    def meesucks_listener(self, event):
        if event.config.hate_meesux is True:
            if event.author.id == 159985870458322944:
                return event.channel.send_message('<@159985870458322944> **NO ONE CARES.**')

    @Plugin.command('pong', level=-1)
    def pong(self, event):
        return event.msg.reply('I pong, you ping. Idiot...')