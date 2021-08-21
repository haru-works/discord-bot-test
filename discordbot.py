import discord
from discord.ext import commands
from os import getenv
import traceback
import confile

# INITIAL_EXTENSIONSの設定
INITIAL_EXTENSIONS = [
    'cogs.cog_command_sample',
    'cogs.command_error_handler'
    ]

# SampleBot クラス
class SampleBot(commands.Bot):
    # コンストラクタ
    def __init__(self, command_prefix):
        
        # prefix設定
        super().__init__(command_prefix)      

        # INITIAL_EXTENSIONSに格納されている名前からcogを読込
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()
        
    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('--- Discord Bot ready! ---')
        print(self.user.name)
        print(self.user.id)
        print('--------------------------')
        
         
# Botのインスタンス化、及び、起動処理
if __name__ == '__main__':
    bot_config = confile.read_config('setting.ini')
    token = bot_config.get_property('bot', 'token')   
    bot = SampleBot(command_prefix='!') 
    bot.run(token) 
                    

