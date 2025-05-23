import json
import os
from typing import Dict, List, Optional

class RealEstateMarketingAssistant:
    def __init__(self, config_path: str):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
    def parse_info(self, text: str) -> Dict:
        """解析房源信息文本，提取关键数据和卖点"""
        result = {
            'key_data': {},
            'selling_points': [],
            'special_tags': []
        }
        
        # 提取特殊标签
        for tag in self.config['info_parser']['special_tags']:
            if tag in text:
                result['special_tags'].append(tag)
        
        # TODO: 实现更复杂的文本解析逻辑
        return result
    
    def generate_visual(self, info: Dict) -> Dict:
        """生成营销图片和地图"""
        result = {
            'marketing_image': None,
            'location_map': None
        }
        
        # 配置图片生成参数
        image_config = self.config['visual_generator']['image']
        map_config = self.config['visual_generator']['map']
        
        # 生成地图
        try:
            from map_generator import MapGenerator
            config_path = os.path.abspath('config.json')
            map_gen = MapGenerator(config_path)
            
            # 设置田安小区的大致位置（沙河市中心位置）
            location = {
                'lat': 37.19,  # 沙河市中心纬度
                'lng': 114.34  # 沙河市中心经度
            }
            
            # 生成地图
            result['location_map'] = map_gen.generate_location_map(location)
        except Exception as e:
            print(f"地图生成失败: {str(e)}")
        
        return result
    
    def generate_content(self, info: Dict, template_name: str) -> str:
        """根据模板生成营销文案"""
        # 获取指定模板
        template = next(
            (t for t in self.config['templates'] if t['name'] == template_name),
            self.config['templates'][0]  # 默认使用第一个模板
        )
        
        # 获取文案生成配置
        content_config = self.config['content_generator']
        
        # TODO: 实现文案生成逻辑
        content = template['structure']
        
        # 添加必要话题标签
        content += '\n' + ' '.join(content_config['required_tags'])
        
        return content
    
    def process_house_info(self, text: str, template_name: Optional[str] = None) -> Dict:
        """处理房源信息的主流程"""
        # 1. 解析信息
        info = self.parse_info(text)
        
        # 2. 生成视觉内容
        visuals = self.generate_visual(info)
        
        # 3. 生成营销文案
        content = self.generate_content(info, template_name) if template_name else [
            self.generate_content(info, t['name']) for t in self.config['templates']
        ]
        
        return {
            'info': info,
            'visuals': visuals,
            'content': content
        }

def main():
    # 初始化助手
    assistant = RealEstateMarketingAssistant('config.json')
    
    # 测试用例
    test_input = "急售！世纪公园旁电梯两房，建面89平中间楼层，满五唯一税费省10万，对口明珠小学，房东置换诚意出售"
    
    # 处理测试用例
    result = assistant.process_house_info(test_input)
    
    # 输出结果
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()