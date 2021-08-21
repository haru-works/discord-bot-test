import discord
from discord.ext import commands
import traceback
import sys

# コマンドエラーハンドラークラス
class CommandErrorHandler(commands.Cog):
    # コンストラクタ
    def __init__(self, bot):
        self.bot = bot
       
    # コマンドエラーイベント検知       
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        # ローカルのイベントハンドラーは処理終了
        if hasattr(ctx.command, 'on_error'):
            return
        
        # cogのイベントハンドラーをチェック
        if ctx.cog:
            cog = ctx.cog
            # Cogのオーバーライドメソッドのcog_command_errorがなければ処理終了
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
            
        # original属性取得
        error = getattr(error, 'original', error)

        # 無視リスト生成    
        ignored = (commands.CommandNotFound, )
        if isinstance(error, ignored):
            return
        
        # DisabledCommandエラー
        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} のコマンドは無効です')
            
        # NoPrivateMessageエラー
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} はプライベートメッセージでは使用できません')
            except discord.HTTPException:
                pass

        # BadArgumentエラー
        elif isinstance(error, commands.BadArgument):
            # どのコマンドの引数が悪かったのかチェック
            # まだ未実装            
            #if ctx.command.qualified_name == 'ping': 
            #await ctx.send('入力したコマンドの引数が無効です')     
            return

        # MissingPermissionsエラー          
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("あなたは、コマンドを実行する権限を持っていません")
            return
        # その他エラー
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
         
def setup(bot):
    return bot.add_cog(CommandErrorHandler(bot))