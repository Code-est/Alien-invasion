class Settings():
     #"""����� ��� �������� ���� �������� ���� Alien Invasion."""
     def __init__(self):
     #"""�������������� ��������� ����."""
         # ��������� ������
         self.screen_width = 1200
         self.screen_height = 800
         self.bg_color = (28, 26, 28)
         # ��������� �������
         self.ship_speed = 1.5
         self.ship_limit = 3
         # ��������� �������
         self.bullet_speed = 1.5
         self.bullet_width = 3
         self.bullet_height = 15
         self.bullet_color = (235, 42, 237)
         self.bullets_allowed = 3
         # ��������� ����������
         self.alien_speed = 1.0
         self.fleet_drop_speed = 10
         #���� ��������� ����
         self.speedup_scale = 1.1
         self.initialize_dynamic_settings()
         # ���� ����� ��������� ����������      
         self.score_scale = 1.5

       
     def initialize_dynamic_settings(self):
         #"""�������������� ���������, ������������ � ���� ����."""
         self.ship_speed_factor = 1.5
         self.bullet_speed_factor = 3.0
         self.alien_speed_factor = 1.0
         # fleet_direction = 1 ���������� �������� ������; � -1 - �����.
         self.fleet_direction = 1
         # ������� �����
         self.alien_points = 50
     

     def increase_speed(self):
         #"""����������� ��������� �������� � ��������� ����������."""
         self.ship_speed_factor *= self.speedup_scale
         self.bullet_speed_factor *= self.speedup_scale
         self.alien_speed_factor *= self.speedup_scale

         self.alien_points = int(self.alien_points * self.score_scale)
         print(self.alien_points)