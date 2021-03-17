from patchnotesparser.patchnotesparser_main import PatchNotesParser
from redbot.core.bot import Red


def setup(bot: Red) -> None:
    bot.add_cog(PatchNotesParser(bot))