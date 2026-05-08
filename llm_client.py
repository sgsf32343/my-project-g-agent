import openai
from config import LLM_API_BASE, LLM_API_KEY, LLM_MODEL, DEMO_MODE

def call_llm(system_prompt: str, user_prompt: str, agent_name: str = "Agent") -> str:
    """统一 LLM 调用接口，支持模拟和真实 API"""
    if DEMO_MODE:
        return mock_response(agent_name, user_prompt)

    client = openai.OpenAI(
        base_url=LLM_API_BASE,
        api_key=LLM_API_KEY
    )
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

def mock_response(agent_name: str, user_prompt: str) -> str:
    """模拟 Agent 响应，用于演示完整推理链（无需 API Key）"""
    if "需求分析" in agent_name:
        return '{"spec": "实现一个函数，输入两个整数，返回它们的和", "signature": "def add(a: int, b: int) -> int"}'
    elif "编码" in agent_name or "Coder" in agent_name:
        # 故意返回一个有 bug 的代码（在第二次修复时返回正确代码）
        if "修复" in user_prompt.lower() or "fix" in user_prompt.lower():
            return "def add(a: int, b: int) -> int:\n    return a + b"
        else:
            return "def add(a: int, b: int) -> int:\n    return a - b"   # bug: 减法
    elif "审查" in agent_name or "Reviewer" in agent_name:
        if "a - b" in user_prompt:
            return "【审查不通过】Bug: 使用了减法而非加法。请修正为 a + b"
        else:
            return "【审查通过】代码安全且符合规范。"
    elif "测试" in agent_name or "Tester" in agent_name:
        if "a - b" in user_prompt:
            return "【测试失败】assert add(3, 5) == 8, 实际输出 -2"
        else:
            return "【测试通过】所有用例通过。"
    return "模拟响应：任务完成"
