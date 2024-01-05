namespace SpriteKind {
    export const Misc = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    game_player.sayText(game.askForString("Please enter your speech content: ", 24), 2000, false)
})
let game_player: Sprite = null
let item_number = 0
scene.setBackgroundColor(9)
tiles.setCurrentTilemap(tilemap`Level1`)
game_player = sprites.create(assets.image`player`, SpriteKind.Player)
game_player.x = 80
game_player.y = 192
controller.moveSprite(game_player)
scene.cameraFollowSprite(game_player)
