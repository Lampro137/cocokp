from openai import OpenAI
import time
import json
from flask import Flask, request, jsonify

# 创建Flask应用
app = Flask(__name__)

class ModelScopeAgent:
    def __init__(self, system_prompt=""):
        self.system_prompt = system_prompt
        self.conversation_history = []
    
    def reset_conversation(self):
        self.conversation_history = []
    
    def update_system_prompt(self, system_prompt):
        try:
            self.system_prompt = system_prompt
            return "系统提示已更新"
        except Exception as e:
            return f"更新失败: {str(e)}"
    
    def chat(self, message, stream=False):
        # 将消息添加到历史记录
        self.conversation_history.append({"role": "user", "content": message})
        
        # 简单的响应生成逻辑
        response = self._generate_response(message)
        
        # 将AI响应添加到历史记录
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def _generate_response(self, message):
        # 基于消息内容生成简单的响应
        message_lower = message.lower()
        
        # 基于不同关键词的响应
        if any(keyword in message_lower for keyword in ['调查', '检查', '搜索']):
            return "你仔细检查了周围，发现了一些有趣的线索。"
        elif any(keyword in message_lower for keyword in ['交谈', '对话', '询问']):
            return "对方警惕地回应了你的问题。"
        elif any(keyword in message_lower for keyword in ['移动', '前往', '离开']):
            return "你来到了一个新的地方，环境有些不同寻常。"
        elif any(keyword in message_lower for keyword in ['检定', '骰子', '投骰']):
            return "进行智力检定：你掷出了12，成功了！"
        elif any(keyword in message_lower for keyword in ['技能', '属性', '状态']):
            return "请描述你想了解的具体技能或属性。"
        elif any(keyword in message_lower for keyword in ['休息', '恢复', '等待']):
            return "你稍作休息，恢复了一些精力。"
        elif any(keyword in message_lower for keyword in ['规则', '帮助', '指导']):
            return "克苏鲁的呼唤是一个恐怖题材的角色扮演游戏，你需要通过检定来完成各种行动。"
        else:
            # 默认响应
            return "你的行动产生了一些影响，接下来你想怎么做？"

# 创建全局智能体实例
# 定义COC KP的系统提示
kp_system_prompt = """你是一名专业的克苏鲁神话跑团游戏(Keeper of Arcane Lore)主持人。你的职责是：
1. 简洁直接地描述场景和事件，避免过度冗长的描写
2. 精确回应玩家的行动和技能检定，只描述玩家明确执行的动作
3. 推进剧情发展，保持适度的紧张氛围
4. 合理判定玩家行动的成功与否及其后果
5. 根据玩家的理智状态调整描述的恐怖程度

请注意：
- 回复要简洁明了，避免冗余内容
- 不要臆测玩家未明确描述的行为或心理活动
- 聚焦于提供游戏必要信息和剧情发展
- 用中文回复，保持克苏鲁神话的神秘氛围但不过度渲染"""

agent = ModelScopeAgent(system_prompt=kp_system_prompt)

# 定义API端点
@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    # 处理预检请求
    if request.method == 'OPTIONS':
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    
    # 处理POST请求
    try:
        # 获取请求数据
        data = request.get_json()
        
        # 获取请求参数
        message = data.get('message', '')
        system_prompt = data.get('system_prompt')
        reset = data.get('reset', False)
        
        # 处理重置请求
        if reset:
            agent.reset_conversation()
            response_data = {'status': 'success', 'message': '对话已重置'}
        # 处理更新系统提示请求
        elif system_prompt:
            result = agent.update_system_prompt(system_prompt)
            response_data = {'status': 'success', 'message': result}
        # 处理聊天请求
        elif message:
            response = agent.chat(message, stream=False)
            if response:
                response_data = {'status': 'success', 'response': response}
            else:
                response_data = {'status': 'error', 'message': 'API调用失败'}
        else:
            response_data = {'status': 'error', 'message': '缺少必要参数'}
        
        # 返回响应
        response = jsonify(response_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# 处理所有其他路径，作为备用
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'status': 'error', 'message': 'Not Found'}), 404

# 导出Flask应用作为Vercel的入口点
export = app

# 如果直接运行此脚本，启动本地服务器
if __name__ == "__main__":
    print("COC KP AI服务已启动！")
    print("本地服务器运行在: http://localhost:8080")
    print("可通过/api/chat端点与AI交互")
    app.run(host='localhost', port=8080, debug=True)