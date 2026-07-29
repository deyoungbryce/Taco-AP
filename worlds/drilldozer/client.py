from typing import TYPE_CHECKING, Tuple, Dict

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from NetUtils import ClientStatus, NetworkItem

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor


class DrillDozerClient(BizHawkClient):
    game = "Drill Dozer"
    system = "GBA"
    patch_suffix = ".dozer"

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x00, 6, "ROM")]))[0]).decode("ascii")
            if rom_name != "MYGAME":
                return False
        except bizhawk.RequestFailedError:
            return False
        
        ctx.game = self.game
        ctx.items_handling = 0b00
        ctx.want_slot_data = True

        return True
    
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:
            save_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [(0x00, 20, "System Bus")]
            )[0]

            if save_data[2] & 0x00:
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": [23]
                }])

            if not ctx.finished_game and (save_data[5] & 0x00):
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

        except bizhawk.RequestFailedError:
            pass