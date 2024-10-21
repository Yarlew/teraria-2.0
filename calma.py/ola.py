import arcade

# Configurações da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classe para o jogo
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Terraria Clone")
        # Posição inicial do jogador
        self.player_x = 400
        self.player_y = 300
        self.player_speed = 5

    def on_draw(self):
        arcade.start_render()
        # Desenhar o jogador como um retângulo verde
        arcade.draw_rectangle_filled(self.player_x, self.player_y, 50, 50, arcade.color.GREEN)

    def on_update(self, delta_time):
        pass  # Atualizações de lógica do jogo

    def on_key_press(self, key, modifiers):
        # Movimentação do jogador
        if key == arcade.key.LEFT:
            self.player_x -= self.player_speed
        elif key == arcade.key.RIGHT:
            self.player_x += self.player_speed
        elif key == arcade.key.UP:
            self.player_y += self.player_speed
        elif key == arcade.key.DOWN:
            self.player_y -= self.player_speed

# Iniciar o jogo
window = MyGame()
arcade.run()
