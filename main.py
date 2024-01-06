@namespace
class SpriteKind:
    Misc = SpriteKind.create()

def on_a_pressed():
    game_player.say_text(game.ask_for_string("Please enter your speech content: ", 24),
        2000,
        False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

game_player: Sprite = None
item_number = 0
scene.set_background_color(9)
tiles.set_current_tilemap(tilemap("""
    Level1
"""))
game_player = sprites.create(assets.image("""
    player
"""), SpriteKind.player)
game_player.x = 80
game_player.y = 192
controller.move_sprite(game_player)
scene.camera_follow_sprite(game_player)