# my-project-g-agent
# CodeOrchestra: 全流程自动化软件工程智能体

> 基于多 Agent 协作的代码生成、审查与自修复系统

## 痛点
传统开发中，审查、测试、Bug 修复等重复性劳动占用了开发人员 60% 以上的时间。孤立的 AI 编码工具缺乏闭环验证，容易产生无法运行的代码。

## 核心逻辑流
本系统模拟一个微型虚拟软件公司，由多个专业 Agent 协作完成 **长链推理**：
1. **需求分析 Agent** – 将自然语言需求拆解为技术规格  
2. **编码 Agent** – 根据规格生成代码  
3. **审查 Agent** – 审查代码质量、安全和架构  
4. **测试 Agent** – 自动生成并运行单元测试  
5. **修复闭环** – 审查/测试失败的代码会循环进入编码→审查→测试，直至通过  

## 技术栈
- **多 Agent 协作**：每个 Agent 独立运行，通过 orchestrator 调度通信  
- **长链推理**：完整覆盖 “需求→编码→审查→测试→修复” 的推理链  
- **可插拔 LLM 后端**：支持本地模拟 (demo) 和真实 API (OpenAI / 小米 MiMo 等)

## 快速开始
```bash
# 安装依赖
pip install -r requirements.txt

# 演示模式（无需 API Key，使用模拟 Agent）
python main.py --demo

# 接入真实 API（需配置环境变量）
export LLM_API_BASE="https://api.mimo.xiaomi.com/v1"   # 示例
export LLM_API_KEY="your-key"
python main.py
agent/api/LLM
