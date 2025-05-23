import os
import json
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Optional, Tuple, List

class MapGenerator:
    def __init__(self, config_path: str):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # 地图默认配置
        self.default_size = (800, 600)
        self.overlay_opacity = 0.15  # 15%透明度
        self.city_bounds = {
            'min_lat': 37.14,  # 沙河市边界范围
            'max_lat': 37.24,
            'min_lng': 114.29,
            'max_lng': 114.39
        }
    
    def create_base_map(self) -> Image.Image:
        """创建基础地图画布"""
        # 创建空白画布
        img = Image.new('RGB', self.default_size, 'white')
        draw = ImageDraw.Draw(img)
        
        # 绘制边框
        draw.rectangle([0, 0, self.default_size[0]-1, self.default_size[1]-1], outline='black')
        
        return img
    
    def add_location_marker(self, img: Image.Image, location: Dict[str, float]) -> Image.Image:
        """添加位置标记"""
        draw = ImageDraw.Draw(img)
        
        # 将经纬度转换为像素坐标
        x = int((location['lng'] - self.city_bounds['min_lng']) / 
                (self.city_bounds['max_lng'] - self.city_bounds['min_lng']) * self.default_size[0])
        y = int((self.city_bounds['max_lat'] - location['lat']) / 
                (self.city_bounds['max_lat'] - self.city_bounds['min_lat']) * self.default_size[1])
        
        # 绘制标记点
        marker_size = 10
        draw.ellipse([x-marker_size, y-marker_size, x+marker_size, y+marker_size], 
                     fill='#DB3B1F')  # 使用品牌红色
        
        return img
    
    def add_traffic_routes(self, img: Image.Image, routes: List[Dict]) -> Image.Image:
        """添加交通路线"""
        draw = ImageDraw.Draw(img)
        
        # 创建半透明覆盖层
        overlay = Image.new('RGBA', self.default_size, (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # 绘制路线
        for route in routes:
            points = [(int(p['lng']), int(p['lat'])) for p in route['points']]
            overlay_draw.line(points, fill=(42, 92, 170, int(255 * self.overlay_opacity)))  # 使用信任蓝色
        
        # 合并图层
        img = Image.alpha_composite(img.convert('RGBA'), overlay)
        
        return img
    
    def generate_location_map(self, location: Dict[str, float], 
                            routes: Optional[List[Dict]] = None) -> str:
        """生成位置地图"""
        # 创建基础地图
        map_img = self.create_base_map()
        
        # 添加位置标记
        map_img = self.add_location_marker(map_img, location)
        
        # 添加交通路线（如果提供）
        if routes:
            map_img = self.add_traffic_routes(map_img, routes)
        
        # 保存地图
        output_path = os.path.join(os.path.dirname(self.config_path), 'output', 'location_map.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        map_img.save(output_path)
        
        return output_path