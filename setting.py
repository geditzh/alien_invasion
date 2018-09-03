class Settings():
    # 存储游戏中的所有设置的类
    def __init__(self):
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 设置外星人
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        # fleet_direcion为1表示右移,为-1表示左移
        self.fleet_direction = 1
